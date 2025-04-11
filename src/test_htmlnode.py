import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, World!")
        self.assertEqual(node.to_html(), "<p>Hello, World!</p>")

    def test_leaf_to_html_props(self):
        node = LeafNode("a", "Hello, World!", {"href": "https://www.google.com"},)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Hello, World!</a>')
    
    def test_no_tag(self):
        node = LeafNode(tag=None, value="Hello, World!")
        self.assertEqual(node.to_html(), "Hello, World!")

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

if __name__ == "__main__":
    unittest.main() 


