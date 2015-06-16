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
import unittest
from hamcrest import assert_that, equal_to
from concept.crypto.rail_fence_cipher import encrypt, decrypt


class TestRailFenceCipher(unittest.TestCase):

    """ Testing rail fence cipher. """

    def test_encrypt_with_two_rails(self):
        """ Testing encryption with two rails """
        plaintext = "HELLO WORLD"
        assert_that("HLOWRD EL OL", equal_to(encrypt(plaintext, 2)))

    def test_decrypt_with_two_rails(self):
        """ Testing decryption with two rails. """
        ciphertext = "HLOWRD EL OL"
        assert_that("HELLO WORLD", equal_to(decrypt(ciphertext, 2)))

    def test_encrypt_with_three_rails(self):
        """ Testing encryption with three rails """
        plaintext = "NO MORE SEGRETS"
        assert_that("NMEEE OO GT  RSRS", equal_to(encrypt(plaintext, 3)))

    def test_decrypt_with_three_rails(self):
        """ Testing decryption with three rails. """
        ciphertext = "NMEEE OO GT  RSRS"
        assert_that("NO MORE SEGRETS", equal_to(decrypt(ciphertext, 3)))
