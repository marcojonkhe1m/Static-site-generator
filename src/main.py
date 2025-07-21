import sys
import shutil
import os
from copy_static import copy_static
from generate_page import generate_page_recursive

static_path = "static"
content_path = "content"
destination_path = "docs"
template = "template.html"

def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1] + "/"

    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)

    copy_static(static_path, destination_path)
    
    generate_page_recursive(content_path,template, destination_path, basepath)

if __name__ == "__main__":
    main()
    
