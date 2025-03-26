# spacy tokenizer

import spacy
from spacy.lang.en import English
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.tokens import Token
from typing import List

def spacy_tokenizer(text: str) -> List[str]:
    """
    Tokenize the text using the Spacy Tokenizer.

    Parameters:
    text (str): The input text to be tokenized.

    Returns:
    List[str]: The list of tokens.
    """
    # Load the English tokenizer, tagger, parser, NER, and word vectors
    nlp = English()

    # Create a Doc object
    doc = nlp(text)

    # Create a list of tokens
    tokens = [token.text for token in doc]

    return tokens

#sample text
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens. олвс'

# Spacy Tokenization
tokens = spacy_tokenizer(text)

# Print tokens
print(tokens)