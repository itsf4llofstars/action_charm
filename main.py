#!/usr/bin/env python3
"""main.py file"""
from cipher import Vigenere

vig_encode = Vigenere()
vig_encode.get_key()
vig_encode.set_key()
vig_encode.get_message()
vig_encode.encode_message()

encoded_message = vig_encode.get_encoded_messaage()
print(encoded_message)

vig_decode = Vigenere()
vig_decode.get_key()
vig_decode.set_key()
vig_decode.get_message()
vig_decode.decode_message()

decoded_message = vig_decode.get_encoded_messaage()
print(decoded_message)
