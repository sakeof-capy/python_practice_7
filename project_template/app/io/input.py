import pandas as pd


def input_from_console():
    """
    Function to retrieve input text from the console.

    Parameters:
    None.

    Returns:
    str: The text entered by the user.
    """
    return input("Enter text from the console: ")


def read_from_file(filename):
    """
    Function to read text from a file using Python's built-in capabilities.

    Parameters:
    filename (str): The path to the file to be read.

    Returns:
    str or None: The text from the file or None if the file was not found.
    """
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print("File not found:", filename)
        return None


def read_from_file_with_pandas(filename):
    """
    Function to read text from a file using the pandas library.

    Parameters:
    filename (str): The path to the file to be read.

    Returns:
    str or None: The text from the file or None if the file was not found or an error occurred while reading.
    """
    try:
        df = pd.read_csv(filename, header=None)
        return df.to_string(index=False, header=False)
    except FileNotFoundError:
        print("File not found:", filename)
        return None
    except Exception as e:
        print("An error occurred while reading the file:", e)
        return None
