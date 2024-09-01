import unittest

from htmlnode import HTMLNode

test_props = {
    "href": "https://www.google.com", 
    "target": "_blank",
}

test_spaces = {
    "data-info": "some value with spaces",
    "target": "balle"
}
string1 = " data-info=\"some value with spaces\" target=\"balle\""
class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        case1 = HTMLNode(props = test_props)
        string = " href=\"https://www.google.com\" target=\"_blank\""
        html_code = case1.props_to_html()
        self.assertEqual(html_code, string)

    def test_props_if_empty(self):
        case1 = HTMLNode(props = {})
        html_code = case1.props_to_html()
        self.assertEqual(html_code,"")



    def test_with_spaces(self):
        case1 = HTMLNode(props = test_spaces)
        html_code = case1.props_to_html()
        self.assertEqual(html_code,string1)


        


if __name__ == "__main__":
    unittest.main()