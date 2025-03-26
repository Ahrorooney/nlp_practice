# sentence_piece_encoding tokenizer

# How Does SentencePiece Work?
# 1. Train on raw text instead of pre-splitting words using spaces.
# 2. Uses either BPE or Unigram Language Model for subword learning.
# 3. Represents words as a sequence of subwords (like BPE and WordPiece).
# 4. Allows space tokens (▁) for word boundaries.

import sentencepiece as spm

# Step 1: Train SentencePiece model on sample text
text_corpus = "Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens."

# Write corpus to a temporary file
with open("corpus.txt", "w", encoding="utf-8") as f:
    f.write(text_corpus)

# Train SentencePiece model (Unigram model with vocab size of 41)
spm.SentencePieceTrainer.train(input="corpus.txt", model_prefix="spm_model", vocab_size=41)

# Load the trained model
sp = spm.SentencePieceProcessor(model_file="spm_model.model")

# Step 2: Tokenize text
text = "Tokenization splits text into words."
tokens = sp.encode(text, out_type=str)
print("Tokens:", tokens)

# Step 3: Decode tokens back to text
decoded_text = sp.decode(tokens)
print("Decoded:", decoded_text)