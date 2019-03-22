
import sentipriori

import json
import random


if __name__ == '__main__':
    business1 = '7sb2FYLS2sejZKxRYF9mtg'
    business2 = 'zvO-PJCpNk4fgAVUnExYAA'

    for biz in [business2, business1]:
        print('processing for ' + biz)

        spp = sentipriori.SentiPrioriProc()
        with open('YelpData/sample_review_by_business/' + biz) as f:
            lines = f.readlines()
            random.shuffle(lines)
            for line in lines[:128]:
                data = json.loads(line)
                try:
                    spp.add_text(data['text'])
                except TypeError:
                    continue
        print(spp.ctrs['positives'].most_common(60)[10:])
        print(spp.ctrs['negatives'].most_common(60)[10:])
        spp.plot_clouds(biz)
