from flask import jsonify, request

from flaskapp import app
from flaskapp.exceptions import InvalidUsage


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
    return jsonify(find_business_matches(name, city, state))

def find_business_matches(name, city, state):
    return [
        { 'business_id': 125,
          'business_name': name,
          'city': city,
          'state': state
        },
        { 'business_id': 123,
          'business_name': 'Hooter',
          'city': 'Richmond',
          'state': 'VA'
        },
        { 'business_id': 124,
          'business_name': 'Your Mom\'s Diner',
          'city': 'Richmond',
          'state': 'VA'
        }
    ]

@app.route('/analysis')
def analyze():
    business_id = request.args.get('business_id', default=None)
    if business_id is None:
        raise InvalidUsage('business_id not supplied', status_code=400)
    data = {
        'business_id': business_id,
        'description': 'This is bullshit',
        'reviews': 1000,
        'rating': 5
    }
    return jsonify(data)