"""File Parser Python Script"""


def read_file(path: str):
    """Reads in a file and returns a list of strings per-line.

    :param
        path: [str]: Full path and filename
    :return:
        List[str]: List of the file with each index as a line
    """
    input_file = []
    if isinstance(path, str):
        if not path.startswith('/'):
            path = '/' + path
        with open(path, 'r', encoding="utf-8") as file_obj:
            input_file = file_obj.readlines()
        return input_file
    return


def strip_newlines(file_list):
    """Strips off the last character in each list index. Works
    if last character is a newline \n char.

    :param
        file_list: List[str]: List of strings
    :return:
        List[str]: List of strings stripped of the last character
    """
    stripped_list = []
    for line in file_list:
        stripped_list.append(line.strip())
    return stripped_list


def write_file(file_path: str, file_text):
    """Writes the passed file_text to a file in the file_path

    :param
        [str]: file_path: Full path and filename of the file to be written
    :param
        file_text: List[str]: List of strings to be written to the file
    :return:
        N/A
    """
    write = "w"
    with open(file_path, write, encoding="utf-8") as file_obj:
        for line in file_text:
            file_obj.write(line)
            file_obj.write("\n")


def main() -> None:
    """main"""


if __name__ == "__main__":
    import sys

    sys.exit(main())
