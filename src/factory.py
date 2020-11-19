from .validators import CMarkerCreatedValidator, LabelSelectedValidator, SleepCreatedValidator, WorkoutCreatedValidator


class BaseFactory(object):
    pass


"""
If it was other language with interface support i've returned here interface, but i can't
But if it is duck typing, who cares?
"""


class ValidatorFactory(BaseFactory):

    @staticmethod
    def create_cmarker_validator(path: str = None) -> CMarkerCreatedValidator:
        return CMarkerCreatedValidator(path)

    @staticmethod
    def create_label_validator(path: str = None) -> LabelSelectedValidator:
        return LabelSelectedValidator(path)

    @staticmethod
    def create_sleep_validator(path: str = None) -> SleepCreatedValidator:
        return SleepCreatedValidator(path)

    @staticmethod
    def create_workout_validator(path: str = None) -> WorkoutCreatedValidator:
        return WorkoutCreatedValidator(path)
