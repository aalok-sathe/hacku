# (C) UR team @ HackU 2019

import os

from nltk.tokenize import PunktSentenceTokenizer
if not os.path.isfile(os.path.expanduser('~') + '/nltk_data/tokenizers/punkt/english.pickle'):
    nltk.download('punkt')

class TextBody:
    text = None
    sentences = None
    tokens_list = None
    sentiments = None

    def __init__(self, text=None):
        self.text = text
        spans = [*PunktSentenceTokenizer().span_tokenize(text_acc)]
        self.sentences = [text[a:b] for a, b in spans]
        self.tokens = [token for token in text.split(' ')]


    def _annotate(self):
        pass


class Email(TextBody):
    def __init__(self, )
        super()
