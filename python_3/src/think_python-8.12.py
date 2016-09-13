#!env python
"""Exercise 8.12.

ROT13 is a weak form of encryption that involves “rotating” each letter in a word by 13 places. To rotate a letter means to shift it through the alphabet, wrapping around to the beginning if necessary, so ’A’ shifted by 3 is ’D’ and ’Z’ shifted by 1 is ’A’.

Write a function called rotate_word that takes a string and an integer as parameters, and that returns a new string that contains the letters from the original string “rotated” by the given amount.

For example, “cheer” rotated by 7 is “jolly” and “melon” rotated by -10 is “cubed”.

You might want to use the built-in functions ord, which converts a character to a numeric code,
and chr, which converts numeric codes to characters.

Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily offended, find and decode some of them. Solution: http: // thinkpython. com/ code/ rotate. py.
"""

from sys import argv

## Write a function called rotate_word
##   that takes a string and an integer as parameters, and
##   returns a new string that contains the letters from the original string “rotated” by the given amount.

def rotate_word(s, i):
    plain_text = s.lower()
    # cipher_text = [0] * len(plain_text)
    cipher_text = []

    for c in plain_text:
        shift = int(i)

        if (( ord(c) + shift ) > ord('z')) :  # if beyond 'z'
            shift = shift - 26  # cheap alphabet wrap
        elif (( ord(c) + shift ) < ord('a')) :  # if before 'a'
            shift = shift + 26  # cheap alphabet wrap
        cipher_text.append(chr(ord(c) + shift))
    return ''.join(cipher_text)


print rotate_word(argv[1], int(argv[2]))
