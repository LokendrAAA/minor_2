# File: data_loader.py

import os

def load_cpp_files_from_folder(folder_path):
    """
    Loads all C++ code files from a specified folder.
    
    Args:
    folder_path (str): Path to the folder containing .cpp files.
    
    Returns:
    List of dictionaries containing 'id', 'language', and 'code'.
    """
    cpp_files = []
    file_id = 1  # ID counter for the files

    # Iterate over files in the specified folder
    for filename in os.listdir(folder_path):
        if filename.endswith(".cpp"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:
                code = file.read()
                cpp_files.append({
                    "id": file_id,
                    "language": "C++",
                    "code": code
                })
                file_id += 1

    return cpp_files

# Usage example:
folder_path = r"D:\phy 1\Project_CodeNet_C++1000.tar\Project_CodeNet_C++1000\p00004"
cpp_files = load_cpp_files_from_folder(folder_path)
