from sacremoses import MosesTokenizer, MosesDetokenizer

# Initialize tokenizer and detokenizer
mt = MosesTokenizer()
md = MosesDetokenizer()

# Example sentence
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.'

# Tokenize
tokens = mt.tokenize(text, return_str=True)
print("Tokenized:", tokens)

# Detokenize (convert back to sentence)
detokenized_text = md.detokenize(tokens.split())
print("Detokenized:", detokenized_text)
