import typing
import json


class BaseReader(object):
    pass


class Reader(BaseReader):

    # region public
    def get_str_from_file(self, path: str) -> str:
        """
        Base function for getting string from file
        :param path:
        :return:
        """
        result: str = ""
        with open(path, "r") as file:
            result: str = file.read()
        return result

    def get_dict_from_file(self, path: str) -> typing.Dict:
        """
        Base function, that exptects to get valid dict object from file
        :param path:
        :return:
        """
        string_result = self.get_str_from_file(path)
        result: typing.Dict = json.loads(string_result)
        return result

    @staticmethod
    def normalize_str(string: str) -> str:
        # Haven't time to fix unicode encoding/decoding, so im going to use this crutch
        # Also now, i'm not sure its working
        dictionary: dict = json.loads(string)
        string = str(dictionary)
        string = json.dumps(string)
        return string

    # endregion
