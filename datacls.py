from __future__ import annotations
from dataclasses import dataclass, field
from datetime import date

from typing import TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
    pass

@dataclass()
class DiplomaParametrs:
    diploma_school_name: str = ""
    diploma_date: date = date(2023, 1, 1)
    diploma_fst_head_of_edu: str = ""
    diploma_print_fst: bool = True
    ali_rating: int = 0
    rating_transcript: int = 2
    z_field: int = 1
    diploma_font_size: int = 11
    diploma_adv_font_size: int = 11
    diploma_fst_font_size: int = 18

@dataclass()
class Point:
    x: float = 0
    y: float = 0

@dataclass()
class DiplomaTitleLayoutParametrs:
    date: Point = field(default_factory=lambda: Point(54.85, 112.8))
    year: Point = field(default_factory=lambda: Point(153.5, 47.5))
    school_name: Point = field(default_factory=lambda: Point(142.7, 68))
    head_of_edu_fst: Point = field(default_factory=lambda: Point(190, 126.5))
    pupil_fst: Point = field(default_factory=lambda: Point(142.7, 21))
    qrcode: Point = field(default_factory=lambda: Point(9.1, 117))
    diploma_title_image: bool = False

@dataclass()
class PupilInformation:
    second_name: str
    name: str
    third_name: str
    birthday: date
    diploma_id: str

@dataclass()
class PupilFullInformation(PupilInformation):
    ratings: dict[str, int]

Parametrs = TypeVar("Parametrs", DiplomaParametrs, DiplomaTitleLayoutParametrs)
Information = TypeVar("Information", PupilInformation, PupilFullInformation)