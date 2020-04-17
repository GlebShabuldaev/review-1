from caesar import Caesar
from alphabet import Alphabet
from train import Train
from dataclasses import dataclass
import sys


@dataclass
class Hack:
    def hack(self, model: dict, word: str) -> int:
        """Determination of a key"""
        sums = self.sums_make(model, word)
        value = min(sums.values())
        return Alphabet().get_key(sums, value)

    def sums_make(self, model: dict, word: str) -> dict:
        """Combines every degree for keys in a dict"""
        sums = {}
        alph = Alphabet().get_lang(list(model.keys())[0])
        for key in alph[0].values():
            text = Caesar().do_caesar(-1, word.lower(), key)
            dic = Train().letter_density(text)
            sums[key] = self.compare(model, dic)
        return sums

    @staticmethod
    def compare(dic1: dict, dic2: dict) -> int:
        """Degree of similarity for a single key"""
        sum = 0
        for symbol in dic1:
            if Alphabet().get_lang(symbol) != Alphabet().get_lang(list(dic1.keys())[0]):
                print('ERROR: Text is written in multiple languages')
                sys.exit(0)
            if symbol in dic2:
                sum += (dic1[symbol] - dic2[symbol])**2
            else:
                sum += (dic1[symbol])**2
        return sum
