# byte_pair_encoding tokenizer

# How Does BPE Work?
# 1. Initialize the vocabulary by treating every character in the text as an individual token.
# 2. Find the most frequent adjacent character pairs in the text.
# 3. Merge the most frequent pair into a new token.
# 4. Repeat until a predefined vocabulary size is reached.
# 5. Use learned merges to tokenize new text.

# Key Components
# 1. get_pair_statistics(words): Counts how often character pairs appear in words.
# 2. merge_vocab(pair, v_in): Merges the most frequent pair into a single token.
# 3. learn_bpe(words): Iteratively applies BPE merging until the vocabulary size is reached.
# 4. segment_word(word): Tokenizes a word based on learned BPE rules.
# 5. segment_text(text): Tokenizes an entire sentence using learned BPE.

import os
import sys
import re
import random
import copy
import collections
from typing import List, Tuple

class BytePairEncoding:
    def __init__(self, vocab_size: int):
        self.vocab_size = vocab_size
        self.bpe_codes = {}
        self.bpe_codes_reverse = {}
        self.bpe_codes_freq = collections.defaultdict(int)
        self.cache = {}

    def get_pair_statistics(self, words: List[str]) -> collections.defaultdict:
        """
        Get the pair statistics of the words.

        Parameters:
        words (List[str]): The list of words.

        Returns:
        collections.defaultdict: The pair statistics of the words.
        """
        pair_statistics = collections.defaultdict(int)
        for word in words:
            symbols = word.split()
            for i in range(len(symbols) - 1):
                pair_statistics[symbols[i], symbols[i + 1]] += 1
        return pair_statistics

    def merge_vocab(self, pair: Tuple[str, str], v_in: List[str]) -> List[str]:
        """
        Merge the pair of symbols in the vocabulary.

        Parameters:
        pair (Tuple[str, str]): The pair of symbols.
        v_in (List[str]): The input vocabulary.

        Returns:
        List[str]: The output vocabulary.
        """
        v_out = []
        bigram = re.escape(' '.join(pair))
        p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        for word in v_in:
            w_out = p.sub(''.join(pair), word)
            v_out.append(w_out)
        return v_out

    def learn_bpe(self, words: List[str]):
        """
        Learn the Byte Pair Encoding (BPE) from the words.

        Parameters:
        words (List[str]): The list of words.
        """
        vocab = collections.defaultdict(int)
        for word in words:
            vocab[' '.join(list(word)) + ' </w>'] += 1

        for i in range(self.vocab_size):
            pairs = self.get_pair_statistics(vocab)
            if not pairs:
                break

            best = max(pairs, key=pairs.get)
            vocab = self.merge_vocab(best, vocab)

            self.bpe_codes[best] = i
            self.bpe_codes_reverse[best[0] + best[1]] = best

            self.bpe_codes_freq[best] = pairs[best]

    def segment_word(self, word: str) -> str:
        """
        Segment the word using the learned BPE.

        Parameters:
        word (str): The input word to be segmented.

        Returns:
        str: The segmented word.
        """
        if word in self.cache:
            return self.cache[word]

        word = word + '</w>'
        symbols = list(word)

        pairs = self.get_pair_statistics([word])
        while pairs:
            bigram = min(pairs, key=pairs.get)
            if pairs[bigram] < 2:
                break
            first, second = bigram
            new_word = []
            i = 0
            while i < len(symbols):
                try_bigram = symbols[i] + symbols[i + 1]
                if try_bigram == first + second:
                    new_word.append(first + second)
                    i += 2
                else:
                    new_word.append(symbols[i])
                    i += 1
            new_word = new_word + symbols[i:]
            symbols = new_word
            if len(symbols) == 1:
                break
            else:
                pairs = self.get_pair_statistics([' '.join(symbols)])

        # Don't print end-of-word symbols
        if symbols[-1] == '</w>':
            symbols = symbols[:-1]
        elif symbols[-1].endswith('</w>'):
            symbols[-1] = symbols[-1].replace('</w>', '')

        out_word = ' '.join(symbols)
        self.cache[word] = out_word
        return out_word

    def segment_text(self, text: str) -> str:
        """
        Segment the text using the learned BPE.

        Parameters:
        text (str): The input text to be segmented.

        Returns:
        str: The segmented text.
        """
        words = text.split()
        out_words = []
        for word in words:
            out_word = self.segment_word(word)
            out_words.append(out_word)
        out_text = ' '.join(out_words)
        return out_text

#sample text
text = 'Tokenization splits text into words, phrases, symbols or other meaningful elements, which are called tokens.'
vocab_size = 10

# Byte Pair Encoding Tokenization
bpe = BytePairEncoding(vocab_size)
bpe.learn_bpe(text.split())
tokens = bpe.segment_text(text)

# Print tokens
print(tokens)
