from dataclasses import dataclass
from typing import List


@dataclass
class teacher:
    _firstname: str
    _lastname: str

    @property
    def name(self) -> str:
        return f"{self._firstname} {self._lastname}".lower().title()

    @property
    def code(self) -> str:
        return f"{self._lastname[0]}{self._firstname[:1]}".upper()


@dataclass
class subject:
    _code: str
    _subject: str
    _teacher: object

    @property
    def code(self) -> str:
        return self._code

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def teacher(self) -> object:
        return self._teacher


@dataclass
class timings:
    _start_hour: int
    _start_min: int
    _end_hour: int
    _end_min: int

    @property
    def start(self) -> str:
        return f"{self._start_hour}:{self._start_min}"

    @property
    def end(self) -> str:
        return f"{self._end_hour}:{self.end_min}"


@dataclass
class subject_instance:
    _subject: object
    _room: str
    _times: object
    _attendance: str

    @property
    def subject(self) -> object:
        return self._subject

    @property
    def room(self) -> str:
        return self._room

    @property
    def times(self) -> object:
        return self._times

    @property
    def attendance(self) -> str:
        return self._attendance


@dataclass
class days_subjects:
    _day: str
    _subjects: List[object]

    @property
    def day(self) -> str:
        return self._day

    @property
    def subjects(self) -> List[object]:
        return self._subjects
