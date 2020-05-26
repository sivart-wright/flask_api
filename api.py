import flask
from flask import request, jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True 


houston_areas = [

#North
    {'Spring': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Woodlands': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Greenspoint': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Willowbrook': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Kingwood': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},

#South

    {'Fort Bend': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Clear Lake': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Galveston': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Kirby': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Midtown': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},

#East

    {'Northshore': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Second Ward': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Harrisburg': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Magnolia Park': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Northshore': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    
#West
    
    {'Memorial': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Katy': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Westchase': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Uptown': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    {'Spring Branch': [{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
    
#Downtown
    
     {'Downtown':[{'parks': 0}, {'schools': 0}, {'entertainment': 0}, {'home_cost': 0}]},
]


@app.route('/', methods=['GET'])
def home():
    return "<h1>Houston Neighborhoods API</h1><p>H-TOWN APP</p>"

@app.route('/houston', methods=['GET'])
def api_all():
    return jsonify(houston_areas)
app.run()