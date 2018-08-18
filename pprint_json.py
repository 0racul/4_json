import json


def load_data(filepath):

    with open(filepath) as f:

        json.loads(f.read())

    with open("pretty.json", "w") as g:

        json.dump(f, g, indent=5)

    return f


print("file path pls \n")

dir_path = input()

loaded_data = load_data(dir_path)





