import os
import shutil
from copy_static import copy_files_recursive

public_path = "./public"
static_path = "./static"



def main():
    print(f"copying files from {static_path} to {public_path}...")
    if os.path.exists(static_path) and os.path.exists(public_path):
        shutil.rmtree(public_path)

        copy_files_recursive(static_path, public_path)
        print("files copied successfully!")


main()
