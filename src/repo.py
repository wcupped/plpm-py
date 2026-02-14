import json
import requests
from config import BASE_DIR, REPO_FILE, HASHES_FILE, REPO_URL, HASHES_URL
import os

def sync_repo():
    BASE_DIR.mkdir(parents=True, exist_ok=True)

    print("Syncing repository...")
    if REPO_FILE.exists():
        os.remove(REPO_FILE)
    with requests.get(REPO_URL, stream=True) as req:
        req.raise_for_status()
        with open(REPO_FILE, "wb") as file:
            for chunk in req.iter_content(8192):
                if chunk:
                    file.write(chunk)

    print("Syncing hashes...")
    if HASHES_FILE.exists():
        os.remove(HASHES_FILE)
    with requests.get(HASHES_URL, stream=True) as req:
        req.raise_for_status()
        with open(HASHES_FILE, "wb") as file:
            for chunk in req.iter_content(8192):
                if chunk:
                    file.write(chunk)


def load_repo():
    with open(REPO_FILE, "r") as file:
        return json.load(file)