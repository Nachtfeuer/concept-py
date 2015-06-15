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


def read(fname):
    """ reading a file from current path of this file. """
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='concept',
      version='0.5.0',
      description='concepts and ideas in Python',
      long_description=read('README.md'),
      author='Thomas Lehmann',
      author_email='thomas.lehmann.private@googlemail.com',
      license="MIT",
      requires=['coverage', 'nose', 'radon', "pep8", "pep257"],
      py_modules=['concept', 'concept.primes'],
      data_files=[('concept', ['README.md'])],
      keywords="concepts ideas",
      url="https://github.com/Nachtfeuer/concept-py",
      classifiers=[
          "Programming Language :: Python",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Development Status :: 5 - Production/Stable",
          "License :: MIT",
          "Operating System :: Microsoft :: Windows",
          "Operating System :: Unix"
      ])
