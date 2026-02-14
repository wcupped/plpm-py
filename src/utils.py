import hashlib

def compare_hashes(file_path, expected_hash):
    hash_func = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)

    return hash_func.hexdigest() == expected_hash