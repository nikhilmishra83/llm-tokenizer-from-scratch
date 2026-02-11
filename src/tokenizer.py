# src/tokenizer.py
# Initialization
# Accept token_to_id dictionary
# Store it as self.token_to_id
# Create self.id_to_token by reversing mapping
# Store <UNK> ID in self.unk_id
# Store <EOS> ID in self.eos_id

# Encode(text)
# Preprocess input text using the same logic as vocab
# For each token:
#   if token exists → append its ID
#   else → append unk_id
# Append eos_id
# Return list of IDs

# Decode(ids)
# Convert IDs back to tokens using id_to_token
# Join tokens into text
# Fix spacing around punctuation
# Return decoded text
from src.helper import tokenize_text
from src.helper import tokenized_text_to_str

class SimpleTokenizer:
    def __init__(self, token_to_id: dict):
        self.token_to_id = token_to_id
        self.id_to_token = {id:token for token, id in token_to_id.items()}

        self.unk_token = "<UNK>"
        self.eos_token = "<EOS>"

        self.unk_id = token_to_id[self.unk_token]
        self.eos_id = token_to_id[self.eos_token]


    def encode(self, text: str) -> list[int] :
        # print("text to encode:", text)
        tokenized_text = tokenize_text(text)
        # print("tokenized_text:", tokenized_text)

        ids = []
        for token in tokenized_text:
            if token in self.token_to_id:
                ids.append(self.token_to_id[token])
            else:
                ids.append(self.unk_id)
            
        ids.append(self.eos_id)
        return ids

    def decode(self, encodings: list[int]) -> str :
        tokens = []
        for id_ in encodings:
            if id_ in self.id_to_token:
                tokens.append(self.id_to_token[id_])
            else:
                tokens.append(self.unk_token)
        
        text = tokenized_text_to_str(tokens)
        return text