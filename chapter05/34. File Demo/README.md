# File Reading in Python

This script demonstrates how to read and print the contents of files in Python. It includes error handling for common issues like missing files and input/output errors.

## Script Overview 📘

The script defines functions to read and print the contents of files. It handles errors gracefully, providing feedback when files are not found or cannot be read. The `main()` function demonstrates these operations with specified file paths.

### :computer: Script Code

```python
def read_file(file_path):
    """
    Reads and prints the content of a file.

    Parameters:
    file_path (str): The path to the file to be read.
    """
    try:
        with open(file_path, 'r') as f:
            print("Filename:", f.name)
            print("Closed:", f.closed)
            print("Opening mode:", f.mode)
            contents = f.read()
            print("Contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")

def read_file_contents(file_path):
    """
    Reads the content of a file and returns it.

    Parameters:
    file_path (str): The path to the file to be read.

    Returns:
    str: The content of the file.
    """
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except IOError as e:
        print(f"Error reading file '{file_path}': {e}")
    return None

def main():
    # Reading and printing details and contents of the first file
    print("Reading 'cf2024.txt':")
    read_file('cf2024.txt')
    print()

    # Reading and printing the contents of the second file
    print("Reading 'C:/tmp/cf5.txt':")
    contents = read_file_contents('C:/tmp/cf5.txt')
    if contents is not None:
        print(contents)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **File Reading**: Learn how to read and print the contents of a file in Python.
- **Error Handling**: Understand how to handle errors such as missing files and input/output errors gracefully.
- **File Details**: See how to print file details like name, mode, and contents.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `34_file_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `34_file_demo.py`.
5. Run the script with: `python 34_file_demo.py`.

## Usage Example 📋
Execute the script to see how file reading works in Python. The script will demonstrate reading and printing the contents of specified files, as well as handling errors gracefully.

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
