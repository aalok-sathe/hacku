# (C) UR team @ HackU 2019

# stdlib
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# local
import text
import sentiment
# import clusters

class SentiPrioriProc:
    texts = None
    issues = None


    def __init__(self):
        texts = []


    def reset(self):
        self.texts = []


senti = SentiPrioriProc()


def process_text(raw_text):
    texts += [raw_text]


if __name__ == '__main__':
    print('in main method', file=sys.stderr)
