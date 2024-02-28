from __future__ import annotations
from configparser import ConfigParser
from os import path
from dataclasses import asdict
from datetime import date
from datacls import DiplomaParametrs, DiplomaTitleLayoutParametrs, Parametrs, Point

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    pass

class Saver:
    sections = ("DiplomaParametrs", "TitleLayoutParametrs")
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.config = ConfigParser()
        if path.isfile(file_name):
            self.config.read(file_name)
        else:
            self.config.add_section(self.sections[0])
            self.config.add_section(self.sections[1])
            d = asdict(DiplomaParametrs())
            d = self.any_to_str(d)
            t = asdict(DiplomaTitleLayoutParametrs())
            t = self.any_to_str(t)
            self.config[self.sections[0]].update(d)
            self.config[self.sections[1]].update(t)
            with open(file_name, "wt") as f:
                self.config.write(f)

    def save_parametrs(self, params: any, section: str) -> None:
        d = self.any_to_str(asdict(params))
        self.config[section].update(d)
        self.save_to_file()

    def get_parametrs(self, p: Parametrs, section: str) -> Parametrs | None:
        try:
            for k, v in self.config[section].items():
                ann = p.__annotations__[k]
                if ann == "int":
                    v = int(v)
                elif ann == "bool":
                    if v == "False":
                        v = False
                    else:
                        v = True
                elif ann == "date":
                    v = date.fromisoformat(v)
                elif ann == "Point":
                    v = v.split("|")
                    d = {}
                    for kv in v:
                        K, V = kv.split("==", 1)
                        d.update({K: float(V)})
                    v = Point(**d)
                setattr(p, k, v)
            return p
        except KeyError:
            return None
    
    def save_diploma_parametrs(self, dp: DiplomaParametrs) -> None:
        self.save_parametrs(dp, self.sections[0])
    
    def get_diploma_parametrs(self) -> DiplomaParametrs:
        p = self.get_parametrs(DiplomaParametrs(), self.sections[0])
        if p is None:
            return DiplomaParametrs()
        return p
    
    def save_title_parametrs(self, dp: DiplomaTitleLayoutParametrs) -> None:
        self.save_parametrs(dp, self.sections[1])
    
    def get_title_parametrs(self) -> DiplomaTitleLayoutParametrs:
        p = self.get_parametrs(DiplomaTitleLayoutParametrs(), self.sections[1])
        if p is None:
            return DiplomaTitleLayoutParametrs()
        return p

    def any_to_str(self, d: dict[str, any]) -> dict[str, str]:
        d = d.copy()
        for k, v in d.items():
                if type(v) == dict:
                    t = []
                    for K, V in v.items():
                        t.append(f"{K}=={V}")
                    d[k] = "|".join(t)
                else:
                    d[k] = str(v)
        return d
    
    def save_to_file(self):
        with open(self.file_name, "wt") as f:
            self.config.write(f)
        