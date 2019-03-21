# (C) UR team @ HackU 2019

from pycorenlp import StanfordCoreNLP

class NLPBackend:
    nlp = None

    def __init__(self):
        self.nlp = StanfordCoreNLP('http://localhost:9000')


    def _annotate(self, sent):
        out = nlp.annotate(text=sent,
                           properties = {'annotators': 'sentiment',
                                         'outputFormat': 'json'})

    def get
