class TextNode:
    def __init__(self, text, text_type, url = None):
        pass

    def __eq__(self, other_node):
        return((self.text.lower(), self.text_type, url) ==
               (other_node.text.lower(), other_node.text_type, url))

    def __repr__(self):
        return str()