"""
Representation of a  mathematical matrix.

.. module:: matrix
    :platform: Unix, Windows
    :synopis: representation of a mathematical matrix

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

   =======
   License
   =======
   Copyright (c) 2013 Thomas Lehmann

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


class Matrix(object):

    """ Matrix of dimensions w x h. """

    class Cell(object):

        """ represent one cell of the matrix. """

        def __init__(self, column, row, matrix):
            """ initializing cell location. """
            self.column = column
            self.row = row
            self.matrix = matrix

        def __repr__(self):
            """ string representation if cell instance. """
            return "cell(%d, %d, %s)" % (self.column, self.row, self.get())

        def get(self):
            """ retrieving value of the cell. """
            return self.matrix[self.column, self.row]

        def set(self, value):
            """ changing value of the cell. """
            self.matrix[self.column, self.row] = value

        def swap(self, other):
            """
            Swap content with another cell.

            :param other: another cell
            """
            if not isinstance(other, self.__class__):
                raise TypeError("instance of type Cell expected, %s given" % type(other))

            value = other.get()
            other.set(self.get())
            self.set(value)

    class Row(object):

        """ represent one row of the matrix. """

        def __init__(self, row, matrix):
            """ initializing row location. """
            self.row = row
            self.matrix = matrix

        def get(self):
            """ :return: copy of the values of the row. """
            return self.matrix.data[self.row][0:]

        def set(self, values):
            """ changing values of the row. """
            for column in range(self.matrix.width):
                self.matrix.data[self.row][column] = values[column]

        def swap(self, other):
            """
            Swap values between this row and the other.

            :param other: another row
            """
            if not isinstance(other, self.__class__):
                raise TypeError("instance of type Row expected, %s given" % type(other))

            values = other.get()
            other.set(self.get())
            self.set(values)

        def cells(self):
            """
            Iterating over each cell of the row of the matrix.

            :return: cell (by cell)
            """
            for column in range(self.matrix.width):
                yield self.matrix.Cell(column, self.row, self.matrix)

    class Column(object):

        """ represent one column of the matrix. """

        def __init__(self, column, matrix):
            """ initializing row location. """
            self.column = column
            self.matrix = matrix

        def get(self):
            """ :return: copy of the values of the column. """
            return [row[self.column] for row in self.matrix.data]

        def set(self, values):
            """ changing values of the column. """
            for row in range(self.matrix.height):
                self.matrix.data[row][self.column] = values[row]

        def swap(self, other):
            """
            Swap values between this column and the other.

            :param other: another column
            """
            if not isinstance(other, self.__class__):
                raise TypeError("instance of type Row expected, %s given" % type(other))

            values = other.get()
            other.set(self.get())
            self.set(values)

        def cells(self):
            """
            Iterating over each cell of the column of the matrix.

            :rtype: cell (by cell)
            """
            for row in range(self.matrix.height):
                yield self.matrix.Cell(self.column, row, self.matrix)

    class Diagonal(object):

        """ represent one diagonal of the matrix. """

        def __init__(self, column, row, step_column, step_row, matrix):
            """ initializing row location. """
            self.row = row
            self.column = column
            self.step_column = step_column
            self.step_row = step_row
            self.matrix = matrix

        def get(self):
            """ :return: copy of the values of the diagonal. """
            data = []
            row = self.row
            column = self.column
            while 0 <= row < self.matrix.height and \
                    0 <= column < self.matrix.width:
                data.append(self.matrix.data[row][column])
                row += self.step_row
                column += self.step_column
            return data

        def set(self, values):
            """ changing values of the diagonal. """
            index = 0
            row = self.row
            column = self.column
            while 0 <= row < self.matrix.height and \
                    0 <= column < self.matrix.width:
                self.matrix.data[row][column] = values[index]
                row += self.step_row
                column += self.step_column
                index += 1

        def cells(self):
            """
            Iterating over each cell of the diagonal of the matrix.

            :return: cell (by cell)
            """
            row = self.row
            column = self.column
            while 0 <= row < self.matrix.height and \
                    0 <= column < self.matrix.width:
                yield self.matrix.Cell(column, row, self.matrix)
                row += self.step_row
                column += self.step_column

    def __init__(self, width, height):
        """
        Initializing a matrix for given width and height.

        :param: width: width of matrix
        :param: height: height of matrix
        """
        self.width = width
        self.height = height
        self.data = self.create_data(width, height)

    @staticmethod
    def create_data(width, height):
        """
        Create a two dimensional matrix initialized with zeroes.

        :param: width: width of matrix
        :param: height: height of matrix
        :rtype: two dimensional matrix
        """
        data = []
        for dummy in range(height):
            data.append([0] * width)
        return data

    def __len__(self):
        """ :return: same as height method. """
        return len(self.data)

    def __setitem__(self, key, value):
        """
        Change a value of a "cell".

        :param key: (column, row) pair
        :param value: new value for cell
        """
        column, row = key
        self.data[row][column] = value

    def __getitem__(self, key):
        """
        Retrieving value of a "cell".

        :param key: (column, row) pair
        :return: value of the cell
        """
        column, row = key
        return self.data[row][column]

    def __delitem__(self, key):
        """
        Reset the cell value to "0".

        :param key: (column, row) pair
        """
        column, row = key
        self.data[row][column] = 0

    def set(self, values):
        """
        Change content by a one dimensional list of values.

        :param: values: list of values
        :return: when successfully assigned list of values
        """
        row = 0
        column = 0
        for value in values:
            if row >= self.height:
                return False

            self.data[row][column] = value
            column += 1
            if column >= self.width:
                row += 1
                column = 0

        return True

    def __repr__(self):
        """ :return: string representation of this class. """
        return "Matrix(%dx%d:" % (self.width, self.height) \
               + ",".join("%s" % cell.get() for cell in self.cells()) + ")"

    def cells(self):
        """
        Iterating over each cell of the matrix.

        :return: cell (by cell)
        """
        for column in range(self.width):
            for row in range(self.height):
                yield self.Cell(column, row, self)

    def rows(self):
        """ :return: using yield you can iterator over all rows. """
        for row in range(self.height):
            yield self.Row(row, self)

    def columns(self):
        """ :return: using yield you can iterator over all columns. """
        for column in range(self.width):
            yield self.Column(column, self)

    def diagonals(self):
        """ :return: using yield you can iterator over all diagonal. """
        for row in range(self.height):
            yield self.Diagonal(0, row, 1, -1, self)
        for column in range(1, self.width):
            yield self.Diagonal(column, self.height-1, 1, -1, self)

    def main_diagonals(self):
        """ :return: using yield you can iterator over all main diagonal. """
        yield self.Diagonal(0, 0, 1, 1, self)
        yield self.Diagonal(0, self.height-1, 1, -1, self)

    def clone(self):
        """ :return: copy of this instance. """
        matrix = Matrix(self.width, self.height)
        for column in range(self.width):
            for row in range(self.height):
                matrix[column, row] = self[column, row]
        return matrix

    def __add__(self, other):
        """
        Sum of throw matrices.

        :param: other: another matrix
        :return: sum of two matrices
        """
        if not isinstance(other, self.__class__):
            raise TypeError("instance of type Matrix expected, %s given" % type(other))

        matrix = self.clone()
        for column in range(self.width):
            for row in range(self.height):
                matrix[column, row] += other[column, row]
        return matrix

    def flip(self, vertical, horizontal):
        """
        Flip matrix vertical and/or horizontal.

        :param: vertical: when true the matrix is flipped vertical
        :param: horizontal: when true the matrix is flipped horizontal
        :return: self (to allow continuous modifications)
        """
        if vertical:
            for row in range(self.height // 2):
                self.Row(row, self).swap(self.Row(self.height-row-1, self))
        if horizontal:
            for column in range(self.width // 2):
                self.Column(column, self).swap(self.Column(self.width-column-1, self))
        return self

    def __mul__(self, other):
        """
        Multiplicate this matrix with another or an factor.

        :param other: if int or float then a matrix will be returned
                      with each cell value multiplied by the given factor.
        :return: matrix if valid otherwise None
        """
        if isinstance(other, int) or isinstance(other, float):
            matrix = self.clone()
            for column in range(self.width):
                for row in range(self.height):
                    matrix[column, row] *= other
            return matrix

        elif isinstance(other, Matrix):
            matrix = Matrix(other.width, self.height)
            for row in self.rows():
                for column in other.columns():
                    matrix[column.column, row.row] = \
                        sum([a*b for a, b in zip([cell.get() for cell in row.cells()],
                                                 [cell.get() for cell in column.cells()])])
            return matrix

        return None
