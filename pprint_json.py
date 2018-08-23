import json


def load_data(filepath):

    with open(filepath) as file:
        data_from_json = json.loads(file.read())

    return data_from_json


def print_data(json_data):

    shown_data = json.dumps(json_data, indent=4, sort_keys=True)
    print(shown_data)

    return None


if __name__ == "__main__":

    dir_path = "/home/inverdat/PycharmProjects/4_json/bars.json"
    loaded_data = load_data(dir_path)
    print_data(loaded_data)
