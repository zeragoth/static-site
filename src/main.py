import os
import shutil

from copy_static import copy_files_recursive


public_path = "./public"
static_path = "./static"


def main():
    if os.path.exists(static_path) and os.path.exists(public_path):
        print(f"Deleting contents of {public_path}...")
        shutil.rmtree(public_path)

        print("Copying static files...")
        copy_files_recursive(static_path, public_path)
        print("Files copied successfully!")


main()
