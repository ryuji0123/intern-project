import json

ref = {}

for i in range(16):
    ref[i] = i * 100


with open('./public/json/sample.json', 'w') as f:
    json.dump(ref, f)
