from enum import Enum
from htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    i = 0
    while block[i] == "#" and i < 6:
        i += 1
        if block[i] == " ":
            return BlockType.HEADING

    if block[:3] == "```" and block[-3:] == "```":
        return BlockType.CODE

    lines = block.split("\n")
    for line in lines:
        if line[:1] != ">":
            break
        return BlockType.QUOTE
    
    for line in lines:
        if line[:2] != "- ":
            break
        return BlockType.UNORDERED_LIST

    for j in range(1, len(lines)+1):
        print(f"j: {j}")
        line = lines[j-1]
        print(f"line: {line}")
        if line[:3] != f"{j}. ":
            break
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH

def markdown_to_blocks(markdown):
    block_strings = markdown.split("\n\n")
    filtered_blocks = []
    for string in block_strings:
        if string == "":
            continue
        block = string.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.PARAGRAPH:
            HTMLNode(tag="<p>", value=block)
        elif block_type == BlockType.HEADING:
        
