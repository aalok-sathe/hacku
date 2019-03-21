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
    backend = None
    trees = None


    def __init__(self, text=None, backend=None):
        # self.nlp = sentiment.NLPBackend()
        self.text = text
        self.sentences = backend.annotate(text)['sentences']
        # spans = [*PunktSentenceTokenizer().span_tokenize(text_acc)]
        # self.sentences = [text[a:b] for a, b in spans]
        # self.tokens = [token for token in text.split(' ')]

        self.trees = [Tree.fromstring(s['sentimentTree'])
                      for s in self.sentences]
        self.labels = [[(subtree.label(), ' '.join(subtree.flatten()))
                       for subtree in tree.subtrees()] for tree in self.trees]
        self.sentiments = [[sentiment.getsentimentfromlabel(label)
                           for label, _ in sentlabels]
                           for sentlabels in self.labels]

    # def positives(self):
    #     return [[flat for (sent, prob), (label, flat) in zip(sentiments, labels) if sent >= 3 and prob > .2] for sentiments, labels in self.sentiments, self.labels]
    #
    # def negatives(self):
    #     return [[flat for (sent, prob), (label, flat) in zip(sentiments, labels) if sent <= 1 and prob > .2] for sentiments, labels in self.sentiments, self.labels]


    def getsentiment(self):
        return [sentiment.overallsentiment(t) for t in self.trees]
