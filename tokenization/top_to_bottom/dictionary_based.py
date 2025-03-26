#dictionary_based tokenization
import re
from typing import List

def dictionary_based(text: str, dictionary: List[str]) -> List[str]:
    """
    Tokenize the text based on the dictionary of words.

    Parameters:
    text (str): The input text to be tokenized.
    dictionary (List[str]): The dictionary of words.

    Returns:
    List[str]: The list of tokens.
    """
    # Create a pattern to match the words in the dictionary
    pattern = re.compile(r'\b(?:' + '|'.join(map(re.escape, dictionary)) + r')\b')

    # Find all the words in the text that are in the dictionary
    tokens = pattern.findall(text)

    return tokens

#sample text
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.'

# Dictionary of words
dictionary = ['Tokenization', 'text', 'words', 'phrases', 'symbols', 'elements', 'tokens']

# Dictionary Based Tokenization
tokens = dictionary_based(text, dictionary)

# Print tokens
print(tokens)
