import json

with open('A.json', 'r') as f:
    data_a = json.load(f)

with open('B.json', 'r') as f:
    data_b = json.load(f)

# скопировать значения ключей из data_a в data_b
for key in data_a:
    if key in data_b:
        data_b[key] = data_a[key]

with open('A_formatted.json', 'w') as f:
    json.dump(data_b, f, indent=4)