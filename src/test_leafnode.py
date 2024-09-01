import unittest
from leafnode import LeafNode

string = "<p>this is some text</p>"
a_string = "<a href=\"https://www.google.com\">sådärjaklickme</a>"

class TestHTMLNode(unittest.TestCase):
    def test_leafnode_p(self):
        case1 = LeafNode(tag = "p", value = "this is some text")
        html_code = case1.to_html()
        self.assertEqual(html_code, string)

    def test_leafnode_a(self):
        case1 = LeafNode(tag = "a", value = "sådärjaklickme", props ={"href": "https://www.google.com"})
        html_code = case1.to_html()
        print(html_code)
        self.assertEqual(html_code,a_string)

if __name__ == "__main__":
    unittest.main()