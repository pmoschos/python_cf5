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
    print("Reading 'cf2023.txt':")
    read_file('cf2024.txt')
    print()

    # Reading and printing the contents of the second file
    print("Reading 'C:/tmp/cf5.txt':")
    contents = read_file_contents('C:/tmp/cf5.txt')
    if contents is not None:
        print(contents)

if __name__ == "__main__":
    main()
