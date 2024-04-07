from app.io.input import input_from_console, read_from_file, read_from_file_with_pandas
from app.io.output import output_to_console, write_to_file


def main():
    user_input = input_from_console()
    output_to_console("You entered: " + user_input)

    file_path = "data/input.txt"
    write_to_file(file_path, user_input)

    text_from_file = read_from_file(file_path)
    output_to_console("Read from file: " + text_from_file)

    text_from_file_pandas = read_from_file_with_pandas(file_path)
    output_to_console("Read from file with pandas: " + text_from_file_pandas)


if __name__ == '__main__':
    main()

