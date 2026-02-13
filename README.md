# 📘 LLM Tokenizer from Scratch (Python)

> Understanding how Large Language Models preprocess text by building a tokenizer from the ground up.

---

## 🚀 Overview

This project implements a **word-level tokenizer from scratch** in Python to understand how Large Language Models (LLMs) process text before training or inference.

It demonstrates:

- 🔹 Regex-based tokenization  
- 🔹 Vocabulary construction from corpus text  
- 🔹 Encoding text → token IDs  
- 🔹 Decoding token IDs → readable text  
- 🔹 Handling unknown tokens & sequence boundaries  

🧭 This project is part of a deeper exploration into **LLM internals**, with **Byte Pair Encoding (BPE)** planned next.

---

## ✨ Features

✅ Tokenizes text into words & punctuation  
✅ Builds vocabulary from corpus text  
✅ Handles unknown tokens with `<UNK>`  
✅ Appends `<EOS>` (end-of-sequence) marker  
✅ Encodes text → numeric token IDs  
✅ Decodes IDs → readable text  
✅ Clean modular architecture  

---

## 🧠 How It Works

### 1️⃣ Tokenization

Text is split into tokens using regex:

- words  
- punctuation  
- whitespace removed  

**Example**

```
Hello everyone, it's nice to meet you.
```

⬇

```
["Hello", "everyone", ",", "it", "'", "s", "nice", "to", "meet", "you", "."]
```

---

### 2️⃣ Vocabulary Building

From training text:

- unique tokens are extracted  
- special tokens are added:
  - `<UNK>` → unknown tokens  
  - `<EOS>` → end of sequence  
- tokens are mapped to integer IDs  

---

### 3️⃣ Encoding

Text → Tokens → IDs

```
Hello everyone!
```

⬇

```
[12, 45, 7, 1]
```

Where `1` may represent `<EOS>`.

---

### 4️⃣ Decoding

IDs → Tokens → Text

Restores readable text with proper punctuation spacing.

---

## 📁 Project Structure

```
src/
  helper.py        # tokenization & text reconstruction
  vocab.py         # vocabulary builder
  tokenizer.py     # encode/decode logic
  main.py          # example usage

requirements.txt
.gitignore
```

---

## 🧩 Module Overview

### 📄 helper.py
- `tokenize_text()` → splits text into tokens  
- `tokenized_text_to_str()` → reconstructs text  

### 📄 vocab.py
Builds vocabulary from training corpus.

### 📄 tokenizer.py
Implements `SimpleTokenizer`:

- stores vocabulary  
- encodes text → ids  
- decodes ids → text  

### 📄 main.py
Demonstrates end-to-end usage.

---

## ▶️ Running the Project

### 1️⃣ Activate environment

```bash
source .venv/bin/activate
```

### 2️⃣ Run the program

```bash
python -m src.main
```

---

## 🧪 Example Output

```
Hello everyone, it's nice to meet you. into tokens:
[45, 78, 9, 23, ...]

after decoding:
Hello everyone, it's nice to meet you.
```

---

## 🎯 Learning Goals

This project demonstrates:

- how tokenizers prepare text for LLMs  
- vocabulary creation & token mapping  
- sequence boundary handling  
- modular Python design  

---

## 🔜 Next Steps

Planned improvements:

- ✅ Byte Pair Encoding (BPE) tokenizer  
- subword tokenization  
- vocabulary size control  
- padding & batching support  
- tokenizer serialization  
- performance optimizations  

---

## 📚 Why This Matters

Understanding tokenization helps explain:

- how LLMs understand text  
- why unknown words disappear  
- how vocabulary size affects models  
- how subwords enable generalization  

---

## 🛠 Built With

- Python 3  
- Regex (`re`)  
- Standard library only  

---

## 👤 Author

**Nikhil Mishra**  
Learning LLM internals by building components from scratch.

---

## ⭐ If you found this useful

Consider starring ⭐ the repository to follow future improvements.
