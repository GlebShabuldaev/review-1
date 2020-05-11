#! ./venv/bin/python3.7
import argparse
from train import Train
from hack import Hack
from caesar import Caesar
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
    ENCODE = 1
    DECODE = -1
    TRAIN = 2
    HACK = 3


def input_text(mode):
    """Input of the text"""
    if mode == Mode.HACK:
        with open(args.model_file, "rb") as f:
            model = pickle.load(f)
            return model
    if mode == Mode.TRAIN:
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
    if mode == Mode.TRAIN:
        with open(args.model_file, "wb") as f:
            pickle.dump(text, f)
    elif args.output_file is not None:
        with open(args.output_file, "w") as f:
            f.write(text)
    else:
        print(text)

def main():
    mode = Mode[args.mode.upper()]
    word = input_text(mode)
    if mode in (Mode.ENCODE, Mode.DECODE):
        if args.cipher == 'caesar':
            write_text(Caesar(args.key).do(mode.value, word), mode)
        else:
            write_text(Vigenere().do(mode.value, word, args.key), mode)
    elif mode == Mode.TRAIN:
        write_text(Train().letter_density(word), mode)
    elif mode == Mode.HACK:
        model = input_text(mode)
        word = input_text(1)
        key = Hack().hack(model, word)
        text = Caesar(key).do(-1, word)
        write_text(text, mode)

if __name__ == '__main__': 
    main()
