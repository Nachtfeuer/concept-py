"""
   =======
   License
   =======
   Copyright (c) 2014 Thomas Lehmann

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
from concept.math.matrix import Matrix
from concept.tools.decorator import validate_test_responsibility_for


def create_matrix(width, height, start=1):
    """
    Create a test matrix.

    :param width: number of columns for matrix
    :param height:  number of rows for matrix
    :param start: let value start with given value (default: 1)
    :returns: matrix instance
    """
    matrix = Matrix(width, height)
    value = start
    for row in range(height):
        for column in range(width):
            matrix[column, row] = value
            value += 1
    return matrix


@validate_test_responsibility_for(Matrix)
@validate_test_responsibility_for(Matrix.Cell, True)
@validate_test_responsibility_for(Matrix.Row, True)
@validate_test_responsibility_for(Matrix.Column, True)
@validate_test_responsibility_for(Matrix.Diagonal, True)
class TestMatrix(unittest.TestCase):

    """ Testing of class concept.math.matrix.Matrix. """

    def test_init(self):
        """ Testing of Matrix.__init__, Matrix.width and Matrix.height. """
        matrix = Matrix(2, 3)
        assert_that(len(matrix.data), equal_to(3))
        assert_that(len(matrix.data[0]), equal_to(2))

    def test_len(self):
        """ Testing of Matrix.height method. """
        matrix = Matrix(2, 3)
        assert_that(len(matrix), equal_to(3))

    def test_setitem(self):
        """ Testing of Matrix.__setitem__ method. """
        matrix = create_matrix(2, 2)
        assert_that(matrix.data[0], equal_to([1, 2]))
        assert_that(matrix.data[1], equal_to([3, 4]))

    def test_getitem(self):
        """ Testing of Matrix.__getitem__ method. """
        matrix = create_matrix(2, 2)
        assert_that(matrix[0, 0], equal_to(1))
        assert_that(matrix[1, 0], equal_to(2))
        assert_that(matrix[0, 1], equal_to(3))
        assert_that(matrix[1, 1], equal_to(4))

    def test_delitem(self):
        """ Testing of Matrix.__delitem__ method. """
        matrix = create_matrix(2, 2)

        del matrix[1, 0]
        del matrix[0, 1]
        assert_that(matrix[1, 0], equal_to(0))
        assert_that(matrix[0, 1], equal_to(0))

    def test_create_data(self):
        """ Testing of Matrix.create_data static method """
        assert_that(Matrix.create_data(3, 2), equal_to([[0, 0, 0], [0, 0, 0]]))

    def test_set(self):
        """ Testing of Matrix.set method """
        matrix = create_matrix(2, 2)
        success = matrix.set([99, 88, 77, 66])
        assert_that(success, equal_to(True))
        assert_that([cell.get() for cell in matrix.cells()], [99, 77, 88, 66])
        # more values than matrix has
        success = matrix.set([1, 2, 3, 4, 5])
        assert_that(success, equal_to(False))

    def test_repr(self):
        """ Testing of Matrix.__repr__ method """
        matrix = create_matrix(3, 2)
        expected = "Matrix(3x2:1,4,2,5,3,6)"
        assert_that(str(matrix), equal_to(expected))

    def test_rows(self):
        """ Testing of Matrix.rows method """
        matrix = create_matrix(2, 2)
        for expected, given in zip([[1, 2], [3, 4]], [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

    def test_columns(self):
        """ Testing of Matrix.columns method """
        matrix = create_matrix(2, 2)
        for expected, given in zip([[1, 3], [2, 4]], [row.get() for row in matrix.columns()]):
            self.assertEqual(expected, given)

    def test_diagonals(self):
        """ Testing of Matrix.diagonals method """
        matrix = create_matrix(2, 2)
        for expected, given in zip([[1], [3, 2], [4]],
                                   [diagonal.get() for diagonal in matrix.diagonals()]):
            self.assertEqual(expected, given)

    def test_main_diagonals(self):
        """ Testing of Matrix.main_diagonals method """
        matrix = create_matrix(2, 2)
        for expected, given in zip([[1, 4], [3, 2]],
                                   [diagonal.get() for diagonal in matrix.main_diagonals()]):
            self.assertEqual(expected, given)

    def test_cells(self):
        """ Testing of Matrix.cells method """
        matrix = create_matrix(2, 2)
        values = [cell.get() for cell in matrix.cells()]
        self.assertEqual([1, 3, 2, 4], values)

    def test_clone(self):
        """ Testing of Matrix.clone method """
        matrix_a = create_matrix(2, 2)
        matrix_b = matrix_a.clone()
        self.assertEqual(matrix_a.data, matrix_b.data)

    def test_add(self):
        """ Testing of Matrix.__add__ method. """
        matrix_a = create_matrix(2, 2, start=1)
        matrix_b = create_matrix(2, 2, start=5)

        matrix_c = matrix_a + matrix_b
        for expected, given in zip([[6, 8], [10, 12]], [row.get() for row in matrix_c.rows()]):
            self.assertEqual(expected, given)

        # you cannot say: "matrix + 1234"
        self.assertRaises(TypeError, matrix_a.__add__, 1234)

    def test_flip(self):
        """ Testing of Matrix.flip method """
        # testing with even rows and columns
        matrix = create_matrix(2, 2)
        matrix.flip(True, False)
        for expected, given in zip([[3, 4], [1, 2]], [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

        matrix.flip(False, True)
        for expected, given in zip([[4, 3], [2, 1]], [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

        matrix.flip(True, True)
        for expected, given in zip([[1, 2], [3, 4]], [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

        # testing with odd rows and columns
        matrix = create_matrix(3, 3)
        matrix.flip(True, False)
        expected_data = [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
        for expected, given in zip(expected_data, [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

        matrix.flip(False, True)
        expected_data = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
        for expected, given in zip(expected_data, [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

        matrix.flip(True, True)
        expected_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        for expected, given in zip(expected_data, [row.get() for row in matrix.rows()]):
            self.assertEqual(expected, given)

    def test_cell_init(self):
        """ Testing of Matrix.Cell.__init__ method """
        cell = Matrix.Cell(1, 2, None)
        self.assertEqual(1, cell.column)
        self.assertEqual(2, cell.row)
        self.assertEqual(None, cell.matrix)

    def test_cell_get(self):
        """ Testing of Matrix.Cell.get method """
        matrix = create_matrix(2, 2)
        self.assertEqual(1, list(matrix.cells())[0].get())
        self.assertEqual(3, list(matrix.cells())[1].get())
        self.assertEqual(2, list(matrix.cells())[2].get())
        self.assertEqual(4, list(matrix.cells())[-1].get())

    def test_cell_set(self):
        """ Testing of Matrix.Cell.set method """
        matrix = create_matrix(2, 2)
        cells = [cell for cell in matrix.cells() if cell.row == 0]
        for cell in cells:
            cell.set(cell.get() * 10)

        values = [cell.get() for cell in matrix.cells()]
        self.assertEqual([10, 3, 20, 4], values)

    def test_cell_repr(self):
        """ Testing of Matrix.Cell.__repr__ method """
        matrix = create_matrix(2, 2)
        cell = list(matrix.cells())[0]
        self.assertEqual("cell(0, 0, 1)", str(cell))
        cell = list(matrix.cells())[-1]
        self.assertEqual("cell(1, 1, 4)", str(cell))

    def test_cell_swap(self):
        """ Testing of Matrix.Cell.__repr__ method """
        matrix = create_matrix(2, 2)
        cell_a = list(matrix.cells())[0]
        cell_b = list(matrix.cells())[-1]

        cell_a.swap(cell_b)
        self.assertEqual("cell(0, 0, 4)", str(cell_a))
        self.assertEqual("cell(1, 1, 1)", str(cell_b))
        # wrong type to swap with
        self.assertRaises(TypeError, cell_a.swap, 1234)

    def test_row_init(self):
        """ Testing of Matrix.Row.__init__ method """
        instance = Matrix.Row(1, None)
        self.assertEqual(1, instance.row)
        self.assertEqual(None, instance.matrix)

    def test_row_set(self):
        """ Testing of Matrix.Row.set method """
        matrix = create_matrix(2, 2)
        # last row:
        row = list(matrix.rows())[-1]
        row.set([5, 6])

        values = [cell.get() for cell in matrix.cells()]
        self.assertEqual([1, 5, 2, 6], values)

    def test_row_get(self):
        """ Testing of Matrix.Row.get method """
        matrix = create_matrix(2, 2)
        # first row:
        row = list(matrix.rows())[0]
        self.assertEqual([1, 2], row.get())
        # last row:
        row = list(matrix.rows())[-1]
        self.assertEqual([3, 4], row.get())

    def test_row_swap(self):
        """ Testing of Matrix.Row.swap method """
        matrix = create_matrix(2, 2)
        # first row:
        row_a = list(matrix.rows())[0]
        row_b = list(matrix.rows())[-1]
        row_a.swap(row_b)
        self.assertEqual([3, 4], row_a.get())
        self.assertEqual([1, 2], row_b.get())
        # wrong type to swap with
        self.assertRaises(TypeError, row_a.swap, 1234)

    def test_row_cells(self):
        """ Testing of Matrix.Row.cells method """
        matrix = create_matrix(2, 2)
        row = list(matrix.rows())[-1]
        self.assertEqual([3, 4], [cell.get() for cell in row.cells()])

    def test_column_init(self):
        """ Testing of Matrix.Column.__init__ method """
        instance = Matrix.Column(1, None)
        self.assertEqual(1, instance.column)
        self.assertEqual(None, instance.matrix)

    def test_column_get(self):
        """ Testing of Matrix.Row.get method """
        matrix = create_matrix(2, 2)
        # first row:
        column = list(matrix.columns())[0]
        self.assertEqual([1, 3], column.get())
        # last row:
        column = list(matrix.columns())[-1]
        self.assertEqual([2, 4], column.get())

    def test_column_set(self):
        """ Testing of Matrix.Row.set method """
        matrix = create_matrix(2, 2)
        # last row:
        column = list(matrix.columns())[-1]
        column.set([5, 6])

        values = [cell.get() for cell in matrix.cells()]
        self.assertEqual([1, 3, 5, 6], values)

    def test_column_swap(self):
        """ Testing of Matrix.Column.swap method """
        matrix = create_matrix(2, 2)
        # first row:
        column_a = list(matrix.columns())[0]
        column_b = list(matrix.columns())[-1]
        column_a.swap(column_b)
        self.assertEqual([2, 4], column_a.get())
        self.assertEqual([1, 3], column_b.get())
        # wrong type to swap with
        self.assertRaises(TypeError, column_a.swap, 1234)

    def test_column_cells(self):
        """ Testing of Matrix.Column.cells method """
        matrix = create_matrix(2, 2)
        column = list(matrix.columns())[-1]
        self.assertEqual([2, 4], [cell.get() for cell in column.cells()])

    def test_diagonal_init(self):
        """ Testing of Matrix.Diagonal.__init__ method """
        instance = Matrix.Diagonal(0, 1, 2, 3, None)
        self.assertEqual(0, instance.column)
        self.assertEqual(1, instance.row)
        self.assertEqual(2, instance.step_column)
        self.assertEqual(3, instance.step_row)
        self.assertEqual(None, instance.matrix)

    def test_diagonal_get(self):
        """ Testing of Matrix.Diagonal.get method """
        matrix = create_matrix(2, 2)
        diagonals = list(matrix.diagonals())
        self.assertEqual(3, len(diagonals))
        self.assertEqual([1], diagonals[0].get())
        self.assertEqual([3, 2], diagonals[1].get())
        self.assertEqual([4], diagonals[2].get())

    def test_diagonal_cells(self):
        """ Testing of Matrix.Diagonal.cells method. """
        matrix = create_matrix(2, 2)
        given_values = [cell.get() for diagonal in matrix.diagonals() for cell in diagonal.cells()]
        self.assertEqual([1, 3, 2, 4], given_values)

    def test_diagonal_set(self):
        """ Testing of Matrix.Diagonal.set method. """
        matrix = create_matrix(2, 2)
        # last row:
        diagonal = list(matrix.diagonals())[1]
        diagonal.set([8, 9])

        values = [cell.get() for cell in matrix.cells()]
        self.assertEqual([1, 8, 9, 4], values)

    def test_mul(self):
        """ Testing of Matrix.__mul__ method """
        self.sub_test_mul_factor()
        self.sub_test_mul_matrix_matrix()
        self.sub_test_mul_bad()

    def sub_test_mul_factor(self):
        """ Testing of Matrix.__mul__ method for matrix with a factor """
        matrix_a = create_matrix(2, 2)
        matrix_b = matrix_a * 10
        values = [cell.get() for cell in matrix_b.cells()]
        self.assertEqual([10, 30, 20, 40], values)

    def sub_test_mul_matrix_matrix(self):
        """ Testing of Matrix.__mul__ method of two matrices """
        matrix_a = create_matrix(3, 4)
        matrix_b = create_matrix(2, 3)
        matrix_c = matrix_a * matrix_b
        self.assertEqual(matrix_a.height, matrix_c.height)
        self.assertEqual(matrix_b.width, matrix_c.width)

        expected_rows = [[22, 28], [49, 64], [76, 100], [103, 136]]
        for expected, given in zip(expected_rows, [row.get() for row in matrix_c.rows()]):
            self.assertEqual(expected, given)

    def sub_test_mul_bad(self):
        """ Testing of Matrix.__mul__ method of a matrix with an unsupported object. """
        matrix = create_matrix(2, 2)
        assert_that(matrix * "text", equal_to(None))
