"""
   =======
   License
   =======
   Copyright (c) 20147Thomas Lehmann

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
from concept.data.movies.purchase import Purchase
from concept.tools.decorator import validate_test_responsibility_for
from concept.tools.compatible import TextType


@validate_test_responsibility_for(Purchase)
class TestPurchase(unittest.TestCase):
    """testing of class concept.data.movies.purchase.Purchase class."""

    def test_init(self):
        """testing of Purchase.__init__ method."""
        purchase = Purchase()
        self.assertEqual("", purchase.where)
        self.assertEqual("", purchase.when)
        self.assertEqual("", purchase.url)

        purchase = Purchase(TextType("Amazon"), TextType("2011-11-10"),
                            TextType("http://amazon.de/dp/B001CIEOD8"))
        self.assertEqual("Amazon", purchase.where)
        self.assertEqual("2011-11-10", purchase.when)
        self.assertEqual("http://amazon.de/dp/B001CIEOD8", purchase.url)

    def test_repr(self):
        """testing of Purchase.__repr__ method."""
        purchase = Purchase(TextType("Amazon"), TextType("2011-11-10"),
                            TextType("http://amazon.de/dp/B001CIEOD8"))
        expected = "Purchase(where=Amazon, when=2011-11-10, url=http://amazon.de/dp/B001CIEOD8)"
        self.assertEqual(expected, str(purchase))

    def test_get_serializable_name(self):
        """testing of Purchase.get_serializable_name method."""
        purchase = Purchase()
        self.assertEqual("purchase", purchase.get_serializable_name())

    def test_get_serializable_fields(self):
        """testing of Purcahse.get_serializable_name method."""
        purchase = Purchase()
        fields = sorted(["where", "when", "url"])
        self.assertEqual(fields, purchase.get_serializable_fields())

    def test_is_enabled_for_attributes(self):
        """testing of Purchase.is_enabled_for_attributes method."""
        purchase = Purchase()
        self.assertEqual(True, purchase.is_enabled_for_attributes())

    def test_to_xml(self):
        """testing of Purchase.to_xml method (base class)."""
        purchase = Purchase(TextType("Amazon"), TextType("2011-11-10"),
                            TextType("http://amazon.de/dp/B001CIEOD8"))
        expected = """<purchase url="http://amazon.de/dp/B001CIEOD8" when="2011-11-10" where="Amazon"/>"""
        self.assertEqual(expected, purchase.to_xml())
