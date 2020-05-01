#! ./venv/bin/python3.7
import argparse
from train import Train
from hack import Hack
from caesar import do_caesar
from vigenere import Vigenere
import pickle
from enum import Enum

parser = argparse.ArgumentParser(description='encode a code')
parser.add_argument('mode', type=str, help='Execution mode')
parser.add_argument('--cipher', type=str, help='Type of a cipher')
parser.add_argument('--key', help='A key word/number for a cipher')
parser.add_argument('-i', '--input_file', type=str, help='Input file')
parser.add_argument('-o', '--output_file', type=str, help='Output file')
parser.add_argument('--text_file', type=str, help='Text to train on')
parser.add_argument('--model_file', type=str, help='Statistics dump')
args = parser.parse_args()


class Mode(Enum):
    encode = 1
    decode = -1
    train = 2
    hack = 3


def input_text(mode):
    """Input of the text"""
    if mode == 3:
        with open(args.model_file, "rb") as f:
            model = pickle.load(f)
            return model
    if mode == 2:
        with open(args.text_file) as f:
            word = f.read()
            return word
    if args.input_file is not None:
        with open(args.input_file) as f:
            word = f.read()
            return word
    else:
        word = input()
        return word


def write_text(text, mode):
    """Writing text output"""
    if mode == 2:
        with open(args.model_file, "wb") as f:
            pickle.dump(text, f)
    elif args.output_file is not None:
        with open(args.output_file, "w") as f:
            f.write(text)
    else:
        print(text)

def main():
    mode = Mode[args.mode].value
    word = input_text(mode)
    if mode == 1 or mode == -1:
        if args.cipher == 'caesar':
            write_text(do_caesar(mode, word, args.key), mode)
        else:
            write_text(Vigenere().do_vigenere(mode, word, args.key), mode)
    elif mode == 2:
        write_text(Train().letter_density(word), mode)
    elif mode == 3:
        model = input_text(mode)
        word = input_text(1)
        key = Hack().hack(model, word)
        text = do_caesar(-1, word, key)
        write_text(text, mode)

if __name__ == '__main__': 
    main()