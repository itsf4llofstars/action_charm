"""The Vigenere Cipher class file"""
from collections import deque


class Vigenere:
    def __init__(self, key='', message='', encoded_message='', decoded_message='') -> None:
        """Instantiates Vigenere attributes

        :param key: encoding key, default ""
        :param message: message to encode default ""
        :param encoded_message: message encoded default ""
        :param decoded_message: message decoded default ""
        """
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
        self.key = key.upper()
        self.key_list = deque([])
        self.message = message.upper()
        self.encoded_message = encoded_message.upper()
        self.decoded_message = decoded_message.upper()

    def get_key(self) -> None:
        while True:
            print("Enter a word to be used as the coding key: ", end="")
            key = input()
            if isinstance(key, str) and len(key) <= len(self.rotor_in):
                self.key = key.upper()
                break
            else:
                if not isinstance(key, str):
                    print("\nPlease enter a word or letters form the 26 character North American Alphabet.\n")
                elif len(key) > len(self.rotor_in):
                    print("\nPlease keep your key to less than 26 characters.\n")

    def get_message(self) -> None:
        while True:
            message = input("Enter your message to be encoded: ")
            if isinstance(message, str):
                message_x = message.replace(' ', 'x')
                self.message = message_x.upper()
                break
            elif not isinstance(message, str):
                print("\nPlease enter a message form the 26 character North American Alphabet.\n")

    def set_key(self) -> None:
        self.key_list = deque(self.key)

    def encode_message(self) -> None:
        message_index = 0

        while len(self.encoded_message) != len(self.message):
            while self.rotor_out[0] != self.key_list[0]:
                deque.rotate(self.rotor_out, -1)

            deque.rotate(self.key_list, -1)

            message_letter = self.message[message_index]
            index_of_letter = self.rotor_in.index(message_letter)

            encoded_letter = self.rotor_out[index_of_letter]
            self.encoded_message += encoded_letter

            message_index += 1

    def decode_message(self) -> None:
        message_index = 0

        while len(self.encoded_message) != len(self.message):
            while self.rotor_out[0] != self.key_list[0]:
                deque.rotate(self.rotor_out, -1)

            deque.rotate(self.key_list, -1)

            message_letter = self.message[message_index]
            index_of_letter = self.rotor_out.index(message_letter)

            encoded_letter = self.rotor_in[index_of_letter]
            self.encoded_message += encoded_letter

            message_index += 1

    def get_encoded_messaage(self) -> str:
        return self.encoded_message


def main():
    vig = Vigenere()
    vig.get_key()
    vig.set_key()
    vig.get_message()
    vig.encode_message()
    print(vig.get_encoded_messaage())

    foo = Vigenere()
    foo.get_key()
    foo.get_message()
    foo.set_key()
    foo.decode_message()
    print(foo.get_encoded_messaage())


if __name__ == '__main__':
    main()
