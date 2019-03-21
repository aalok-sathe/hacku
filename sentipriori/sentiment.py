# (C) UR team @ HackU 2019

from pycorenlp import StanfordCoreNLP

class NLPBackend:
    nlp = None

    def __init__(self):
        self.nlp = StanfordCoreNLP('http://localhost:9000')


    def annotate(self, text):
        return nlp.annotate(text=sent,
                           properties = {'annotators': 'sentiment',
                                         'outputFormat': 'json'})


def getsentimentfromlabel(treelabel):
    parts = treelabel.split('|')
    sent = parts[1][10:]
    prob = parts[2][5:]
    return int(sent), float(prob)


def overallsentiment(tree):
    return getsentimentfromlabel(subtree.label())
