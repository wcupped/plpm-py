from pathlib import Path

BASE_DIR = Path.home() / "AppData" / "Roaming" / "PacmanLikePackageManager"
DOWNLOADS_DIR = BASE_DIR / "Downloads"

REPO_URL = "https://raw.githubusercontent.com/wcupped/plpm-repo/refs/heads/main/repo.json"
HASHES_URL = "https://raw.githubusercontent.com/wcupped/plpm-repo/refs/heads/main/hashes.json"

REPO_FILE = BASE_DIR / "repo.json"
HASHES_FILE = BASE_DIR / "hashes.json"