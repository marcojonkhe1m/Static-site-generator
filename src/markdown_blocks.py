from enum import Enum
from htmlnode import HTMLNode, ParentNode
from inline import text_to_textnodes
from textnode import text_node_to_html, TextNode 

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
    nodes = []
    for block in blocks:
        html_node = block_to_html_node(block)
    return ParentNode("<div>", children=nodes)

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == BlockType.PARAGRAPH:
        return paragraph_to_html_node(block)
    elif block_type == BlockType.HEADING:
        return heading_to_html_node(block)
    elif block_type == BlockType.CODE:
        return code_to_html_node(block)
    elif block_type == BlockType.QUOTE:
        return quote_to_html_node(block)
    elif block_type == BlockType.UNORDEREDLIST:
        return ulist_to_html_node
    else:
        return olist_to_html_node


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_html_node(block):
    rank = heading_rank(block)
    text = block[rank + 1:]
    children = text_to_children(text)
    return ParentNode(f"h{rank}", children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code markdown")
    text = block[4:-3]
    html_node = text_node_to_html(TextNode(text, BlockType.NORMAL))
    code = ParentNode("code", html_node)
    return ParentNode("pre", code)

def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not startswith(">"):
            raise ValueError("invalid quote markdown")
        new_lines.append(line.lstrip(">").strip())
    quote = " ".join(new_lines)
    children = text_to_children(quote)
    return ParentNode("blockquote", children)

def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def heading_rank(header):
    print(f"header: {header}")
    i = 0
    while header[i] == "#" and i < 6:
        print(f"i: {i}")
        i += 1
    return i

def text_to_children(text):
    nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        nodes.append(text_node_to_html(node))
    return nodes

