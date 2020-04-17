from dataclasses import dataclass
from collections import Counter
from alphabet import Alphabet


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
        for i in range(len(text)):
            alph = Alphabet().get_lang(text[i])
            if text[i] in alph[0]:
                text_c += text[i]
        return text_c

    def letter_density(self, text: str) -> dict:
        """Letters density in the text"""
        count = self.letters_num(text)
        dic = {}
        for symbol in count.keys():
            dic[symbol] = count[symbol] / len(text)
        return dic
