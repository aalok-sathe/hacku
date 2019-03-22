# (C) UR team @ HackU 2019

import os
import sentiment
from nltk import Tree
from collections import defaultdict

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
        self.labels = [[(subtree.label(), subtree)
                       for subtree in tree.subtrees()] for tree in self.trees]
        self.sentiments = [[sentiment.getsentimentfromlabel(label)
                           for label, _ in sentlabels]
                           for sentlabels in self.labels]

    def positives(self):
        return sum([
            [(flat, prob, sent) for (sent, prob), (label, flat) in zip(sentiments, labels)
             if (sent >= 3 and prob > .2)]
            for sentiments, labels in zip(self.sentiments, self.labels)
        ], [])


    def negatives(self):
        return sum([
            [(flat, prob, sent) for (sent, prob), (label, flat) in zip(sentiments, labels)
             if (sent <= 1 and prob > .2)]
            for sentiments, labels in zip(self.sentiments, self.labels)
        ], [])


    def neutrals(self):
        return sum([
            [(flat, prob, sent) for (sent, prob), (label, flat) in zip(sentiments, labels)
             if (sent == 2 or prob <= .2)]
            for sentiments, labels in zip(self.sentiments, self.labels)
        ], [])


    def get_pos(self, treelabel):
        parts = treelabel.split('|')
        pos = parts[0]
        return pos


    def postproc(self, item):
        # if item.lower() == 'i': return False
        if len(item) <= 3: return False
        if len(item.split()) >= 6: return False
        if len(item) >= 26: return False
        return True


    def get_key_stuff(self):
        returnable = defaultdict(list)
        for functype in {'positives', 'negatives', 'neutrals'}:
            try:
                trees = getattr(self, functype)()
            except ValueError:
                continue
            for tree, prob, sent in trees:
                label = tree.label()
                pos = self.get_pos(label)
                if pos in {'ROOT', 'S', 'SBAR'}:
                    for subtree in tree.subtrees():
                        label_ = subtree.label()
                        pos_ = self.get_pos(label_)
                        if pos_ in {'NP', '@NP', 'VP', '@VP', 'NN'}:
                            returnable[functype] += [' '.join([*subtree.flatten()])]
            returnable[functype] = set(filter(self.postproc,
                                              returnable[functype]))

        return returnable

    def getsentiment(self):
        return [sentiment.overallsentiment(t) for t in self.trees]
