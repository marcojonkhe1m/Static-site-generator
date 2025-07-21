import os
from markdown_blocks import markdown_to_html_node

def generate_page_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    filepaths = os.listdir(dir_path_content)
    for filepath in filepaths:
        new_content_path = os.path.join(dir_path_content, filepath)
        new_dest_path = os.path.join(dest_dir_path, filepath)
        if not os.path.isfile(new_content_path):
            if not os.path.exists(new_dest_path):
                os.mkdir(new_dest_path)
            generate_page_recursive(
                    new_content_path, template_path, new_dest_path, basepath
                    )
        if new_content_path.endswith(".md"):
            new_dest_path = new_dest_path.replace(".md", ".html")
            generate_page(
                    new_content_path, template_path, new_dest_path, basepath
                    )


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"{from_path} to {dest_path} using {template_path}")

    with open(from_path, 'r') as f:
        markdown = f.read()

    with open(template_path, 'r') as f:
        template = f.read()
    
    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()

    title = extract_title(markdown)

    static_site = template.replace("{{ Title }}", title).replace("{{ Content }}", html_string)
    static_site = static_site.replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    directories = dest_path.split("/")
    path = ""
    for i in range(0, len(directories) - 1):
        path += f"{directories[i]}/"
        if not os.path.exists(path):
            os.mkdir(path)

    with open(dest_path, 'w') as f:
        f.write(static_site)


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("No header found in markdown text")
