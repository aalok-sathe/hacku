# (C) UR team @ HackU 2019

# stdlib
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from collections import Counter
from io import BytesIO
import base64

# local
import text
import sentiment
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import WordCloud as wordcloud
# import clusters

class SentiPrioriProc:
    texts = None
    issues = None
    ctrs = None
    nlp = sentiment.NLPBackend()


    def __init__(self):
        self.texts = []
        self.ctrs = {sentiment: Counter() for sentiment in ['positives',
                                                            'negatives']}


    def reset(self):
        self.texts = []


    def add_text(self, txt):
        txtbdy = text.TextBody(txt, self.nlp)
        self.texts.append(txtbdy)
        tb = self.texts[-1]
        entries = tb.get_key_stuff()
        if tb.is_negative():
            key = 'negatives'
        else:
            key = 'positives'
        self.ctrs[key].update(entries[key])


    def get_texts(self):
        return iter(self.texts)


    def plot_clouds(self, who, plot=0):
        b64s = []
        for label in ['positives', 'negatives']:
            wc = wordcloud().generate(' '.join([x for x, _ in self.ctrs[label].most_common(100)[10:]]))
            # plt.title(who + '; ' + label)
            plt.axis('off')
            plt.imshow(wc, interpolation='bilinear')
            if plot:
                plt.show()
            b64s += [plt_to_b64(plt)]
        return b64s


# def add_text(*args, **kwargs):
#     _senti.add_text(*args, **kwargs)


def plot_wordcloud(label, wc):
    # Display the generated image:
    # the matplotlib way:
    # lower max_font_size
    # wc = wordcloud(max_font_size=40).generate(text)
    plt.xlabel(label)
    plt.imshow(wc, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()
    return plt_to_b64(plt)


def plt_to_b64(pltinst):
    stringIObytes = BytesIO()
    pltinst.savefig(stringIObytes, format='jpg')
    stringIObytes.seek(0)
    base64_jpgData = base64.b64encode(stringIObytes.read())#.replace('\n', '')
    return base64_jpgData


if False:
    _senti = SentiPrioriProc()
    # def process_text(raw_text):
    #     texts += [raw_text]

    # add_text('hello darkness my old friend')
    # add_text('my computer is poop and drives me crazy when it heats up')
    # add_text('I hate that you exist')
    add_text("Went here once to get my tires changed over for summer. It was wildly overpriced at $120 plus tax and they took 2 hrs to do it. Most good tire shops would have you out in half an hour. They also torqued my lug nuts so tight that I broke a wrench changing a tire later. Vehicle manufacturers have torque specification for lug nuts which these guys in their inexperience and lack of knowledge ignored. Not going back. Ever.")
    add_text("Pretty good breakfast spot if you're in Las Vegas area. I'm not an egg person but i decided to give it a try since my party chose this place. I got the traditional Benny which came out to be so delicious. I checked in on yelp and got a free banana muffin which also was delicious! It wasn't dry or nasty. It was perfect. They also have a cute idea of flipping over a plastic egg to a sad face when you need something. We needed some extra tortillas and flipped our egg to a sad face and they came immediately. My plate came with a side of potatoes which tasted amazing. I'm so glad I gave this place a try! Open to trying new places now.")
    add_text("Taco Naco catered my husband's 40th birthday party. All I heard from the guests were: \"Omg, this food is amazing.\", \"Who made this food, it's incredible!\" and \"This salsa is the best I've ever had. I need this in my life every day!\" Food and service was top notch. Don't call anyone else, hands down, this is the Mexican food you need for your next event.")
    add_text("So Fox Sports Grill has become The Canyon Grill....new concept with live music venue, same very very disappointing food. An upscale looking place in an upscale location should serve at least half way upscale food.....I would rather eat at Chili's . It is too bad because the ambiance and viewing options are great. PLEASE change the menu, change the food quality, change the chef.")
    for tb in _senti.get_texts():
        print(tb)
        print('positives', *tb.positives(), sep='\n')
        print()
        print('neutrals', *tb.neutrals(), sep='\n')
        print()
        print('negatives', *tb.negatives(), sep='\n')
        print('='*80)
        key_stuff = tb.get_key_stuff()
        print(key_stuff, sep='\n')
        print('='*80)
        print(np.mean([(sent) for sent, prob in tb.getsentiment()]))
        print(np.mean([(sent*prob) for sent, prob in tb.getsentiment()]))
        print('='*80)

        # print(' '.join(key_stuff['positives'])[:100])

        if tb.is_negative():
            wc = wordcloud().generate(' '.join(key_stuff['negatives']))
            plot_wordcloud('negatives', wc)
        else:
            wc = wordcloud().generate(' '.join(key_stuff['positives']))
            plot_wordcloud('positives', wc)


if __name__ == '__main__':
    print('in main method', file=sys.stderr)
