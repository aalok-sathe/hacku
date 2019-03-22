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
    pos_img = pos_img.decode('UTF-8')
    neg_img = neg_img.decode('UTF-8')

    pos_words = analysis.ctrs['positives'].most_common(60)
    neg_words = analysis.ctrs['negatives'].most_common(60)
    pos_words = [(word, score/pos_words[0][1]) for word, score in pos_words]
    neg_words = [(word, score/neg_words[0][1]) for word, score in neg_words]

    fig, ax = plt.subplots()
    # Example data

    bar_plots = []
    for wordlist, color in [(pos_words, 'cyan'), (neg_words, 'red')]:
        y_pos = np.arange(len(wordlist))
        scores = [score for word, score in wordlist]
        ax.barh(y_pos, scores, align='center', color=color, ecolor='black')
        ax.set_yticks(y_pos)
        ax.set_yticklabels([word for word, score in wordlist])
        ax.invert_yaxis()  # labels read top-to-bottom
        ax.set_xlabel('Salience')
        # ax.set_title('')
        b64_img = plt_to_b64(plt)
        bar_plots.append(b64_img.decode('UTF-8'))


    data = {
        'business_id': business_id,
        'images': [pos_img, neg_img],
        'bar_plots': [*bar_plots],
        'keywords': [pos_words, neg_words],
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

    return spp
