import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkDownBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
        )

    def test_markdown_blocks_ex_lines(self):
        md = """
This is the first paragraph with starting and trailing spaces   


and this is the second after two enters
"""

        blocks = markdown_to_blocks(md)
        self.assertEqual(
                blocks,
                [
                    "This is the first paragraph with starting and trailing spaces",
                    "and this is the second after two enters",
                ],
        )

    def test_block_to_blocktype_header(self):
        md = """
            ### This is a header
            """
        md = md.strip()
        self.assertEqual(BlockType.HEADING, block_to_block_type(md))

    def test_block_to_blocktype_not_header(self):
        md = """
            ######This is a header
            """
        md = md.strip()
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(md))


    def test_block_to_blocktype_code(self):
        md = """
            ``` This is a code
            block
            ```
            """
        md = md.strip()
        self.assertEqual(BlockType.CODE, block_to_block_type(md))
    
    def test_block_to_blocktype_not_code(self): 
        md = """ ``` This is a code
            block
            """
        md = md.strip()
        self.assertNotEqual(BlockType.CODE, block_to_block_type(md))


    def test_block_to_blocktype_quote(self):
        md = """
            >This is a quote
            >block
            """
        md = md.strip()
        self.assertEqual(BlockType.QUOTE, block_to_block_type(md))

    def test_block_to_blocktype_unordered_list(self): 
        md = """ 
        - this
        - is
        - an
        - unordered
        - list
        """
        md = md.strip()
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(md))
    
    def test_block_to_blocktype_ordered_list(self): 
        md = """ 
        1. this
        2. is
        3. an
        4. ordered
        5. list
        """
        md = md.strip()
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(md))

if __name__ == "__main__":
    unittest.main()
