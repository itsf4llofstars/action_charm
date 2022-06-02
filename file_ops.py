"""File Parser Python Script"""


def read_in_a_file(path: str):
    read = 'r'
    try:
        with open(path, read) as fo:
            input_file = fo.readlines()
    except FileNotFoundError as fnfe:
        print(f'The file: {fnfe} was not found.')
    else:
        return input_file


def main() -> None:
    """main"""
    file_text = read_in_a_file('/etc/bash.bashrc')
    [print(line) for line in file_text]


if __name__ == '__main__':
    import sys
    sys.exit(main())
