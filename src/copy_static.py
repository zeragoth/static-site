import os
import shutil


def copy_files_recursive(src, dst):
    if not os.path.exists(dst):
        os.mkdir(dst)

    if os.path.exists(src):
        for entry in os.listdir(src):
            entry_path = os.path.join(src, entry)
            dst_path = os.path.join(dst, entry)
            if os.path.isfile(entry_path):
                shutil.copy(entry_path, dst_path)
            else:
                copy_files_recursive(entry_path, dst_path)
    else:
        raise FileExistsError(f"{src} does not exist")
