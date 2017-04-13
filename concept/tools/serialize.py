"""
.. module:: serialize
    :platform: Unix, Windows
    :synopis: some tools for saving data

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
import inspect
from xml.etree.ElementTree import XMLParser
from xml.sax.saxutils import escape
from concept.tools.xml_handler import XMLHandler


class Serializable(object):
    """ provides functionality to serialize data; it kept as simple as possible;
        this means you have to accept some simple rules (limitations):
        - fields are written in sorted order.
        - all fields are identically to the tag name (expected).
        - it's assumed that you create your fields in your __init__ and that
          you do not create other than fields.
        - when writing a list all entries not derived from this class are
          wrapped by a "value" tag..
        - if you would like to have control over the order of fields and which
          fields are written then implement 'getSerializableFields'.
        - you can change the tag name for your class by implementing
          the method 'getSerializableName' (default is lower case of your class name).
        - In your derived class you have to call 'super(YourClass, self).__init__()'
          in 'YourClass.__init__'.
        - for derived classes the "to_xml" string is used for other object - basically -
          the string representation is used.
        - to_xml does NOT do pretty printing.
    """

    def __init__(self):
        """
        remember all those entries which are defined before calling __init__ (in derived class)
        """
        self.__not_serializable__ = set(key for key in self.__dict__.keys())
        self.__not_serializable__.add("__not_serializable__")

    def get_serializable_fields(self):
        """
        :rtype: intention is to have a list of valid fields names
                for which the data will be serialized
        """
        fields = sorted(u"%s" % field for field in self.__dict__.keys()
                        if field not in self.__not_serializable__)
        if len(fields) == 0:
            raise AttributeError("missing attributes for serialization")
        return fields

    def get_serializable_name(self):
        """
        :rtype: intention is to have the outer name/tag for the data (usually lower case)
        """
        return self.__class__.__name__.lower()

    def is_enabled_for_attributes(self):
        """
        :rtype: when True values for simple fields (not serializable objects and not lists)
                are written as attributes inside the start tag
        """
        return False

    @staticmethod
    def is_derived(instance, base_class):
        """
        :param a: an instance of something
        :param b: a class type
        :return: True when instance a is of a type that is derived from type in b.
        """
        try:
            return inspect.isclass(instance.__class__) and \
                issubclass(instance.__class__, base_class)
        except TypeError:
            return False

    def to_xml(self):
        """
        :rtype: xml representation of this class (or derived class)
        """
        fields = self.get_serializable_fields()
        if not isinstance(fields, list):
            raise TypeError("expected a list but got a %s" % str(type(fields)))

        attributes = ""
        counter = 0
        if self.is_enabled_for_attributes():
            for field in fields:
                if field in self.__dict__ and not isinstance(self.__dict__[field], list):
                    attributes += u" %s=\"%s\"" % (field, escape("%s" % self.__dict__[field]))

        xml = u"<%s%s" % (self.get_serializable_name(), attributes)
        for field in fields:
            if field not in self.__dict__:
                raise NameError("field %s has not been found" % field)

            if isinstance(self.__dict__[field], list):
                if counter == 0:
                    xml += u">"

                xml += u"<%s>" % field
                for entry in self.__dict__[field]:
                    if self.is_derived(entry, Serializable):
                        xml += entry.to_xml()
                    else:
                        xml += u"<value>%s</value>" % escape("%s" % entry)
                counter += 1
                xml += u"</%s>" % field
            else:
                if not self.is_enabled_for_attributes():
                    if counter == 0:
                        xml += u">"

                    if self.is_derived(self.__dict__[field], Serializable):
                        xml += u"%s" % self.__dict__[field].to_xml()
                    else:
                        xml += u"<%s>%s</%s>" % (field, escape(u"%s" % self.__dict__[field]), field)
                    counter += 1

        if counter > 0:
            xml += u"</%s>" % self.get_serializable_name()
        else:
            xml += u"/>"
        return xml

    @staticmethod
    def register_class(theClass, name=None):
        """
        :param: cls: a class to be registered
        :param: if the name is not set (None) then cls.__name__.lower() is used.
        :return: True when succeeded otherwise False
        """
        return XMLHandler.register_class(theClass, name)

    @staticmethod
    def from_xml(xml):
        """
        :param: xml string
        :rtype: object tree from XML string
        """
        handler = XMLHandler()
        parser = XMLParser(target=handler)
        parser.feed(xml)
        parser.close()
        return handler.root
