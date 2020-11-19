from abc import ABCMeta, abstractmethod
from typing import List
from .schemas import CMarkerCreatedSchemaMixin, LabelSelectedSchemaMixin, SleepCreatedSchemaMixin, \
    WorkoutCreatedSchemaMixin
from jsonschema import validate, ValidationError, Draft3Validator, Draft7Validator
from pprint import pp


class Validator(object):
    """
        Base Validator class
    """
    schema: dict = {}

    def validate(self, json_data: dict) -> bool:
        validator = Draft7Validator(self.schema)
        return validator.is_valid(json_data)

    def get_errors(self, json_data: dict) -> List[str]:
        errors: List[str] = []
        validator = Draft7Validator(self.schema)
        for error in sorted(validator.iter_errors(json_data), key=str):
            errors.append(error.message)
        return errors


class CMarkerCreatedValidator(Validator, CMarkerCreatedSchemaMixin):
    """
        CMarker Validator version
    """

    def __init__(self, path: str = None):
        super().__init__(path)
        self.schema = self.read_schema_from_file()


class LabelSelectedValidator(Validator, LabelSelectedSchemaMixin):
    """
        Label Validator version
    """

    def __init__(self, path: str = None):
        super().__init__(path)
        self.schema = self.read_schema_from_file()


class SleepCreatedValidator(Validator, SleepCreatedSchemaMixin):
    """
        Sleep Validator version
    """

    def __init__(self, path: str = None):
        super().__init__(path)
        self.schema = self.read_schema_from_file()


class WorkoutCreatedValidator(Validator, WorkoutCreatedSchemaMixin):
    """
        Workout Validator version
    """

    def __init__(self, path: str = None):
        super().__init__(path)
        self.schema = self.read_schema_from_file()
