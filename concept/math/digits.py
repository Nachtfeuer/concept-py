"""
   Math function relating digits of a number.

.. module:: functions
    :platform: Unix, Windows
    :synopis: math functions relating digits of a number.

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


def sum_digits(value):
    """
    Sum of digits of given number.

    :param value: integer value (can also be negative)
    :returns: sum of digits of given number

    >>> sum_digits(1024)
    7
    >>> sum_digits(1234567890)
    45
    >>> sum_digits(-1234567890)
    45
    """
    value = abs(value)
    result = 0
    while value > 0:
        result += value % 10
        value //= 10
    return result


def count_digits(value):
    """
    Count of digits of given number.

    :param value: integer value (can also be negative)
    :returns: count of digits of given number

    >>> count_digits(0)
    1
    >>> count_digits(1024)
    4
    >>> count_digits(1234567890)
    10
    >>> count_digits(-1234567890)
    10
    """
    if 0 == value:
        return 1

    value = abs(value)
    result = 0
    while value > 0:
        result += 1
        value //= 10
    return result


def is_pandigital(value):
    """
    Check that each digit appears once only.

    :param value: integer value (can also be negative)
    :retuns: true when given number is pandigital

    see http://en.wikipedia.org/wiki/Pandigital_number

    >>> is_pandigital(1234567890)
    True
    >>> is_pandigital(12345678900)
    False
    >>> is_pandigital(9876543210)
    True
    >>> is_pandigital(10240)
    False
    """
    value = abs(value)
    digits = set()
    counter = 0
    while value > 0:
        digits.add(value % 10)
        counter += 1
        value //= 10
    return counter == len(digits)


def is_palindrome(value):
    """
    Check that given number is a palindrom like: 161, 2332.

    :returns: true when given number is a palindrom
    see http://en.wikipedia.org/wiki/Palindromic_number

    >>> is_palindrome(123454321)
    True
    >>> is_palindrome(1231)
    False
    """
    value = abs(value)
    digits = []
    while value > 0:
        digits.append(value % 10)
        value //= 10

    left = 0
    right = len(digits)-1
    while left < right:
        if not digits[left] == digits[right]:
            return False
        left += 1
        right -= 1
    return True
