from src.reader import Reader
import json


def test_get_dict_from_file_json() -> None:
    reader: Reader = Reader()
    result: dict = reader.get_dict_from_file(
        "./tests/test_data/event/1eba2aa1-2acf-460d-91e6-55a8c3e3b7a3.json")
    expected_result_str: str = '{"event": "label_selected", "data": {"id": null, "rr_id": null, "labels": [{"slug": ' \
                               '"flu", "type": 2, "color": {"color": "#e83e35", "label": "stress"}, "name_en": ' \
                               '"cold/flu", "name_ru": ' \
                               '"\u043f\u0440\u043e\u0441\u0442\u0443\u0434\u0430/\u0433\u0440\u0438\u043f\u043f", ' \
                               '"category": "health-body", "type_stress": 2, "is_custom_tag": false, ' \
                               '"property_where": null, "property_arousal": null, "property_pleasure": null, ' \
                               '"property_vitality": null, "property_stability": null}], "timestamp": ' \
                               '"2020-09-09T14:07:44"}, "created_at": "2020-09-09T11:07:45.080214Z", ' \
                               '"environment_id": 2} '
    expected_result: dict = json.loads(expected_result_str)
    assert result == expected_result


def test_get_dict_from_dict_scheme() -> None:
    reader: Reader = Reader()
    result: dict = reader.get_dict_from_file(
        "./tests/test_data/schema/cmarker_created.schema")
    expected_result_str: str = '{"type": "object", "$schema": "http://json-schema.org/schema#", "required": [' \
                               '"cmarkers", "datetime", "user_id"], "properties": {"user_id": {"type": "integer"}, ' \
                               '"cmarkers": {"type": "array", "items": {"type": ["object", "string"], "required": [' \
                               '"date", "id", "slug"], "properties": {"id": {"type": "integer"}, "date": {"type": ' \
                               '"string"}, "slug": {"type": "string"}}}}, "datetime": {"type": "string"}}} '
    expected_result: dict = json.loads(expected_result_str)
    assert result == expected_result
