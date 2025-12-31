import os
import argparse
import shutil

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    parser = argparse.ArgumentParser(description="Organize files and assign them to specific folders")
    parser.add_argument("prefix", help="Prefix to match (files that start with this this)")
    parser.add_argument("folder", help="Prefix to match (files that start with this this)")

    args = parser.parse_args()

    prefix = args.prefix.strip()
    dest_dir = os.path.join(BASE_DIR, args.folder)

    os.makedirs(dest_dir, exist_ok=True)

    for filename in sorted(os.listdir(BASE_DIR)):
            src_path = os.path.join(BASE_DIR, filename)

            if not os.path.isfile(src_path):
                continue

            if filename.lower().startswith(prefix.lower()):
                shutil.move(src_path, dest_dir)




if __name__ == "__main__":
    main()