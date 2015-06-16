"""
   Rail fence cipher (encryption and decryption).

.. module:: rail_fence_cipher
    :platform: Unix, Windows
    :synopis: rail fencer cipher (encryption and decryption)

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


def encrypt(plaintext, rails):
    """
    Rail fence cipher. Encrypts plaintext by given number of rails.

    :param plaintext: plaintext to encrypt.
    :param rails: number of rails to use to encrypt.
    :returns: encrypted plaintext (ciphertext).

    See https://en.wikipedia.org/wiki/Rail_fence_cipher
    Example:

    >>> encrypt("DANGEROUS", 2)
    'DNEOS AGRU'
    >>> encrypt("DANGEROUS", 3)
    'DGO AEU NRS'
    """
    data = [""] * rails
    for index, character in enumerate(plaintext):
        data[index % rails] += character

    return " ".join(data)


def decrypt(ciphertext, rails):
    """
    Rail fence cipher. Decrypts plaintext by given number of rails.

    :param ciphertext: encrypted plaintext.
    :param rails: number of rails being used to encrypt the plaintext.
    :returns: decrypted text (plaintext).

    See https://en.wikipedia.org/wiki/Rail_fence_cipher
    Example:

    >>> decrypt("DNEOS AGRU", 2)
    'DANGEROUS'
    >>> decrypt("DGO AEU NRS", 3)
    'DANGEROUS'
    """
    xrails = len(ciphertext) // rails + 1
    data = [""] * xrails
    for index, character in enumerate(ciphertext):
        data[index % xrails] += character

    return "".join(data[0:-1])
