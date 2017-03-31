"""
   Caesar cipher (encryption and decryption).

.. module:: caesar_cipher
    :platform: Unix, Windows
    :synopis: caesar cipher (encryption and decryption)

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


def encrypt(plaintext, cipher, shift):
    """
    Caesar encryption of a plaintext using a shifted cipher.

    You can specify a positiv shift to rotate the cipher to the right
    and using a negative shift to rotate the cipher to the left.

    :param plaintext: the text to encrypt.
    :param cipher: set of characters, shifted in a directed to used for character substitution.
    :param shift: offset to rotate cipher.
    :returns: encrypted plaintext (ciphertext).

    See: https://en.wikipedia.org/wiki/Caesar_cipher
    Example:

    >>> encrypt("hello world", "abcdefghijklmnopqrstuvwxyz ", 1)
    'gdkknzvnqkc'
    >>> encrypt("hello world", "abcdefghijklmnopqrstuvwxyz ", -1)
    'ifmmpaxpsme'
    """
    # calculating shifted cipher
    shifted_cipher = cipher
    if shift > 0:
        while shift > 0:
            shifted_cipher = shifted_cipher[-1] + shifted_cipher[0:len(shifted_cipher) - 1]
            shift -= 1
    else:
        while shift < 0:
            shifted_cipher = shifted_cipher[1:] + shifted_cipher[0]
            shift += 1

    return "".join([shifted_cipher[cipher.index(character)] for character in plaintext])


def decrypt(ciphertext, cipher, shift):
    """
    Caesar decryption of a ciphertext using a shifted cipher.

    :param ciphertext: the encrypted plaintext to decrypt.
    :param cipher: set of characters, shifted in a directed to used for character substitution.
    :param shift: offset to rotate cipher.
    :returns: decrypted cyphertext (plaintext).

    See: https://en.wikipedia.org/wiki/Caesar_cipher
    Example:

    >>> decrypt("gdkknzvnqkc", "abcdefghijklmnopqrstuvwxyz ", 1)
    'hello world'
    >>> decrypt("ifmmpaxpsme", "abcdefghijklmnopqrstuvwxyz ", -1)
    'hello world'
    """
    # calculating shifted cipher
    shifted_cipher = cipher
    if shift > 0:
        while shift > 0:
            shifted_cipher = shifted_cipher[-1] + shifted_cipher[0:len(shifted_cipher) - 1]
            shift -= 1
    else:
        while shift < 0:
            shifted_cipher = shifted_cipher[1:] + shifted_cipher[0]
            shift += 1

    return "".join([cipher[shifted_cipher.index(character)] for character in ciphertext])
