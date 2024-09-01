from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag = None, value = None, props = None):
        super().__init__(tag,value,None,props)

    def __eq__(self,leafnode):
        if not isinstance(leafnode,LeafNode):
            return False
        if not (self.tag == leafnode.tag and self.value == leafnode.value and self.props == leafnode.props):
            return False
        else:
            return True         


    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

        

