import json

with open('../public/json/nsample.json', 'r') as f:
    data = json.load(f)

with open('../public/json/sample.json', 'w') as f:
    json.dump(list(data.keys()), f)
