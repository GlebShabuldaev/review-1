from alphabet import Alphabet
from dataclasses import dataclass
import sys


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
            alph = Alphabet().get_lang(symbol_1)
            Alphabet().check_symbol(word[i], alph)
            if Alphabet().get_lang(symbol_2) != alph:
                print('ERROR: Key is in different language')
                sys.exit(0)
            c_1 = Alphabet().case(symbol_1, alph)  # Register of a word's symbol
            c_2 = Alphabet().case(symbol_2, alph)  # Register of a key's symbol
            n = alph[c_1][symbol_1]                # Word's symbol place in the alphabet
            n_1 = alph[4][c_1]                     # Amount of letters in the alphabet + 1
            k = alph[c_2][symbol_2]                # Key's symbol place in the alphabet
            unknwn_word += Alphabet().get_key(alph[c_1], (n + n_1/2 + m*(k - n_1/2)) % n_1)
        return unknwn_word
