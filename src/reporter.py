from typing import List, Optional
import re


class BaseReporter(object):
    pass


class Reporter(BaseReporter):
    text: str = ""

    # region private
    def _add_header(self, header: List[str]):
        header = "|".join(header) + "|\n"
        header += "| ----- | ----- | ------- |\n"
        self.text += header

    def _add_row(self, row: List[str]):
        row = "|".join(row) + "|\n"
        self.text += row

    @staticmethod
    def _get_field_from_error(error: str) -> Optional[str]:
        try:
            pattern: str = r"\'.*\'"
            field: str = re.match(pattern, error).group(0)
            return field
        except:
            return None

    # end region
    # region public
    def add_validator_name(self, validator_name: str) -> None:
        self.text += f"# {validator_name}\n"

    def add_validator_status(self, validator_status: str) -> None:
        self.text += f"### {validator_status}\n"

    def add_file(self, file: str) -> None:
        self.text += f"## {file}\n"

    def add_errors_table(self, errors_list: List[str], filename: str) -> None:
        """
        | field | what-to-do | raw_error |
        :param filename:
        :param errors_list:
        :return:
        """
        self._add_header(["Field", "What to do?", "Error log from code"])
        for error in errors_list:
            field: str = self._get_field_from_error(error)
            if field is not None:
                self._add_row([field, f"add {field} inside {filename}", error])
            else:
                self._add_row(["?", f"Better show this error for developer", error])

    def build(self) -> None:
        with open("./README.md", "w") as file:
            file.write(self.text)

    # endregion
