import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in (lines):
        if line.startswith("# "):
            return line.lstrip("#").strip()
    raise ValueError("No valid header found")


def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path)
    md_content = from_file.read()
    from_file.close()

    template_file = open(template_path)
    template = template_file.read()
    template_file.close
    
    node = markdown_to_html_node(md_content)
    html = node.to_html()

    title = extract_title(md_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace('href="/', f'href="{basepath}')
    template = template.replace('src="/', f'src="{basepath}')

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath="/"):
    if os.path.exists(dir_path_content):
        for entry in os.listdir(dir_path_content):
            entry_path = os.path.join(dir_path_content, entry)
            dst_path = os.path.join(dest_dir_path, entry)
            if os.path.isfile(entry_path):
                # replaces the suffix (.md) with a new one (.html)
                dst_path = Path(dst_path).with_suffix(".html")
                generate_page(entry_path, template_path, dst_path, basepath)
            else:
                generate_pages_recursive(entry_path, template_path, dst_path, basepath)
    else:
        raise FileExistsError(f"{dir_path_content} does not exist")
