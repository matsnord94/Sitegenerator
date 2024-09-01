from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props = None):
        super().__init__(tag,None,children,props)

    def to_html(self):
        construct_string = ""
        if self.tag is None:
            raise ValueError("parentnodes must have a tag")
        
        if self.children is None:
            raise ValueError("parentnodes must have children")
        
        construct_string += f"<{self.tag}>"

        for child in self.children:
            construct_string += child.to_html()

        construct_string += f"</{self.tag}>"
        return construct_string
    