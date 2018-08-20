import json



def load_data(filepath):

    with open(filepath) as file:
        json_data = json.loads(file.read())

    return json_data

def print_data(json_data):

    file = json.dumps(json_data, indent=4, sort_keys=True)
    print(file)

    return file



if __name__ == "__main__":

    print("file path pls \n")
    dir_path = input()
    loaded_data = load_data(dir_path)
    print_data(loaded_data)





