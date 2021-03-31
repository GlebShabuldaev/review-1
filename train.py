from dataclasses import dataclass
from collections import Counter
from alphabet import Alphabet
from sys import exit

@dataclass
class Train:
    def letters_num(self, text: str) -> dict:
        """Counts the number of letter being in a text"""
        text = self.text_converter(text)
        count = Counter(text.lower())
        return count

    @staticmethod
    def text_converter(text: str) -> str:
        """Removes every symbol from the text except 
        for letters in the alphabet"""
        text_c = ''
        if len(text) == 0:
            print("Wrong text input")
            exit(0)
        for i in text:
            alph = Alphabet().get_lang(i)
            if i in alph[0]:
                text_c += i
        return text_c

    def letter_density(self, text: str) -> dict:
        """Letters density in the text"""
        count = self.letters_num(text)
        dic = {}
        for symbol in count.keys():
            dic[symbol] = count[symbol] / len(text)
        return dic
