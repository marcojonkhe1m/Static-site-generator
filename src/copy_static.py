import os
import shutil

def copy_static():
    SOURCE_DIR = "static"
    DESTINATION_DIR = "public"

    if len(os.listdir(SOURCE_DIR)) == 0:
           raise ValueError("no files in source directory")
    
    # empty public directory
    if os.path.exists(DESTINATION_DIR):
        print(f"deleting directory: {DESTINATION_DIR}")
        shutil.rmtree(DESTINATION_DIR)
    os.mkdir(DESTINATION_DIR)

    create_filepath_list_to_copy(SOURCE_DIR, DESTINATION_DIR)

def create_filepath_list_to_copy(source, destination):
    dir_content = os.listdir(source)
    for item in dir_content:
        item_path = os.path.join(source, item)
        destination_path = os.path.join(destination, item)
        if os.path.isfile(item_path):
            print(f"copying: {item_path} to --> {destination_path}")
            copy_file(item_path, destination_path)
        else:
            if not os.path.exists(destination_path):
                os.mkdir(destination_path)

            create_filepath_list_to_copy(item_path, destination_path)

def copy_file(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"source path: {source} doesn't exist")
    shutil.copy(source, destination)

