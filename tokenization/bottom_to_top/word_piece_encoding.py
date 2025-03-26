# word_piece_encoding tokenizer

# How Does Word Piece Encoding Work?
# 1. Start with a character-based vocabulary (every character is an individual token).
# 2. Compute the likelihood of merging character pairs based on how well they predict words.
# 3. Merge the most probable pair (instead of just the most frequent pair, like in BPE).
# 4. Repeat until reaching the desired vocabulary size.
# 5. Use learned subword merges to tokenize new words.

from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.processors import TemplateProcessing

# Initialize a tokenizer
tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()

# Train the tokenizer
trainer = WordPieceTrainer(vocab_size=50, special_tokens=["[UNK]", "[CLS]", "[SEP]", "[PAD]", "[MASK]"])
text_corpus = [
    "Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.",
    "Subword tokenization helps reduce vocabulary size and improve NLP models.",
]

tokenizer.train_from_iterator(text_corpus, trainer)

# Tokenize text
output = tokenizer.encode("Tokenization splits text into words.")
print("Tokens:", output.tokens)

# Decode
decoded_text = tokenizer.decode(output.ids)
print("Decoded:", decoded_text)
