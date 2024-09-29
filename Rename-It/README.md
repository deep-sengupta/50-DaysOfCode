# Rename It
This script renames files in a specified directory that match a given file extension. The user can provide the directory path, file extension, and a new prefix for renaming the files.

## How to Use

1. Run the script in your Python environment.
2. Enter the following inputs when prompted:
   - **Directory Path**: The full path to the directory where the files are located.
   - **File Extension**: The file extension (e.g., `.txt`, `.jpg`) of the files you want to rename.
   - **New Name**: The new prefix to use for renaming the files.
3. Each file will be renamed to `newname_X.extension`, where `X` is an incremental number.

## Example
All `.txt` files in the directory will be renamed to `document_0.txt`, `document_1.txt`, and so on.

## Requirements
- Python 3.x
- Ensure you have the necessary permissions to rename files in the specified directory.