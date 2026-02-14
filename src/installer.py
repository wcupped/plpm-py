import os
import re
import stat
import subprocess
import requests
from pathlib import Path
from tqdm import tqdm
from config import DOWNLOADS_DIR, HASHES_FILE
from utils import compare_hashes
import json


def get_install_command(installer_path):
    path_lower = installer_path.lower()

    if path_lower.endswith(".msi"):
        return ["msiexec", "/i", installer_path, "/qn", "/norestart"]

    try:
        with open(installer_path, "rb") as f:
            header = f.read(1024 * 1024)

        if b"Inno Setup" in header:
            return [installer_path, "/VERYSILENT", "/SUPPRESSMSGBOXES", "/NORESTART"]

        if b"NullsoftInst" in header:
            return [installer_path, "/S"]

        if b"InstallShield" in header:
            return [installer_path, "/s", "/v/qn"]

    except Exception:
        pass

    return [installer_path, "/S"]


def execute_silent_install(installer_path):
    try:
        st = os.stat(installer_path)
        os.chmod(installer_path, st.st_mode | stat.S_IEXEC)
    except Exception as e:
        print(f"Permission adjustment failed: {e}")

    cmd = get_install_command(installer_path)

    try:
        subprocess.run(cmd, check=True)
        return True
    except subprocess.CalledProcessError:
        return False


def download_file(url, package_name):
    DOWNLOADS_DIR.mkdir(parents=True, exist_ok=True)

    filename = url.split("/")[-1].split("?")[0].split("#")[0]
    filename = re.sub(r'[<>:"/\\|?*]', "_", filename).strip()

    if not filename or filename in (".", ".."):
        filename = f"{package_name}_installer"

    file_path = DOWNLOADS_DIR / filename

    with requests.get(url, stream=True) as req:
        req.raise_for_status()

        total_size = int(req.headers.get('content-length', 0))

        with tqdm(total=total_size, unit="B", unit_scale=True, desc=filename) as prog_bar:
            with open(file_path, "wb") as file:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
                        prog_bar.update(len(chunk))

    return file_path


def install_package(url, package_name):
    try:
        file_path = download_file(url, package_name)
        print(f"{package_name} downloaded.")

        with open(HASHES_FILE, "r") as file:
            hashes = json.load(file)

        expected_hash = hashes.get(package_name)
        if not expected_hash:
            print("No hash found for this package.")
            return False

        if not compare_hashes(file_path, expected_hash):
            print("Hash mismatch. Aborting.")
            return False

        print("Installing...")
        success = execute_silent_install(str(file_path))

        file_path.unlink(missing_ok=True)

        return success

    except Exception as e:
        print(f"Installation failed: {e}")
        return False