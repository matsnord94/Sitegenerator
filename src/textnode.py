class TextNode():
    def __init__(self,text,text_type,url = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,textnode):
        if self.text == textnode.text and self.text_type == textnode.text_type and self.url == textnode.url:
            return True

    def __repr__(self):
        return "TextNode(TEXT, TEXT_TYPE, URL)"