"""File Parser Python Script"""


def read_in_a_file(path: str):
    """Reads in a file and returns a list of it's lines.

    :param
        path: [str]: Full path and filename
    :return:
        List[str]: List of the file with each index as a line
    """
    read = 'r'
    try:
        with open(path, read) as fo:
            input_file = fo.readlines()
    except FileNotFoundError as fnfe:
        print(f'The file: {fnfe} was not found.')
    else:
        return input_file


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
    write = 'w'
    with open(file_path, write) as fo:
        for line in file_text:
            fo.write(line)
            fo.write('\n')


def main() -> None:
    """main"""
    foo = read_in_a_file('/etc/adduser.conf')
    file_text = strip_newlines(foo)
    write_file('/home/bumper/delete-me.txt', file_text)


if __name__ == '__main__':
    import sys
    sys.exit(main())
