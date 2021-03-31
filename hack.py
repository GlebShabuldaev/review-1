from caesar import Caesar
from alphabet import Alphabet
from train import Train
from dataclasses import dataclass
import sys
from utils import get_key
from typing import Dict
from collections import defaultdict


@dataclass
class Hack:
    def hack(self, model: Dict[str, int], word: str) -> int:
        """Determination of a key"""
        sums = self.sums_make(model, word)
        value = min(sums.values())
        return get_key(sums, value)

    def sums_make(self, model: Dict[str, int], word: str) -> Dict[str, int]:
        """Combines every degree for keys in a dict"""
        sums = {}
        alph = Alphabet().get_lang(list(model.keys())[0])
        for key in alph[0].values():
            text = Caesar(key).do(-1, word.lower())
            dic = defaultdict(lambda: 0, Train().letter_density(text))
            sums[key] = self.compare(model, dic)
        return sums

    @staticmethod
    def compare(dic1: Dict[str, int], dic2: Dict[str, int]) -> int:
        """Degree of similarity for a single key"""
        sum = 0
        for symbol in dic1:
            if Alphabet().get_lang(symbol) != Alphabet().get_lang(list(dic1.keys())[0]):
                print('ERROR: Text is written in multiple languages')
                sys.exit(0)
            sum += (dic1[symbol] - dic2[symbol])**2
        return sum
