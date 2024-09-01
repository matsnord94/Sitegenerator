import unittest
from parentnode import ParentNode
from leafnode import LeafNode

testArray =  [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ]

testArray2 =  [
        ParentNode(tag = "p", children = testArray)
    ]

string = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></p>"
string2 = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"

class TestHTMLNode(unittest.TestCase):
    def test_parent_node(self):
        case1 = ParentNode(tag = "p", children = testArray2)
        html_code = case1.to_html()
       # print(html_code)
        self.assertEqual(html_code, string)

    def test_parent_error(self):
        case1 = ParentNode(tag = None, children = testArray2)
        with self.assertRaises(ValueError) as context:
            case1.to_html()
        self.assertEqual(str(context.exception),"parentnodes must have a tag")


 
if __name__ == "__main__":
    unittest.main()