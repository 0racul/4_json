import json
import argparse

def load_data(filepath):

    with open(filepath) as file:
        decoded_json = json.loads(file.read())

    return decoded_json


def print_data(json_data):

    pretty_json = json.dumps(json_data, indent=4, sort_keys=True)
    print(pretty_json)


def parser_parser():
    global parser
    parser = argparse.ArgumentParser()
    pars_result = parser.parse_args()

    return vars(pars_result)


if __name__ == "__main__":

    pars_result = parser_parser()
    dir_path = pars_result.get("path_to_file")
    loaded_data = load_data(dir_path)
    print_data(loaded_data)
