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
