"""
   Vigenere cipher (encryption and decryption).

.. module:: vigenere_cipher
    :platform: Unix, Windows
    :synopis: vigenere cipher (encryption and decryption)

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2015 Thomas Lehmann

   Permission is hereby granted, free of charge, to any person obtaining a copy of this
   software and associated documentation files (the "Software"), to deal in the Software
   without restriction, including without limitation the rights to use, copy, modify, merge,
   publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons
   to whom the Software is furnished to do so, subject to the following conditions:

   The above copyright notice and this permission notice shall be included in all copies
   or substantial portions of the Software.

   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
   INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
   IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
   DAMAGES OR OTHER LIABILITY,
   WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


def encrypt(plaintext, key, cipher):
    """
    Using Vignere cipher to encrypt plaintext.

    :param plaintext: plaintext to encrypt with given key and given cipher
    :param key: the key is appended until it has same length as plaintext;
                each character of the key decides which cipher to use to
                subtitute the plaintext character.
    :param cipher: from the cipher we create a map of shifted ciphers as
                   many characters the cipher contains.
    :returns: encrypted plaintext

    See: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

    >>> encrypt("ATTACKATDAWN", "LEMON", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    'LXFOPVEFRNHR'
    """
    mapping = {cipher[0]: cipher}

    counter = len(cipher)
    shifted_cipher = cipher
    while counter > 0:
        shifted_cipher = shifted_cipher[-1] + shifted_cipher[0:len(shifted_cipher) - 1]
        mapping[shifted_cipher[0]] = shifted_cipher
        counter -= 1

    plaintext_key = ""
    while len(plaintext_key) < len(plaintext):
        for character in key:
            plaintext_key += character
            if len(plaintext_key) == len(plaintext):
                break

    ciphertext = ""
    for pos, character in enumerate(plaintext):
        use_cipher = mapping[plaintext_key[pos]]
        ciphertext += use_cipher[cipher.index(character)]

    return ciphertext


def decrypt(ciphertext, key, cipher):
    """
    Using Vignere cipher to decrypt ciphertext.

    :param ciphertext: encrypted text to decrypt with given key and given cipher
    :param key: the key is appended until it has same length as ciphertext;
                each character of the key decides which cipher to use to
                subtitute the ciphertext character.
    :param cipher: from the cipher we create a map of shifted ciphers as
                   many characters the cipher contains.
    :returns: decrypted ciphertext

    See: https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher

    >>> decrypt("LXFOPVEFRNHR", "LEMON", "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    'ATTACKATDAWN'
    """
    mapping = {cipher[0]: cipher}

    counter = len(cipher)
    shifted_cipher = cipher
    while counter > 0:
        shifted_cipher = shifted_cipher[-1] + shifted_cipher[0:len(shifted_cipher) - 1]
        mapping[shifted_cipher[0]] = shifted_cipher
        counter -= 1

    ciphertext_key = ""
    while len(ciphertext_key) < len(ciphertext):
        for character in key:
            ciphertext_key += character
            if len(ciphertext_key) == len(ciphertext):
                break

    plaintext = ""
    for pos, character in enumerate(ciphertext):
        use_cipher = mapping[ciphertext_key[pos]]
        plaintext += cipher[use_cipher.index(character)]

    return plaintext
