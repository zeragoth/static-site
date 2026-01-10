import os
import shutil
import sys

from copy_static import copy_files_recursive
from gencontent import generate_pages_recursive


public_path = "./docs"
static_path = "./static"
content_path = "./content"
template_path = "./template.html"


def main():
    if os.path.exists(static_path):
        basepath = "/"
        if len(sys.argv) > 1:
            basepath = sys.argv[1]
        print(f'Basepath is: "{basepath}"')

        if os.path.exists(public_path):
            print(f"Deleting contents of {public_path}...")
            shutil.rmtree(public_path)

        print("Copying static files...")
        copy_files_recursive(static_path, public_path)
        print("Files copied successfully!")

        print("Generating page...")
        generate_pages_recursive(content_path, template_path, public_path, basepath)


main()
