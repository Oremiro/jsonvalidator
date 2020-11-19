from abc import ABCMeta, abstractmethod
from typing import List
from .schemas import CMarkerCreatedSchemaMixin, LabelSelectedSchemaMixin, SleepCreatedSchemaMixin, \
    WorkoutCreatedSchemaMixin
from jsonschema import validate, ValidationError

"""
Before start:
I completly understand, that control code flow with exceptions is antipattern, but it is the way jsonschema lib works:
if there is no exceptions => json is valid
"""


class Validator(object):
    """
        Base Validator class
    """
    schema: dict = {}
    errors: List[str] = []
    warnings: List[str] = []

    def validate(self, json_data: dict) -> bool:
        try:
            validate(instance=json_data, schema=self.schema)
            return True
        except Exception as e:
            self.errors.append(type(e).__name__)
            self.warnings.append(type(e).__name__)

    def report(self):
        pass


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
