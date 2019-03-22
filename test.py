
import sentipriori

import json
import random
from glob import glob
import pickle
from pathlib import Path


def get_obj_for_bus(bizname):

    spp = sentipriori.SentiPrioriProc()
    path = Path(glob('./YelpData/sample_review_by_business/' + biz)[0])
    archivepath = Path('./archive') / path.stem

    print('processing for ' + str(path))


    if not archivepath.exists():
        with open(str(path), 'r') as f:
            lines = f.readlines()
            random.shuffle(lines)
            for line in lines[:128]:
                data = json.loads(line)
                try:
                    spp.add_text(data['text'])
                except TypeError:
                    continue

        with open(str(archivepath), 'wb') as f:
            pickle.dump(spp, f)

    with open(str(archivepath), 'rb') as f:
        spp = pickle.load(f)


    print(spp.ctrs['positives'].most_common(60)[8:])
    print(spp.ctrs['negatives'].most_common(60)[8:])

    return spp


if __name__ == '__main__':
    businesses = ['3kdSl5mo9dWC4clrQjEDGg',
                  '7sb2FYLS2sejZKxRYF9mtg',
                  'b2jN2mm9Wf3RcrZCgfo1cg',
                  'CRVtzesMuwHK-phmS_ojaA',
                  'kOo4ZY2UQAX4j312mzQ8mA',
                  'NZnhc2sEQy3RmzKTZnqtwQ',
                  'RXBFk3tVBxiTf3uOt9KExQ',
                  'vHz2RLtfUMVRPFmd7VBEHA',
                  'yA6dKNm_zl1ucZCnwW8ZCg',
                  'zvO-PJCpNk4fgAVUnExYAA']

    for biz in businesses:
        this_obj = get_obj_for_bus(biz)
        b64s = this_obj.plot_clouds(biz)
