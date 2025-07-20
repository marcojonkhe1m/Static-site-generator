import shutil
import os
from copy_static import copy_static
from generate_page import generate_page_recursive

source_path = "static"
destination_path = "public"

def main():
    if os.path.exists(destination_path):
        shutil.rmtree(destination_path)
    os.mkdir(destination_path)

    copy_static(source_path, destination_path)
    
    generate_page_recursive("content","template.html", "public")

    

if __name__ == "__main__":
    main()
    
