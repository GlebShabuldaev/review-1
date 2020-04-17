from dataclasses import dataclass
import sys
import string


@dataclass
class Alphabet:
    def __init__(self):
        self.l_e = string.ascii_lowercase
        self.l_e = {x: self.l_e.index(x) for x in self.l_e}
        self.l_r = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.l_r = {x: self.l_r.index(x) for x in self.l_r}
        self.u_r = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.u_r = {x: self.u_r.index(x) for x in self.u_r}
        self.u_e = string.ascii_uppercase
        self.u_e = {x: self.u_e.index(x) for x in self.u_e}
        self.punc = string.punctuation
        self.punc = {x: self.punc.index(x) for x in self.punc}
        self.blank = ' \n\t'
        self.blank = {x: self.blank.index(x) for x in self.blank}
        self.N_e = [len(self.l_e), len(self.u_e), len(self.punc), len(self.blank)]
        self.N_r = [len(self.l_r), len(self.u_r), len(self.punc), len(self.blank)]
        self.eng = [self.l_e, self.u_e, self.punc, self.blank, self.N_e]
        self.ru = [self.l_r, self.u_r, self.punc, self.blank, self.N_r]

    def case(self, symbol: str, alph: list) -> int:
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
            print("ERROR: Unknown symbol")
            sys.exit(0)

    def get_lang(self, symbol: str) -> list:
        """Determines language of a symbol"""
        if symbol in self.u_r or symbol in self.l_r:
            return self.ru
        else:
            return self.eng

    @staticmethod
    def get_key(dic, value):
        """Returns key by value from a dict"""
        for k, v in dic.items():
            if v == value:
                return k

    @staticmethod
    def check_symbol(symbol: str, alph: list) -> None:
        """Checks if the symbol was typed correctly"""
        for i in range(len(alph)):
            if symbol in alph[i]:
                return
        else:
            print("ERROR: Unknown symbol")
            sys.exit(0)
