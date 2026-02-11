# src/main.py
from pathlib import Path
from pprint import pprint
from src.vocab import build_vocabulary
from src.tokenizer import SimpleTokenizer

def main():
    sample_sentence = "Hello everyone, it's nice to meet you."
    with open("text_files/book_sample_2.txt", "r", encoding="utf-8") as f:
        text = f.read()
        file_name = Path(f.name).name

    print(f"file name is: {file_name}")
    print(f"total number of characters: {len(text)}")
    # print(text[:99])
    print("-" * 60)

    # calling build_vocabulary, passing it a text and storing dictionary returned by it 
    vocab = build_vocabulary(text)
    # vocab = build_vocabulary(sample_sentence)

    # print("vocabulary build by us:", vocab)
    print("vocab size:", len(vocab))
    # print("f20 tokens from 51 to 70:", list(vocab.items())[51:70])

    # for token, idx in vocab.items():
    #     print(token, "->", idx)

    # tokens_51_to_70 = list(vocab.items())[51:70]
    # print("20 tokens from index 51 to 70:")
    # pprint(list(vocab.items())[51:70])

    tokenizer = SimpleTokenizer(vocab)
    tokens = tokenizer.encode(sample_sentence)
    print(f"{sample_sentence} into tokens:")
    pprint(tokens)

    sample_text_decoded = tokenizer.decode(tokens)
    print(f"{sample_sentence} after decoding:", sample_text_decoded)


if __name__ == "__main__":
    main()