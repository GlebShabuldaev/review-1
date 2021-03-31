from dataclasses import dataclass
import sys
from typing import List
import string


@dataclass
class Alphabet:
    def __init__(self):
        self.lower_eng = string.ascii_lowercase
        self.lower_eng = {x: self.lower_eng.index(x) for x in self.lower_eng}
        self.lower_rus = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.lower_rus = {x: self.lower_rus.index(x) for x in self.lower_rus}
        self.upper_rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.upper_rus = {x: self.upper_rus.index(x) for x in self.upper_rus}
        self.upper_eng = string.ascii_uppercase
        self.upper_eng = {x: self.upper_eng.index(x) for x in self.upper_eng}
        self.punc = string.punctuation
        self.punc = {x: self.punc.index(x) for x in self.punc}
        self.blank = string.whitespace
        self.blank = {x: self.blank.index(x) for x in self.blank}
        self.N_e = [len(self.lower_eng), len(self.upper_eng), len(self.punc), len(self.blank)]
        self.N_r = [len(self.lower_rus), len(self.upper_rus), len(self.punc), len(self.blank)]
        self.eng = [self.lower_eng, self.upper_eng, self.punc, self.blank, self.N_e]
        self.ru = [self.lower_rus, self.upper_rus, self.punc, self.blank, self.N_r]

    def check_type(self, symbol: str, alph: List[str]) -> int:
        """Determines if the symbol is lower/uppercase, punctuation or blank space"""
        self.check_symbol(symbol, alph)
        if symbol in alph[0]:
            return 0
        elif symbol in alph[1]:
            return 1
        elif symbol in alph[2]:
            return 2
        elif symbol in alph[3]:
            return 3
        else:
            print(f"ERROR: Unknown symbol {symbol}")
            sys.exit(0)

    def get_lang(self, symbol: str) -> list:
        """Determines language of a symbol"""
        if symbol in self.upper_rus or symbol in self.lower_rus:
            return self.ru
        else:
            return self.eng

    @staticmethod
    def check_symbol(symbol: str, alph: List[str]) -> None:
        """Checks if the symbol was typed correctly"""
        for i in alph:
            if symbol in i:
                return
        print(f"ERROR: Unknown symbol {symbol}")
        sys.exit(0)
