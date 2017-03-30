"""
   Game raster.

.. module:: raster
    :platform: Unix, Windows
    :synopis: game raster.

.. moduleauthor:: Thomas Lehmann <thomas.lehmann.private@googlemail.com>

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
class Raster(object):
    """Game raster."""

    def __init__(self, width, height, default_cell_value=None):
        """Init raster for a given width and height."""
        self.width = width
        self.height = height
        self.default_cell_value = default_cell_value
        self.rows = []

        for _ in range(self.height):
            row = []
            for _ in range(self.width):
                row.append(default_cell_value)
            self.rows.append(row)

    @staticmethod
    def create_from(data):
        """Creating a raster from a list of lists."""
        if isinstance(data, list) and len(set(len(entry) for entry in data)) == 1:
            raster = Raster(len(data[0]), len(data))
            for row, values in enumerate(data):
                for column, value in enumerate(values):
                    raster.set(column, row, value)
            return raster
        return None

    def set(self, column, row, obj):
        """Change cell content for a given column and row."""
        if 0 <= column < self.width and 0 <= row <= self.height:
            self.rows[row][column] = obj

    def get(self, column, row):
        """Get cell content for a given column and row."""
        if 0 <= column < self.width and 0 <= row <= self.height:
            return self.rows[row][column]
        return None

    def turned_left(self):
        """Provide rotation of current matrix 90 degree to the left."""
        new_raster = Raster(self.height, self.width)
        for row in range(self.height):
            for column in range(self.width):
                new_raster.set(row, column, self.get(self.width-column-1, row))

        return new_raster

    def turned_right(self):
        """Provide rotation of current matrix 90 degree to the right."""
        new_raster = Raster(self.height, self.width)
        for row in range(self.height):
            for column in range(self.width):
                new_raster.set(new_raster.width-row-1, column, self.get(column, row))

        return new_raster

    def occupied_cells(self):
        """
        Provided row, column and value for cells not having default value.

        :returns: tuple: column, row, cell value
        """
        for row in range(self.height):
            for column in range(self.width):
                if not self.rows[row][column] == self.default_cell_value:
                    yield column, row, self.rows[row][column]
