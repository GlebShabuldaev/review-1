from alphabet import Alphabet
from dataclasses import dataclass
import sys
from utils import get_key


@dataclass
class Vigenere:

    def make_key_word(self, word: str, key: str) -> str:
        """Generates new key with word's length"""
        self.check_key(key)
        key_word = ''
        for i in range(len(word)):
            alph = Alphabet().get_lang(word[i])
            if word[i] in alph[0] or word[i] in alph[1]:
                key_word += key[i % len(key)]
            else:
                key_word += word[i]
        return key_word

    @staticmethod
    def check_key(key: str) -> None:
        """Checks if they key is correct"""
        alph = Alphabet().get_lang(key[0])
        for i in range(len(key)):
            if key[i] in alph[0] or key[i] in alph[1]:
                return
        else:
            print('ERROR: Key contains letters from defferent languages')
            exit(0)

    def do_vigenere(self, m: int, word: str, key: str) -> str:
        """Vigenere encryption and decryption"""
        unknwn_word = ''
        key_word = self.make_key_word(word, key)
        for i in range(len(word)):
            symbol_1 = word[i]
            symbol_2 = key_word[i]
            al = Alphabet()
            alph = al.get_lang(symbol_1)
            al.check_symbol(word[i], alph)
            if al.get_lang(symbol_2) != alph:
                print('ERROR: Key is in different language')
                sys.exit(0)
            symbol_type = al.check_type(symbol_1, alph)  # Register of a word's symbol
            key_type = al.check_type(symbol_2, alph)  # Register of a key's symbol
            symbol_position = alph[symbol_type][symbol_1]                # Word's symbol place in the alphabet
            alph_letters = alph[4][symbol_type]                     # Amount of letters in the alphabet + 1
            key_position = alph[key_type][symbol_2]                # Key's symbol place in the alphabet
            unknwn_word += get_key(alph[symbol_type], (symbol_position + alph_letters/2 + m*(key_position - alph_letters/2)) % alph_letters)
        return unknwn_word
