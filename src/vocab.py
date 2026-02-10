# src/vocab.py
# Accept raw training text
# Split text into tokens using a single regex:
#   words
#   punctuation
#   ignore whitespace
# Remove empty tokens
# Create a set of unique tokens
# Add special tokens:
#   <UNK>
#   <EOS>
# Assign integer IDs using enumerate
# Return token_to_id dictionary

from src.helper import tokenize_text

def build_vocabulary(text: str) -> dict:
    print("text length:", len(text))

    token_list = tokenize_text(text)
    print("length of tokens:", len(token_list))

    unique_tokens = sorted(set(token_list))
    print("length of unique tokens:", len(unique_tokens))

    # special tokens with stable IDs
    special_tokens = ["<UNK>", "<EOS>"]
    all_tokens = special_tokens + unique_tokens

    vocab = {token: idx for idx, token in enumerate(all_tokens)}
    print("length of vocab:", len(vocab))

    return vocab


if __name__ == "__main__":
    with open("text_files/book_sample_1.txt", "r", encoding="utf-8") as f:
        text = f.read()

    print(f"total number of characters: {len(text)}")
    print(text[:99])
    print("-" * 60)

    build_vocabulary(text)
