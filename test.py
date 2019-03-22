
import sentipriori

import json
import random
from glob import glob
import pickle
from pathlib import Path


if __name__ == '__main__':
    businesses = '7sb2FYLS2sejZKxRYF9mtg', 'zvO-PJCpNk4fgAVUnExYAA', 'v*'

    for biz in businesses:
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
        b64s = (spp.plot_clouds(str(path.stem)))
