class HTMLNode():
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        return f"This is the HTMLNodes properties: tag: {self.tag} value: {self.value} children: {self.children} props: {self.props}"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        new_string = ""
        if self.props == None or self.props == "":
            return ""
        for prop in self.props:
            new_string += f" {prop}=\"{self.props[prop]}\""

        return new_string.rstrip(" ")
    
    