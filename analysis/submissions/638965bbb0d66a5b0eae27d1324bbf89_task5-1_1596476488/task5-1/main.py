import flask
from flask import request
from flask import jsonify
from flask import abort
import pandas as pd
import re
from ipaddress import ip_address

df = pd.read_csv("data.csv")

# dataframe[(dataframe['Age'] == 21) & dataframe['Stream'].isin(options)]
#entry = df[(df['email'] == "ctruin1@surveymonkey.com") & (df['ip_address'] == "206.110.220.40")]
#details = entry[['first_name', 'last_name', 'gender']]
#result = details.to_dict('index')[1]
#print(result)





app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome"


@app.route('/query', methods=['GET'])
def query():
    email = request.args.get('email')
    ip = request.args.get('ip')

    if not re.match(re.compile(".+@.+[.].{2,}"), email):
        abort(400)
    try:
        ip_address(ip)
    except:
        abort(400)

    entry = df[(df['email'] == email) & (df['ip_address'] == ip)]
    details = entry[['first_name', 'last_name', 'gender']]
    result = details.to_dict('index')
    try:
        extracted_result = result[0]
    except:
        abort(404)
    return jsonify(extracted_result)


app.run(host='127.0.0.1', port='8000', debug=True)


