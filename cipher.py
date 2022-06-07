"""The Vigenere Cipher class file"""
from collections import deque


class Vigenere:
    def __init__(self):
        # fmt: off
        self.rotor_in = deque([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])
        self.rotor_out = deque([
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        ])
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

    def get_message(self):
        while True:
            message = input("Enter your message to be encoded: ")
            if isinstance(message, str):
                message_x = message.replace(' ', 'x')
                self.message = message_x.upper()
                break
            elif not isinstance(message, str):
                print("\nPlease enter a message form the 26 character North American Alphabet.\n")

    def set_key(self):
        while self.rotor_out[0] != self.key[0]:
            deque.rotate(self.rotor_out)

    def encode_message(self):
        message_index = 0

        while len(self.encoded_message) != len(self.message):
            while self.rotor_out[0] != self.key[0]:
                deque.rotate(self.rotor_out)

            message_letter = self.message[message_index]
            index_of_letter = self.rotor_in.index(message_letter)

            encoded_letter = self.rotor_out[message_letter]
            self.encoded_message += encoded_letter

    def get_encoded_messaage(self):
        return self.encoded_message
