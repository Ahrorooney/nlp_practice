# rule based tokenization
import re
from typing import List

def rule_based(text: str, pattern: str) -> List[str]:
    """
    Tokenize the text based on the rule defined by the pattern.

    Parameters:
    text (str): The input text to be tokenized.
    pattern (str): The pattern to match the tokens.

    Returns:
    List[str]: The list of tokens.
    """
    # Create a pattern to match the tokens
    pattern = re.compile(pattern)

    # Find all the tokens in the text that match the pattern
    tokens = pattern.findall(text)

    return tokens

#sample text
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.'

# Rule Based Tokenization
pattern = r'\b\w+\b'
tokens = rule_based(text, pattern)

# Print tokens
print(tokens)