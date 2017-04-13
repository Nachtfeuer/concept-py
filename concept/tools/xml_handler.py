"""
.. module:: xml_handler
    :platform: Unix, Windows
    :synopis: used by XMLParser

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


class XMLHandler(object):
    """ XML handler used by XMLParser """

    classes = {}  # global dictionary of registered classes by its names

    def __init__(self):
        """ Initializing fields only """
        super(XMLHandler, self).__init__()
        self.root = None
        self.current_object = None
        self.current_tag = ""
        self.level = -1

    @staticmethod
    def register_class(theClass, name=None):
        """
        :param: cls: a class to be registered
        :param: if the name is not set (None) then cls.__name__.lower() is used.
        :return: True when succeeded otherwise False
        """
        class_name = name
        if class_name is None:
            class_name = theClass.__name__.lower()

        if class_name not in XMLHandler.classes:
            XMLHandler.classes[class_name] = theClass
            return True
        return False

    def start(self, tag, dummy):
        """
        :param: tag: name of the tag
        :param: dummy: attributes (names and values) if given
        """
        self.current_tag = tag
        self.level += 1
        if not self.current_object or tag in self.current_object.__dict__:
            if tag in self.classes:
                self.current_object = self.classes[self.current_tag]()
                if not self.root:
                    self.root = self.current_object

    def data(self, content):
        """
        :param: content: string between two tags
        """
        if self.current_object:
            self.current_object.__dict__[self.current_tag] = content

    def end(self, dummy):
        """
        :param: tag: name of the tag
        """
        self.level -= 1

    def close(self):
        """ Called when the processing of the XML is done. """
        pass
