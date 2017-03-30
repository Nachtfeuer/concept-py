"""
   =======
   License
   =======
   Copyright (c) 2017 Thomas Lehmann

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
from concept.game.raster import Raster


class TestRaster(unittest.TestCase):
    """ Testing game raster. """

    def test_init(self):
        """Testing raster intialization."""
        raster = Raster(3, 2)
        assert_that(len(raster.rows), equal_to(2))
        assert_that(all(len(row) == 3 for row in raster.rows), equal_to(True))
        assert_that(all(raster.rows[row][column] is None
                        for row in range(2) for column in range(3)), equal_to(True))

    def test_set_top_left(self):
        """Testing Raster.set method."""
        raster = Raster(3, 2)
        raster.set(0, 0, "hello")
        assert_that(raster.rows[0][0], equal_to("hello"))
        assert_that(all(raster.rows[row][column] is None
                        for row in range(2) for column in range(3)
                        if not row == 0 and not column == 0), equal_to(True))

    def test_set_top_right(self):
        """Testing Raster.set method."""
        raster = Raster(3, 2)
        raster.set(2, 0, "hello")
        assert_that(raster.rows[0][2], equal_to("hello"))
        assert_that(all(raster.rows[row][column] is None
                        for row in range(2) for column in range(3)
                        if not row == 0 and not column == 2), equal_to(True))

    def test_set_bottom_right(self):
        """Testing Raster.set method."""
        raster = Raster(3, 2)
        raster.set(2, 1, "hello")
        assert_that(raster.rows[1][2], equal_to("hello"))
        assert_that(all(raster.rows[row][column] is None
                        for row in range(2) for column in range(3)
                        if not row == 1 and not column == 2), equal_to(True))

    def test_get(self):
        """Testing Raster.get method."""
        raster = Raster(3, 2)
        raster.set(2, 1, "hello")
        assert_that(raster.get(2, 1), equal_to("hello"))
        assert_that(raster.get(10, 10), equal_to(None))

    def test_turned_left(self):
        """Testing Raster.turned_left method."""
        # 1.2 => 2.3
        # 4.3 => 1.4
        raster = Raster(3, 2)
        raster.set(0, 0, 1)
        raster.set(2, 0, 2)
        raster.set(2, 1, 3)
        raster.set(0, 1, 4)
        turned_raster = raster.turned_left()
        assert_that(turned_raster.get(0, 0), equal_to(2))
        assert_that(turned_raster.get(1, 0), equal_to(3))
        assert_that(turned_raster.get(1, 2), equal_to(4))
        assert_that(turned_raster.get(0, 2), equal_to(1))

    def test_turned_right(self):
        """Testing Raster.turned_right method."""
        # 1.2 => 4.1
        # 4.3 => 3.2
        raster = Raster(3, 2)
        raster.set(0, 0, 1)
        raster.set(2, 0, 2)
        raster.set(2, 1, 3)
        raster.set(0, 1, 4)
        turned_raster = raster.turned_right()
        assert_that(turned_raster.get(0, 0), equal_to(4))
        assert_that(turned_raster.get(1, 0), equal_to(1))
        assert_that(turned_raster.get(1, 2), equal_to(2))
        assert_that(turned_raster.get(0, 2), equal_to(3))

    def test_create_from(self):
        """Testing Raster.create_from function."""
        raster = Raster.create_from([[1, 2, 3], [4, 5, 6]])
        assert_that(raster.width, equal_to(3))
        assert_that(raster.height, equal_to(2))
        assert_that(raster.get(0, 0), equal_to(1))
        assert_that(raster.get(1, 0), equal_to(2))
        assert_that(raster.get(2, 0), equal_to(3))
        assert_that(raster.get(0, 1), equal_to(4))
        assert_that(raster.get(1, 1), equal_to(5))
        assert_that(raster.get(2, 1), equal_to(6))
        # negative test
        assert_that(Raster.create_from(1234), equal_to(None))
        assert_that(Raster.create_from([]), equal_to(None))
        assert_that(Raster.create_from([[1, 2], [3, 4, 5]]), equal_to(None))

    def test_occupied_cells(self):
        """Testing Raster.occupied_cells."""
        raster = Raster(3, 2)
        raster.set(0, 0, 1)
        raster.set(2, 0, 2)
        raster.set(2, 1, 3)
        raster.set(0, 1, 4)

        occupied_cells = list(raster.occupied_cells())
        assert_that(occupied_cells[0], equal_to((0, 0, 1)))
        assert_that(occupied_cells[1], equal_to((2, 0, 2)))
        assert_that(occupied_cells[2], equal_to((0, 1, 4)))
        assert_that(occupied_cells[3], equal_to((2, 1, 3)))
