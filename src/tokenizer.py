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