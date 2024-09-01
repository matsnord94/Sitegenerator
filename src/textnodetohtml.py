from leafnode import LeafNode
from textnode import TextNode
from htmlnode import HTMLNode

def text_node_to_html_node(text_node):
    if text_node.text_type == "text":
        new_node = LeafNode(value = text_node.text)
    elif text_node.text_type == "bold":
        new_node = LeafNode(tag = "b", value = text_node.text)
    elif text_node.text_type == "italic":
        new_node = LeafNode(tag = "i", value = text_node.text)
    elif text_node.text_type == "code":
        new_node = LeafNode(tag = "code", value = text_node.text)
    elif text_node.text_type == "link":
        if text_node.url == None:
            raise ValueError("type link cannot have url:None")
        new_node = LeafNode(tag = "a", value = text_node.text, props = {"href": text_node.url})
    elif text_node.text_type == "image":
        if text_node.url == None:
            raise ValueError("type img requires img link")
        new_node = LeafNode(tag = "img",value = "",props = {"src": text_node.url,
                                                            "alt": text_node.text})
    else:
        raise Exception("invalid text type")
    
    return new_node