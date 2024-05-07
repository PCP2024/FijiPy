import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

new = {
    "key1": "value1",
    "key2": "value2"
}

data.update(new)

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

print(data.keys())
