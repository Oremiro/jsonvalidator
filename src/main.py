from src.factory import ValidatorFactory
from src.reader import Reader
from os import listdir


def validate_json(path: str):
    reader: Reader = Reader()
    json_dict: dict = reader.get_dict_from_file(path)
    print(path)
    for validator in ValidatorFactory.create_all_validators():
        if validator.validate(json_dict):
            print("Valid")
        else:
            print("Invalid")
    return

def main():
    base_path: str = "./tests/test_data/event/"
    for file in listdir(base_path):
        validate_json(base_path + file)


if __name__ == '__main__':
    main()
