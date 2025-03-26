# unigram_language_model tokenizer

# How Does the Unigram Language Model Work?
# 1. Start with a large vocabulary of subwords (all possible segmentations).
# 2. Assign probabilities to each subword based on how well it explains the corpus.
# 3. Iteratively prune the vocabulary by removing the least probable subwords while maximizing the probability of the training data.
# 4. Final vocabulary is optimized for efficiency and robustness.

import sentencepiece as spm

# Step 1: Create a text corpus
text_corpus = "Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens."

# Write corpus to a temporary file
with open("corpus.txt", "w", encoding="utf-8") as f:
    f.write(text_corpus)

# Train SentencePiece model using Unigram LM
spm.SentencePieceTrainer.train(
    input="corpus.txt", model_prefix="unigram_model", vocab_size=41, model_type="unigram"
)

# Load the trained model
sp = spm.SentencePieceProcessor(model_file="unigram_model.model")

# Tokenize text
text = "Tokenization splits text into words."
tokens = sp.encode(text, out_type=str)
print("Tokens:", tokens)

# Decode tokens back to text
decoded_text = sp.decode(tokens)
print("Decoded:", decoded_text)

