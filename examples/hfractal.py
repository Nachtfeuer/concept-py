#!/usr/bin/python
"""
Visualizing H fractal with tkinter.

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
if __name__ == "__main__":
    import math
    import Tkinter as tk
    from concept.math.point import Point2d
    from concept.math.vector import Vector2d
    from concept.math.hfractal import hfractal


    class Application(tk.Frame):
        """Simple tk application displaying a H fractal."""

        def __init__(self):
            """Init canvas and display fractal."""
            tk.Frame.__init__(self, tk.Tk())
            self.angle = 0.0
            self.scale = 1.0
            self.depth = 0

            self.master.title("H Fractal")
            self.master.geometry("640x480+50+50")
            self.canvas = tk.Canvas(self)
            self.canvas['bg'] = "#ffffff"
            self.canvas.bind("<Configure>", self.on_configure)
            self.canvas.pack(fill=tk.BOTH, expand=tk.YES)
            self.pack(fill=tk.BOTH, expand=tk.YES)

            self.bind("<Left>", self.on_key_left)
            self.bind("<Right>", self.on_key_right)
            self.bind("<Up>", self.on_key_up)
            self.bind("<Down>", self.on_key_down)
            self.bind("+", self.on_key_plus)
            self.bind("-", self.on_key_minus)
            self.focus_set()

        def set_title(self, count):
            """Change the title."""
            self.master.title("H Fractal (%d H's, angle=%.2f Degree, scale=%.2f)"
                              % (count, self.angle * 180.0 / math.pi, self.scale))

        def on_key_left(self, event):
            """Rotate hfractal to the left."""
            self.angle -= 0.05
            self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_key_right(self, event):
            """Rotate hfractal to the right."""
            self.angle += 0.05
            self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_key_up(self, event):
            """Scale hfractal (increase)."""
            self.scale += 0.05
            self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_key_down(self, event):
            """Scale hfractal (decrease)."""
            if self.scale >= (0.05 + 0.05):
                self.scale -= 0.05
                self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_key_plus(self, event):
            """Increase hfractal depth."""
            if self.depth < 7:
                self.depth += 1
                self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_key_minus(self, event):
            """Decrease hfractal depth."""
            if self.depth > 0:
                self.depth -= 1
                self.repaint(self.canvas.winfo_width(), self.canvas.winfo_height())

        def on_configure(self, event):
            """Called to react on changes to width and height."""
            self.repaint(event.width, event.height)

        def repaint(self, width, height):
            """Repaint hfractal."""
            # delete all previous lines
            self.canvas.delete(tk.ALL)
            center = Point2d(width / 2.0, height / 2.0)
            direction = Vector2d(0.0, height / 2.0).scaled(self.scale).rotated(self.angle)
            hdefs = hfractal(center, direction, 2.0, self.depth)
            self.set_title(len(hdefs))
            for hdef in hdefs:
                for line in hdef.generate_lines():
                    self.canvas.create_line(
                        line[0].x,
                        line[0].y,
                        line[0].x + line[1].x,
                        line[0].y + line[1].y
                    )

        def mainloop(self):
            """Application mainloop when called."""
            self.master.mainloop()

    def main():
        """Main function."""
        app = Application()
        app.mainloop()

    main()
