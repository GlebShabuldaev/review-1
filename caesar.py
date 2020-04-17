from alphabet import Alphabet
from dataclasses import dataclass
from typing import Union


@dataclass
class Caesar:
    @staticmethod
    def do_caesar(m: int, word: str, key: Union[int, str]) -> str:
        """Caesar encode/decode"""
        unknwn_word = ''
        for i in range(len(word)):
            symbol = word[i]
            alph = Alphabet().get_lang(symbol)
            Alphabet.check_symbol(word[i], alph)
            c = Alphabet().case(symbol, alph)             # Register of a symbol
            n = alph[c][symbol]                           # Symbol's place in the alphabet
            n_1 = alph[4][c]                              # Amount of letters in the alphabet
            k = int(key) % n_1
            unknwn_word += Alphabet.get_key(alph[c], (n+k*m) % n_1)
        return unknwn_word
