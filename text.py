from basic import SYMBOLS
from basic import SYMHEIGHT

def generate_ascii(text: str) -> str:
    ascii_lines: list = ["" for _ in range(SYMHEIGHT)]
    
    for char in text:
        for index, line in enumerate(SYMBOLS[char].split("\n")):
            ascii_lines[index] += line
    
    return "\n".join(ascii_lines)