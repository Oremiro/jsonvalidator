import json


class Schema(object):
    base_path: str
    path_name: str

    def __init__(self, path: str = None):
        if path is not None:
            self.base_path = path
        else:
            self.base_path = './tests/test_data/schema/'

    def read_schema_from_file(self) -> dict:
        with open(self.base_path + self.path_name) as file:
            result: str = file.read()
        result_dict: dict = json.loads(result)
        return result_dict


class CMarkerCreatedSchemaMixin(Schema):
    path_name: str = "cmarker_created.schema"


class LabelSelectedSchemaMixin(Schema):
    path_name: str = "label_selected.schema"


class SleepCreatedSchemaMixin(Schema):
    path_name: str = "sleep_created.schema"


class WorkoutCreatedSchemaMixin(Schema):
    path_name: str = "workout_created.schema"
