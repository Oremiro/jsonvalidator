from src.factory import ValidatorFactory
from src.reader import Reader
from os import listdir

from src.reporter import Reporter


def main():
    base_path: str = "./tests/test_data/event/"
    reader: Reader = Reader()
    # i know it's insufficient, but it is test task, so for better representation, i would like to write it
    # is like run instance of validator for each file in directory
    reporter: Reporter = Reporter()
    for validator in ValidatorFactory.create_all_validators():
        reporter.add_validator_name(type(validator).__name__)
        for file in listdir(base_path):
            reporter.add_file(file)
            json_dict: dict = reader.get_dict_from_file(base_path + file)
            if validator.validate(json_dict):
                reporter.add_validator_status("valid")
            else:
                reporter.add_validator_status("invalid")
                reporter.add_errors_table(validator.get_errors(json_dict), file)
    reporter.build()


if __name__ == '__main__':
    main()
