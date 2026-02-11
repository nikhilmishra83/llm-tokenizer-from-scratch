# src/helper.py
import re

def tokenize_text(text: str) -> list[str]:
    tokens = re.split(r'([,.:;?_!"()\']|--|\s)', text)
    tokens = [t for t in tokens if t.strip()]
    return tokens

def tokenized_text_to_str(tokens: list[str]) -> str:
    # remove special tokens like <EOS>
    tokens = [t for t in tokens if t != "<EOS>"]

    text = " ".join(tokens)

    # fix spaces before punctuation
    text = re.sub(r"\s+([,.:;?_!\"()\'])", r"\1", text)

    return text
