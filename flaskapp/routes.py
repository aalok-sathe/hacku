from flask import jsonify, request
from glob import glob
import pickle
import random
from pathlib import Path
import json

from flaskapp import app
from flaskapp.exceptions import InvalidUsage
from namesearch import namesearch
import sentipriori





@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@app.route('/business')
def search_business():
    name = request.args.get('name', default='')
    city = request.args.get('city', default='')
    state = request.args.get('state', default='')
    return jsonify(namesearch.find_similar(name, city, state))

@app.route('/analysis')
def analyze():
    business_id = request.args.get('business_id', default=None)
    if business_id is None:
        raise InvalidUsage('business_id not supplied', status_code=400)

    analysis = get_business_analysis(business_id)
    pos_img, neg_img = analysis.plot_clouds(business_id)

    data = {
        'business_id': business_id,
        'description': 'This is bullshit',
        'images': [str(pos_img), str(neg_img)]
    }
    return jsonify(data)


def get_business_analysis(business_id):

    spp = sentipriori.SentiPrioriProc()
    path = Path(glob('./YelpData/sample_review_by_business/' + business_id)[0])
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
