import json
data = {
    'kernel_size': 3,
    'sigma': 1,
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)


