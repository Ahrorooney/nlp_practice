# penn tree tokenization
import re
from typing import List

def penn_tree(text: str) -> List[str]:
    """
    Tokenize the text based on the Penn Treebank Tokenization.

    Parameters:
    text (str): The input text to be tokenized.

    Returns:
    List[str]: The list of tokens.
    """
    # Create a pattern to match the tokens
    pattern = re.compile(r'''(?x)    # set flag to allow verbose regexps
    (?:[A-Z]\.)+        # abbreviations, e.g. U.S.A.
    |\w+(?:[-']\w+)*    # words with optional internal hyphens or apostrophes
    |\$?\d+(?:\.\d+)?%? # currency and percentages, e.g. $12.40, 82%
    |\.\.\.             # ellipsis
    |[][.,;"'?():-_`]   # these are separate tokens; includes ], [
    ''')

    # Find all the tokens in the text that match the pattern
    tokens = pattern.findall(text)

    return tokens

#sample text
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.'

# Penn Tree Tokenization
tokens = penn_tree(text)

# Print tokens
print(tokens)