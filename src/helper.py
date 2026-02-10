# src/helper.py
import re

def tokenize_text(text: str) -> list[str]:
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = [t for t in tokens if t.strip()]
    return tokens
