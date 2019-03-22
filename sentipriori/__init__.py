# (C) UR team @ HackU 2019

# stdlib
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
# local
import text
import sentiment
import numpy as np
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

# add_text('hello darkness my old friend')
# add_text('my computer is poop and drives me crazy when it heats up')
# add_text('I hate that you exist')
# add_text("Went here once to get my tires changed over for summer. It was wildly overpriced at $120 plus tax and they took 2 hrs to do it. Most good tire shops would have you out in half an hour. They also torqued my lug nuts so tight that I broke a wrench changing a tire later. Vehicle manufacturers have torque specification for lug nuts which these guys in their inexperience and lack of knowledge ignored. Not going back. Ever.")
add_text("Pretty good breakfast spot if you're in Las Vegas area. I'm not an egg person but i decided to give it a try since my party chose this place. I got the traditional Benny which came out to be so delicious. I checked in on yelp and got a free banana muffin which also was delicious! It wasn't dry or nasty. It was perfect. They also have a cute idea of flipping over a plastic egg to a sad face when you need something. We needed some extra tortillas and flipped our egg to a sad face and they came immediately. My plate came with a side of potatoes which tasted amazing. I'm so glad I gave this place a try! Open to trying new places now.")
for tb in _senti.get_texts():
    print(tb)
    print('positives', *tb.positives(), sep='\n')
    print()
    print('neutrals', *tb.neutrals(), sep='\n')
    print()
    print('negatives', *tb.negatives(), sep='\n')
    print('='*80)
    print(tb.get_key_stuff(), sep='\n')
    print('='*80)
    print(np.mean([(sent) for sent, prob in tb.getsentiment()]))
    print(np.mean([(sent*prob) for sent, prob in tb.getsentiment()]))
    print('='*80)


if __name__ == '__main__':
    print('in main method', file=sys.stderr)
