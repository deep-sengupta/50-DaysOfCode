import os

def rename_files(directory, extension, newname):
    files = os.listdir(directory)
    counter = 0
    for file in files:
        if file.endswith(extension):
            filetype = file.split('.')[-1]
            new_file = os.path.join(directory, f"{newname}_{counter}.{filetype}")
            os.rename(os.path.join(directory, file), new_file)
            print(f"Renaming {file} to {newname}_{counter}.{filetype}")
            counter += 1

directory = input("Enter the directory path: ")
extension = input("Enter the file extension: ")
newname = input("Enter the new name: ")

rename_files(directory, extension, newname)