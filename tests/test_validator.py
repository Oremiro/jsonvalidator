from src.reader import Reader
from src.factory import ValidatorFactory

base_path: str = "./tests/test_data/event/"


def test_validate_json_cmarker_schema() -> None:
    cmarker_json_path: str = "3ade063d-d1b9-453f-85b4-dda7bfda4711.json"
    reader: Reader = Reader()
    json_dict = reader.get_dict_from_file(base_path + cmarker_json_path)
    validator = ValidatorFactory.create_cmarker_validator()
    assert validator.validate(json_dict) is False


def test_validate_json_label_selected_schema() -> None:
    label_json_path: str = "1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json"
    reader: Reader = Reader()
    json_dict = reader.get_dict_from_file(base_path + label_json_path)
    validator = ValidatorFactory.create_label_validator()
    assert validator.validate(json_dict) is False


def test_validate_json_sleep_created_schema() -> None:
    sleep_json_path: str = "297e4dc6-07d1-420d-a5ae-e4aff3aedc19.json"
    reader: Reader = Reader()
    json_dict = reader.get_dict_from_file(base_path + sleep_json_path)
    validator = ValidatorFactory.create_sleep_validator()
    assert validator.validate(json_dict) is False


def test_validate_json_workout_created() -> None:
    """
    there is only meditation files => we aren't going to do this test
    :return:
    """
