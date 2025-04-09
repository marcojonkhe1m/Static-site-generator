import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_url(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT, "https://url.nl")
        node2 = TextNode("This is a text node", TextType.ITALIC_TEXT,"https://url.nl")
        self.assertEqual(node, node2)

    def test_uneq(self):
        node = TextNode("This is not a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_uneq_texttype(self):
        node = TextNode("This is a text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)

    def test_uneq_url(self):
        node = TextNode("This is a text node", TextType.IMAGE, "test.url")
        node2 = TextNode("This is a text node", TextType.IMAGE, None)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.LINK, "test.url")
        self.assertEqual("TextNode(This is a text node, link, test.url)", repr(node))


if __name__ == "__main__":
    unittest.main()
