import os
import argparse
import shutil
from pathlib import Path

# BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_desktop_directory():
    user_profile = Path.home()

    if os.name == 'nt':
        desktop_dir = user_profile / "Desktop"
    else:
        desktop_dir = user_profile / "Desktop"

    return desktop_dir

def main():
    parser = argparse.ArgumentParser(description="Organize files and assign them to specific folders")
    parser.add_argument("prefix", help="Prefix to match (files that start with this this)")
    parser.add_argument("folder", help="Prefix to match (files that start with this this)")

    args = parser.parse_args()

    prefix = args.prefix.strip()
    desktop_dir = get_desktop_directory()
    dest_dir = desktop_dir / args.folder

    os.makedirs(dest_dir, exist_ok=True)

    for filename in sorted(os.listdir(desktop_dir)):
            src_path = desktop_dir / filename

            if not os.path.isfile(src_path):
                continue

            if filename.lower().startswith(prefix.lower()):
                shutil.move(src_path, dest_dir)




if __name__ == "__main__":
    main()