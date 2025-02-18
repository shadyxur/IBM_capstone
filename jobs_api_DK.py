#Downloading Json data

import requests
import flask
from flask import request, jsonify
import re
import json

# Step 1: Download the JSON file
url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/module%201/Accessing%20Data%20Using%20APIs/jobs.json'
response = requests.get(url)

# Save the file locally
with open('jobs.json', 'wb') as file:
    file.write(response.content)

print("Download complete!")

# Step 2: Define the Flask application and use the downloaded JSON file
def get_data(key, value, current):
    results = []
    pattern_dict = {
        'C': '(C)',
        'C++': '(C\\+\\+)',
        'Java': '(Java)',
        'C#': '(C\\#)',
        'Python': '(Python)',
        'Scala': '(Scala)',
        'Oracle': '(Oracle)',
        'SQL Server': '(SQL Server)',
        'MySQL Server': '(MySQL Server)',
        'PostgreSQL': '(PostgreSQL)',
        'MongoDB': '(MongoDB)',
        'JavaScript': '(JavaScript)',
        'Los Angeles': '(Los Angeles)',
        'New York': '(New York)',
        'San Francisco': '(San Francisco)',
        'Washington DC': '(Washington DC)',
        'Seattle': '(Seattle)',
        'Austin': '(Austin)',
        'Detroit': '(Detroit)',
    }
    for rec in current:
        if re.search(pattern_dict[value], rec[key]) is not None:
            results.append(rec)
    return results

app = flask.Flask(__name__)

data = None
with open('jobs.json', encoding='utf-8') as f:
    data = json.load(f)

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Welcome to flask JOB search API</h1>'''

@app.route('/data/all', methods=['GET'])
def api_all():
    return jsonify(data)

@app.route('/data', methods=['GET'])
def api_id():
    res = None
    for req in request.args:
        if req == 'Job Title':
            key = 'Job Title'
        elif req == 'Job Experience Required':
            key = 'Job Experience Required'
        elif req == 'Key Skills':
            key = 'Key Skills'
        elif req == 'Role Category':
            key = 'Role Category'
        elif req == 'Location':
            key = 'Location'
        elif req == 'Functional Area':
            key = 'Functional Area'
        elif req == 'Industry':
            key = 'Industry'
        elif req == 'Role':
            key = 'Role'
        elif req == 'id':
            key = 'id'
        else:
            pass

        value = request.args[key]
        if res is None:
            res = get_data(key, value, data)
        else:
            res = get_data(key, value, res)

    return jsonify(res)

if __name__ == '__main__':
    app.run()
