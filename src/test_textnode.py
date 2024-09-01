import unittest

from textnode import TextNode
from textnodetohtml import text_node_to_html_node
from leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    def test_text_output(self):
        node = text_node_to_html_node(TextNode("this is a text","bold"))
        node2 = LeafNode(tag = "b", value = "this is a text")
        self.assertEqual(node, node2)

    def test_function_error(self):
        with self.assertRaises(Exception) as context:
            case1 = text_node_to_html_node(TextNode("this is a text","sad"))
        self.assertEqual(str(context.exception),"invalid text type")

    def test_image_without_link(self):
        with self.assertRaises(ValueError) as context:
            case1 = text_node_to_html_node(TextNode("this is a text", "image", None))
        self.assertEqual(str(context.exception),"type img requires img link")
    


if __name__ == "__main__":
    unittest.main()