"""
Package setup.

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
import os
from distutils.core import setup
from concept import VERSION


def read(fname):
    """ reading a file from current path of this file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='concept-py',
      version=VERSION,
      description='concepts and ideas in Python',
      long_description=read('README.md'),
      author='Thomas Lehmann',
      author_email='thomas.lehmann.private@googlemail.com',
      license="MIT",
      requires=['coverage', 'nose', 'radon', "pep8", "pep257"],
      packages=['concept', 'concept.primes', 'concept.math',
                'concept.performance', 'concept.query',
                'concept.graph.gnuplot', 'concept.tools'],
      data_files=[('concept', ['README.md',
                               'examples/primes.py',
                               'examples/learn.py',
                               'examples/easy-mail.py',
                               'examples/easy-mail.yml',
                               'examples/easy-mail.html'])],
      keywords="concepts ideas",
      url="https://github.com/Nachtfeuer/concept-py",
      classifiers=[
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: Implementation :: PyPy",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Development Status :: 5 - Production/Stable",
          "License :: OSI Approved :: MIT License",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: Unix"
      ])
