from fuzzywuzzy import fuzz
import json


with open('YelpData/business_trimmed.json', 'r') as f:
    businesses = json.load(f)

FUZZY_LEVEL = 90  # if 2 string has partial_ratio 90 or more, consider them similar
MAX_RESULTS = 100

def find_similar(name, city='', state=''):
    name = name.lower()
    city = city.lower()
    state = state.lower()
    matches = []
    for business in businesses:
        score = similarity_score(business, name, city, state)
        if score >= FUZZY_LEVEL:
            matches.append((score, business))
    matches.sort(key=lambda x: (-x[0], x[1]['name']))
    return [business for _, business in matches[:MAX_RESULTS]]

def similarity_score(business, name, city, state):
    if (city and business['city'].lower() != city) \
        or (state and business['state'].lower() != state) \
        or len(business['name']) < len(name):
        return 0
    else:
        return fuzz.partial_ratio(business['name'].lower(), name)
