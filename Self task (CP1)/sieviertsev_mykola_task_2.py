class Time:
    __hours: int
    __minutes: int
    __seconds: int

    def __init__(self, hours: int, minutes: int, seconds: int):
        if self._is_correctly_hours(hours):
            self.__hours = hours
        if self._is_correctly_minutes(minutes):
            self.__minutes = minutes
        if self._is_correctly_seconds(seconds):
            self.__seconds = seconds

    @staticmethod
    def _is_correctly_hours(hours: int):
        if (hours >= 0) and (hours <= 23):
            return True
        return False

    @staticmethod
    def _is_correctly_minutes(minutes: int):
        if (minutes >= 0) and (minutes <= 59):
            return True
        return False

    @staticmethod
    def _is_correctly_seconds(seconds: int):
        if (seconds >= 0) and (seconds <= 59):
            return True
        return False

    def get_hours(self):
        return self.__hours

    def get_minutes(self):
        return self.__minutes

    def get_seconds(self):
        return self.__seconds

    def set_hours(self, hours: int):
        if self._is_correctly_hours(hours):
            self.__hours = hours

    def set_minutes(self, minutes: int):
        if self._is_correctly_minutes(minutes):
            self.__minutes = minutes

    def set_seconds(self, seconds: int):
        if self._is_correctly_seconds(seconds):
            self.__seconds = seconds

    def print_12hour_format(self):
        meridiem: str

        if 12 > self.__hours >= 0:
            meridiem = "a.m."
        elif 23 >= self.__hours >= 12:
            meridiem = "p.m."

        print(f"{self.__hours} {meridiem} {self.__minutes} minutes {self.__seconds} seconds")

    def print_24hour_format(self):
        print(f"{self.__hours} hours {self.__minutes} minutes {self.__seconds} seconds")


time_ = Time(12, 23, 45)
time_.print_24hour_format()
time_.print_12hour_format()
