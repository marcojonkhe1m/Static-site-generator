from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "text" 
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return(
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html(textnode: TextNode):
    text_to_html_dict = {
        TextType.NORMAL: LeafNode(None, textnode.text),
        TextType.BOLD: LeafNode("b", textnode.text),
        TextType.ITALIC: LeafNode("i", textnode.text),
        TextType.CODE: LeafNode("code", textnode.text),
        TextType.LINK: LeafNode("a", textnode.text, {"href": textnode.url}),
        TextType.IMAGE: LeafNode("img", None, {"src": textnode.url, "alt": textnode.text}),
    }
    if isinstance(textnode.text_type,TextType):
        return text_to_html_dict[textnode.text_type]
    raise Exception("Given text type is not valid!")
