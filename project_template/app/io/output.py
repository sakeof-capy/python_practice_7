def output_to_console(text):
    """
    Function to output text to the console.

    Parameters:
    text (str): The text to be output to the console.

    Returns:
    None.
    """
    print(text)


def write_to_file(filename, text):
    """
    Function to write text to a file using Python's built-in capabilities.

    Parameters:
    filename (str): The path to the file to be written.
    text (str): The text to be written to the file.

    Returns:
    None.
    """
    try:
        with open(filename, 'w') as file:
            file.write(text)
    except Exception as e:
        print("An error occurred while writing to the file:", e)
