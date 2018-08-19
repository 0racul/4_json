import json


def load_data(filepath):

    with open(filepath) as file:
        temp_inf = json.loads(file.read())

    with open("pretty.json", "w") as good_file:
        json.dump(temp_inf, good_file, indent=5, encoding="utf-8")

    return file



if __name__ == '__main__':

    print("file path pls \n")
    dir_path = input()
    loaded_data = load_data(dir_path)





