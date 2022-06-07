"""The Vigenere Cipher class file"""
from collections import deque


class Vigenere:
    def __init__(self):
        # fmt: off
        self.rotor_in = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.rotor_in = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        # fmt: on
        self.key = ''
        self.message = ''
        self.encoded_message = ''

    def get_key(self):
        while True:
            key = input("Enter a word to be used as the coding key: ")
            if isinstance(key, str) and len(key) <= len(self.rotor_in):
                self.key = key.upper()
                break
            else:
                if not isinstance(key, str):
                    print("\nPlease enter a word or letters form the 26 character North American Alphabet.\n")
                elif len(key) > len(self.rotor_in):
                    print("\nPlease keep your key to less than 26 characters.\n")
