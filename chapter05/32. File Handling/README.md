# File Operations in Python

This script demonstrates basic file operations in Python, including reading from a file, writing to a file, and deleting a file. It handles errors gracefully and provides useful feedback to the user.

## Script Overview 📘

The script defines functions to read from, write to, and delete a file. It uses Python's built-in file handling capabilities and the `pathlib` and `os` modules for file operations. The `main()` function demonstrates these operations with a specified file path.

### :computer: Script Code

```python
import sys
from pathlib import Path
import os

def read_from_file(path):
    """
    Reads the contents of a file.
    
    Parameters:
    path (Path or str): The path to the file to be read.
    
    Returns:
    str: The contents of the file, or None if an error occurs.
    """
    try:
        with open(path, 'r') as f:
            contents = f.read()
        return contents
    except OSError as e:
        print(f"Error reading from file {path}: {e}", file=sys.stderr)
        return None

def write_to_file(path, text):
    """
    Writes text to a file.
    
    Parameters:
    path (Path or str): The path to the file to be written to.
    text (str): The text to write to the file.
    """
    try:
        with open(path, 'a') as f:
            f.write(text)
    except OSError as e:
        print(f"Error: could not write to file {path}: {e}", file=sys.stderr)

def delete_file(path):
    """
    Deletes a file.
    
    Parameters:
    path (Path or str): The path to the file to be deleted.
    """
    try:
        os.remove(path)
        print(f"File {path} deleted!")
    except OSError as e:
        print(f"Error: could not delete file {path}: {e}", file=sys.stderr)

def main():
    """
    Main function to demonstrate reading from, writing to, and deleting a file.
    """
    path = Path('C:/tmp/cf4.txt')

    # Read from the file
    print("Reading from the file:")
    contents = read_from_file(path)
    if contents:
        print(contents)
    
    # Write to the file
    print("\nWriting to the file:")
    write_to_file(path, "I love Python!\n")

    # Read from the file again to see the changes
    print("\nReading from the file after writing:")
    contents = read_from_file(path)
    if contents:
        print(contents)
    
    # Delete the file
    print("\nDeleting the file:")
    delete_file(path)
    
    # Try to read from the file after deletion
    print("\nReading from the file after deletion:")
    contents = read_from_file(path)
    if contents:
        print(contents)
    else:
        print("File does not exist.")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Reading Files**: Learn how to read the contents of a file in Python.
- **Writing Files**: Understand how to append text to a file.
- **Deleting Files**: See how to delete a file and handle potential errors.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities (pathlib and os modules)

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `32_file_handling.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `32_file_handling.py`.
5. Run the script with: `python 32_file_handling.py`.

## Usage Example 📋
Execute the script to see how basic file operations work in Python. The script will demonstrate reading from, writing to, and deleting a file, as well as handling errors gracefully.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
