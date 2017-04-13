"""
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
import unittest
from concept.tools.serialize import Serializable
from concept.tools.decorator import validate_test_responsibility_for


@validate_test_responsibility_for(Serializable)
class TestSerializable(unittest.TestCase):
    """testing of class pydemo.tools.serialize.Serializable class."""

    def test_init(self):
        """Testing of Serializable.__init__ method."""
        serializable = Serializable()
        self.assertEqual("serializable", serializable.get_serializable_name())
        self.assertRaises(AttributeError, serializable.get_serializable_fields)

    def test_is_derived(self):
        """Testing of Serializable.is_derived function."""
        class A(object):
            pass

        class B(A):
            def __init__(self):
                super(B, self).__init__()

        b = B()
        self.assertEqual(True, Serializable.is_derived(b, A))
        self.assertEqual(False, Serializable.is_derived(1234, A))

    def test_get_serializable_fields_with_no_field(self):
        """Testing of Serializable.get_Serializable_fields with no field."""
        class Data(Serializable):
            pass

        data = Data()
        self.assertRaises(AttributeError, data.get_serializable_fields)

    def test_get_serializable_fields(self):
        """Testing of Serializable.getSerializableFields with fields (as usual)."""
        class Data(Serializable):
            def __init__(self):
                super(Data, self).__init__()
                self.firstName = "Agatha"
                self.surName = "Christie"

        data = Data()
        self.assertEqual(["firstName", "surName"], sorted(data.get_serializable_fields()))

    def test_get_serializable_name(self):
        """Testing of Serializable.getSerializableName."""
        class Data(Serializable):
            pass

        data = Data()
        self.assertEqual("data", data.get_serializable_name())

    def test_is_enabled_for_attributes(self):
        """Testing of Serializable.is_enabled_for_attributes."""
        class DataA(Serializable):
            pass

        class DataB(Serializable):
            def __init__(self, title):
                super(DataB, self).__init__()
                self.title = title

            def is_enabled_for_attributes(self):
                return True

        data = DataA()
        self.assertEqual(False, data.is_enabled_for_attributes())

        data = DataB("hello world")
        expectedXML = """<datab title="hello world"/>"""
        self.assertEqual(expectedXML, data.to_xml())

    def test_to_xml(self):
        """Testing of Serializable.to_xml method."""
        class Person(Serializable):
            def __init__(self, firstName, surName):
                super(Person, self).__init__()
                self.firstName = firstName
                self.surName = surName

        person = Person("Agatha", "Christie")
        expectedXML = "<person><firstName>Agatha</firstName><surName>Christie</surName></person>"
        self.assertEqual(expectedXML, person.to_xml())

    def test_to_xml_with_standard_list(self):
        """Testing of Serializable.to_xml with a standard list."""
        class Values(Serializable):
            def __init__(self, values):
                super(Values, self).__init__()
                self.values = values

            def get_serializable_name(self):
                return "list"

        values = Values([10, 20, 30])
        expectedXML = "<list><values><value>10</value><value>20</value><value>30</value></values></list>"
        self.assertEqual(expectedXML, values.to_xml())

    def test_to_xml_with_serializable_field(self):
        """ Testing of Serializable.to_xml with a serializable field """
        class Field(Serializable):
            def __init__(self, first_name, sur_name):
                super(Field, self).__init__()
                self.first_name = first_name
                self.sur_name = sur_name

            def is_enabled_for_attributes(self):
                return True

        class Data(Serializable):
            def __init__(self, first_name, sur_name):
                super(Data, self).__init__()
                self.field = Field(first_name, sur_name)

        data = Data("Agatha", "Christie")
        expected = """<data><field first_name="Agatha" sur_name="Christie"/></data>"""
        self.assertEqual(expected, data.to_xml())

    def test_to_xml_with_bad_type_for_fields(self):
        """ Testing of Serializable.to_xml for failures with getSerializableFields """
        class PersonNoFieldList(Serializable):
            def get_serializable_fields(self):
                return "not a list"

        person = PersonNoFieldList()
        self.assertRaises(TypeError, person.to_xml)

    def test_to_xml_with_missing_field_in_class(self):
        """ Testing of Serializable.to_Xml for failures with getSerializableFields """
        class PersonFieldDoesNotExist(Serializable):
            def get_serializable_fields(self):
                return ["firstName"]

        person = PersonFieldDoesNotExist()
        self.assertRaises(NameError, person.to_xml)

    def test_register_class(self):
        """ Testing of Serializable.registerClass method """
        class TestRegisterClass:
            def __init__(self):
                pass

        self.assertTrue(Serializable.register_class(TestRegisterClass))
        self.assertFalse(Serializable.register_class(TestRegisterClass))

        self.assertTrue(Serializable.register_class(TestRegisterClass, "otherName"))
        self.assertFalse(Serializable.register_class(TestRegisterClass, "otherName"))

    def test_from_xml(self):
        """Testing of Serializable.to_xml method (simple)."""
        class Person:
            def __init__(self, name=""):
                self.name = name

            def __eq__(self, other):
                return self.name == other.name

        Serializable.register_class(Person)
        person = Serializable.from_xml("""<person><name>Agatha Christie</name></person>""")
        self.assertTrue(isinstance(person, Person))
        self.assertEqual(Person("Agatha Christie"), person)
