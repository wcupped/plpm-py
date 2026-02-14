import argparse
from repo import load_repo, sync_repo
from installer import install_package
from elevation import *

def run():
    parser = argparse.ArgumentParser(prog="plpm")
    parser.add_argument("-S", metavar="package", help="Install package")
    parser.add_argument("-F", metavar="package", help="Find package")
    parser.add_argument("-Sr", action="store_true", help="Sync repository")

    args = parser.parse_args()

    if args.S:
        if not is_admin():
            print("This action requires elevation. Restarting with administrator rights...")
            relaunch_as_admin()

        repo = load_repo()
        if args.S in repo:
            print(f"Found {args.S}, installing...")
            if install_package(repo[args.S], args.S):
                print("Installed successfully.")
            else:
                print("Installation failed.")
        else:
            print("Package not found.")

    elif args.F:
        repo = load_repo()
        if args.F in repo:
            print(f"{args.F}: {repo[args.F]}")
        else:
            print("Package not found.")

    elif args.Sr:
        sync_repo()

    else:
        parser.print_help()
