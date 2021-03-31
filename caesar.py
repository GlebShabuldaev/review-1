from alphabet import Alphabet
from typing import Union
from utils import get_key

class Caesar:
    def __init__(self, key):
        self.key = int(key)

    def do(self, m: int, word: str) -> str:
        """Caesar encode/decode"""
        unknwn_word = ''
        for i in range(len(word)):
            symbol = word[i]
            al = Alphabet()
            alph = al.get_lang(symbol)
            al.check_symbol(word[i], alph)
            symbol_type = al.check_type(symbol, alph)             # Register of a symbol
            symbol_position = alph[symbol_type][symbol]                           # Symbol's place in the alphabet
            alph_letters = alph[4][symbol_type]                              # Amount of letters in the alphabet
            key_position = int(self.key) % alph_letters
            unknwn_word += get_key(alph[symbol_type], (symbol_position+key_position*m) % alph_letters)
        return unknwn_word
