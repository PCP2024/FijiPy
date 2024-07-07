import json


def update_json_file(file_path: str, key: str, new_value: float) -> None:
    """
    Update a json file.
    args:
        file_path (str): path to the configuration file
        key (str): key
        new_value (float): new valueconfiguration
    
    """    
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)

    # Update the specific element
    data[key] = new_value

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)