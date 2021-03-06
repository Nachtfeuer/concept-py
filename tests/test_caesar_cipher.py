"""
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
# pylint: disable=R0201
import unittest
from hamcrest import assert_that, equal_to
from concept.crypto.caesar_cipher import encrypt, decrypt


class TestCaesarCipher(unittest.TestCase):

    """ Testing caesar cipher. """

    def test_encrypt_with_one_shift_right(self):
        """ Testing encryption with one shift to the right. """
        cipher = "abcdefghijklmnopqrstuvwxyz "
        plaintext = "no more segrets"
        assert_that("mnzlnqdzrdfqdsr", equal_to(encrypt(plaintext, cipher, 1)))

    def test_decrypt_with_one_shift_right(self):
        """ Testing decryption with one shift to the right. """
        cipher = "abcdefghijklmnopqrstuvwxyz "
        ciphertext = "mnzlnqdzrdfqdsr"
        assert_that("no more segrets", equal_to(decrypt(ciphertext, cipher, 1)))

    def test_encrypt_with_one_shift_left(self):
        """ Testing encryption with one shift to the left. """
        cipher = "abcdefghijklmnopqrstuvwxyz "
        plaintext = "no more segrets"
        assert_that("opanpsfatfhsfut", equal_to(encrypt(plaintext, cipher, -1)))

    def test_decrypt_with_one_shift_left(self):
        """ Testing decryption with one shift to the left. """
        cipher = "abcdefghijklmnopqrstuvwxyz "
        ciphertext = "opanpsfatfhsfut"
        assert_that("no more segrets", equal_to(decrypt(ciphertext, cipher, -1)))
