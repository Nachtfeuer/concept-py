""""Module tetris."""
from random import randint
from concept.game.raster import Raster


class Tetris(object):
    """Simple tetris game."""

    SHAPES = [["****"], ["****", "*   ", "*   ", "*   "], ["***", "*"],
              ["***", "* *"], ["***", "  *"], ["***", "** ", "*  "],
              ["***", " * "], [" **", "** "], ["**", " **"], ["**", "**"]]

    def __init__(self, raster_width, raster_height):
        """Initialize tetris."""
        self.raster = Raster(raster_width, raster_height)
        self.shape = self.get_next_shape()
        self.current_row = 0
        self.current_column = (self.raster.width - self.shape.width) // 2

    def get_next_shape(self):
        """:return: random shape as raster."""
        return Raster.create_from(self.SHAPES[randint(0, len(self.SHAPES))])

    def turn_left(self):
        """Rotate shape 90 degrees to the left."""
        self.shape = self.shape.turned_left()

    def turn_right(self):
        """Rotate shape 90 degrees to the right."""
        self.shape = self.shape.turned_right()

    def move_left(self):
        """Move current shape one column to the left (when possible)."""
        if self.current_column > 0:
            self.current_column -= 1

    def move_right(self):
        """Move current shape one column to the right (when possible)."""
        if self.current_column + self.shape.width < self.raster.width:
            self.current_column += 1

    def step(self):
        """One game step."""
        if self.can_step():
            self.current_row += 1
            return True
        else:
            for scolumn, srow, value in self.shape.occupied_cells():
                self.raster.set(self.current_column + scolumn,
                                self.current_row + srow, value)

            self.shape = self.get_next_shape()
            self.current_row = 0
            return not self.is_collision(self.current_row)

    def can_step(self):
        """Check whether shape can move down one step."""
        if self.current_row + self.shape.height >= self.raster.height:
            return False
        return not self.is_collision(self.current_row + 1)

    def is_collision(self, shape_row):
        """Check collision between shape and old content in raster."""
        for scolumn, srow, _ in self.shape.occupied_cells():
            for column, row, _ in self.raster.occupied_cells():
                if scolumn + self.current_column == column and \
                   srow + shape_row == row:
                    return True
        return False
