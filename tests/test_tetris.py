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
import mock
from hamcrest import assert_that, equal_to, greater_than_or_equal_to, less_than_or_equal_to
from concept.game.tetris import Tetris
from concept.game.raster import Raster


class TestTetris(unittest.TestCase):
    """Testing Tetris class."""

    def test_init(self):
        """Testing construction."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape

            tetris = Tetris(6, 10)
            assert_that(tetris.raster.width, equal_to(6))
            assert_that(tetris.raster.height, equal_to(10))
            assert_that(tetris.shape.width, equal_to(shape.width))
            assert_that(tetris.shape.height, equal_to(shape.height))
            margin = (tetris.raster.width - shape.width) // 2
            assert_that(tetris.current_column, equal_to(margin))
            assert_that(tetris.current_row, equal_to(0))
            assert_that(tetris.can_step(), equal_to(True))
            assert_that(tetris.is_collision(0), equal_to(False))

    def test_step_simple(self):
        """Verify simple step mechanism."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape

            counter = 0
            tetris = Tetris(6, 10)
            while tetris.can_step():
                tetris.step()
                counter += 1

            assert_that(counter, equal_to(tetris.raster.height - 1))

    def test_run_simple(self):
        """Running a simple game until game over."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape

            counter = 0
            tetris = Tetris(6, 10)
            expected = sum(range(tetris.raster.height + 1)) - 1
            while tetris.step():
                counter += 1

            assert_that(counter, equal_to(expected))

    def test_turn_left(self):
        """Testing method Tetris.turn_left."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[1])
            mocked_method.return_value = shape
            tetris = Tetris(6, 10)
            tetris.turn_left()
            expected = Raster.create_from(["*   ", "*   ", "*   ", "****"])
            assert_that(tetris.shape, equal_to(expected))

    def test_turn_right(self):
        """Testing method Tetris.turn_right."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[1])
            mocked_method.return_value = shape
            tetris = Tetris(6, 10)
            tetris.turn_right()
            expected = Raster.create_from(["****", "   *", "   *", "   *"])
            assert_that(tetris.shape, equal_to(expected))

    def test_run_simple_turned_left(self):
        """
        Running a simple game until game over.

        Here the first shape is turned to the left.
        """
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape

            counter = 0
            tetris = Tetris(6, 10)
            tetris.turn_left()
            expected = 7 + 6 + 5 + 4 + 3 + 2
            while tetris.step():
                counter += 1

            assert_that(counter, equal_to(expected))

    def test_move_left_simple(self):
        """Testing Tetris.move_left method."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape
            tetris = Tetris(6, 10)
            margin = (tetris.raster.width - shape.width) // 2
            assert_that(tetris.current_column, equal_to(margin))
            tetris.move_left()
            assert_that(tetris.current_column, equal_to(margin-1))
            for _ in range(10):
                tetris.move_left()
                assert_that(tetris.current_column, greater_than_or_equal_to(0))

    def test_move_right_simple(self):
        """Testing Tetris.move_left method."""
        with mock.patch.object(Tetris, "get_next_shape") as mocked_method:
            shape = Raster.create_from(Tetris.SHAPES[0])
            mocked_method.return_value = shape
            tetris = Tetris(6, 10)
            margin = (tetris.raster.width - shape.width) // 2
            assert_that(tetris.current_column, equal_to(margin))
            tetris.move_right()
            assert_that(tetris.current_column, equal_to(margin+1))
            expected = tetris.raster.width - tetris.shape.width
            for _ in range(10):
                tetris.move_right()
                assert_that(tetris.current_column,less_than_or_equal_to(expected))
