# (C) UR team @ HackU 2019

import os
import sentiment
from nltk import Tree

# from nltk.tokenize import PunktSentenceTokenizer
# if not os.path.isfile(os.path.expanduser('~') + '/nltk_data/tokenizers/punkt/english.pickle'):
#     nltk.download('punkt')


class TextBody:
    text = None
    sentences = None
    tokens = None
    # sentiments = None
    nlp = None
    trees = None


    def __init__(self, text=None):
        self.nlp = sentiment.NLPBackend()
        self.text = text
        self.sentences = nlp.annotate(text)['sentences']
        # spans = [*PunktSentenceTokenizer().span_tokenize(text_acc)]
        # self.sentences = [text[a:b] for a, b in spans]
        # self.tokens = [token for token in text.split(' ')]

        self.trees = [Tree.fromtring(s) for s in self.sentences]
        self.labels = [[subtree.label(), subtree.flatten()]
                       for subtree in self.trees.subtrees()]
        self.sentiments = None
