"""
Mechanism for serialization with XML.

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
from concept.tools.compatible import TextType


class Serializable(object):
    """
    Provide functionality to serialize data; it kept as simple as possible.

    This means you have to accept some simple rules (limitations):
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
        """Remember all those entries which are defined before init (in derived class)."""
        self.__not_serializable__ = set(key for key in self.__dict__.keys())
        self.__not_serializable__.add("__not_serializable__")

    def get_serializable_fields(self):
        """
        Provide fields to serialize (default: all fields of current instance).

        :rtype: intention is to have a list of valid fields names
                for which the data will be serialized
        """
        fields = sorted("%s" % field for field in self.__dict__.keys()
                        if field not in self.__not_serializable__)
        if len(fields) == 0:
            raise AttributeError("missing attributes for serialization")
        return fields

    def get_serializable_name(self):
        """
        Mechanism to overwrite tag name (default: class name in lower case letters).

        :rtype: intention is to have the outer name/tag for the data (usually lower case)
        """
        return self.__class__.__name__.lower()

    def is_enabled_for_attributes(self):
        """
        Mechanism of derived classes to controll whether fields are serialized as XML attributes.

        :rtype: when True values for simple fields (not serializable objects and not lists)
                are written as attributes inside the start tag
        """
        return False

    @staticmethod
    def is_derived(instance, base_class):
        """
        Check whether given instance is derived from a certain class.

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
        Serializing current class instance to XML.

        :rtype: xml representation of this class (or derived class)
        """
        fields = self.get_serializable_fields()
        if not isinstance(fields, list):
            raise TypeError("expected a list but got a %s" % str(type(fields)))

        attributes = ""
        counter = 0
        covered = []
        if self.is_enabled_for_attributes():
            for field in fields:
                if field in self.__dict__ and (
                    isinstance(self.__dict__[field], TextType) or
                        isinstance(self.__dict__[field], str) or
                        isinstance(self.__dict__[field], int) or
                        isinstance(self.__dict__[field], float)):
                    attributes += " %s=\"%s\"" % (field, escape("%s" % self.__dict__[field]))
                    covered.append(field)

        xml = "<%s%s" % (self.get_serializable_name(), attributes)
        for field in fields:
            if field not in self.__dict__:
                raise NameError("field %s has not been found" % field)

            if isinstance(self.__dict__[field], list):
                if counter == 0:
                    xml += ">"

                xml += "<%s>" % field
                for entry in self.__dict__[field]:
                    if self.is_derived(entry, Serializable):
                        xml += entry.to_xml()
                    else:
                        xml += "<value>%s</value>" % escape("%s" % entry)
                counter += 1
                xml += "</%s>" % field
            else:
                if field not in covered:
                    if counter == 0:
                        xml += ">"

                    if self.is_derived(self.__dict__[field], Serializable):
                        xml += "%s" % self.__dict__[field].to_xml()
                    else:
                        xml += "<%s>%s</%s>" % (field, escape("%s" % self.__dict__[field]), field)
                    counter += 1

        if counter > 0:
            xml += "</%s>" % self.get_serializable_name()
        else:
            xml += "/>"
        return xml

    @staticmethod
    def register_class(theClass, name=None):
        """
        Register a class for a tag name.

        :param: cls: a class to be registered
        :param: if the name is not set (None) then cls.__name__.lower() is used.
        :return: True when succeeded otherwise False
        """
        return XMLHandler.register_class(theClass, name)

    @staticmethod
    def from_xml(xml):
        """
        Deserialize from a XML string.

        :param: xml string
        :rtype: object tree from XML string
        """
        handler = XMLHandler()
        parser = XMLParser(target=handler)
        parser.feed(xml)
        parser.close()
        return handler.root
