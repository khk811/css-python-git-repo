import string
from string import ascii_uppercase as up_case
from string import ascii_lowercase as lo_case


def caesar(s, k, decode = False):
    if decode:
        k = 26 - k
    return s.translate(
        str.maketrans(
            up_case + lo_case,
            up_case[k:] + up_case[:k] +
            lo_case[k:] + lo_case[:k]
            )
        )

while True:
    encrypt_key = int(input("Decide secret number: "))
    msg = input("give me the some words to encrypt: ")
    print("encrypted message: ", caesar(msg, encrypt_key))
    print("decrypted message: ", caesar(caesar(msg, encrypt_key), encrypt_key, False))
    exit = input("press any key to continue or 'q' to quit: ")
    if exit == 'q' or exit == 'Q':
        break
