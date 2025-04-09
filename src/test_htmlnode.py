import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(repr(node), repr(node2))

    def test_htmlnode(self):
        node = HTMLNode("a", "link", None, {
            "href": "https://www.google.com", "target": "_blank",
        })
        self.assertEqual(
            "this is an html node(a, link, None, {'href': 'https://www.google.com', 'target': '_blank'})",
            repr(node)
        )

    def test_props_to_html(self):
        dict = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        node = HTMLNode("a", "link", None, dict)
        self.assertEqual(' href="https://www.google.com" target="_blank"',
                         node.props_to_html()
                         )

if __name__ == "__main__":
    unittest.main() 

