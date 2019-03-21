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
    nlp = sentiment.NLPBackend()


    def __init__(self):
        self.texts = []


    def reset(self):
        self.texts = []


    def add_text(self, txt):
        txtbdy = text.TextBody(txt, self.nlp)
        self.texts.append(txtbdy)


    def get_texts(self):
        return iter(self.texts)

_senti = SentiPrioriProc()

def add_text(*args, **kwargs):
    _senti.add_text(*args, **kwargs)

# def process_text(raw_text):
#     texts += [raw_text]

add_text('hello darkness my old friend')
it = _senti.get_texts()
tb = [*it][0]
print(tb)
print(tb.getsentiment())


if __name__ == '__main__':
    print('in main method', file=sys.stderr)
