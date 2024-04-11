from __future__ import annotations
import fpdf
from segno import make_qr
from os import remove, path, mkdir

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import MainWindow
    from datacls import PupilInformation

class DiplomaLayout:
    months = (
        None,
        "января",
        "февраля",
        "марта",
        "апреля",
        "мая",
        "июня",
        "июля",
        "августа",
        "сентября",
        "октября",
        "ноября",
        "декабря",
    )

    def __init__(self, window: MainWindow) -> None:
        self.pdf = fpdf.FPDF(orientation="L", unit="mm", format="A4")
        self.pdf.set_margin(0)
        self.pdf.add_font("TimesNR","","src/fonts/Times_New_Roman.ttf")

        self.title = {"width": 220, "height": 155, "start_x": self.pdf.epw-220, "start_y": self.pdf.eph/2-155/2, "end_x": self.pdf.epw, "end_y": self.pdf.eph/2+155/2}
        self.window = window

    def generate_title_list(self, pupil: PupilInformation) -> None:
        diploma_params = self.window.get_diploma_parametrs()
        title_params = self.window.get_title_parametrs()
        self.pdf.add_page()
        self.pdf.set_font(family="TimesNR", style="", size=self.window.ui.diploma_font_size.value())
        font_height = self.pdf.font_size

        if title_params.diploma_title_image:
            self.pdf.image("src/diploma_title.png", w=self.title["width"], h=self.title["height"], x=self.title["start_x"], y=self.title["start_y"])

        d = diploma_params.diploma_date
        d_text = f"{d.day} {self.months[d.month]} {d.year} года"
        d_width = self.pdf.get_string_width(d_text)
        self.pdf.set_xy(self.title["start_x"]+title_params.date.x-d_width/2, self.title["start_y"]+title_params.date.y+font_height)
        self.pdf.cell(text=d_text, align="C")

        y = str(d.year)
        y_width = self.pdf.get_string_width(y)
        self.pdf.set_xy(self.title["start_x"]+title_params.year.x-y_width/2, self.title["start_y"]+title_params.year.y-font_height)
        self.pdf.cell(text=y, align="C")

        school_name = diploma_params.diploma_school_name
        self.pdf.set_xy(self.title["start_x"]+title_params.school_name.x, self.title["start_y"]+title_params.school_name.y-font_height*6/2)
        self.pdf.multi_cell(w=50, text=school_name, align="C") # type: ignore

        if diploma_params.diploma_print_fst:
            fst = diploma_params.diploma_fst_head_of_edu
            self.pdf.set_xy(self.title["start_x"]+title_params.head_of_edu_fst.x, self.title["start_y"]+title_params.head_of_edu_fst.y-font_height)
            self.pdf.cell(text=fst, align="L")

        self.pdf.set_font(family="TimesNR", style="", size=self.window.ui.diploma_FST_font_size.value())
        pupil_fst = f"{pupil.second_name} {pupil.name} {pupil.third_name}"
        pupil_fst_width = self.pdf.get_string_width(pupil_fst)
        self.pdf.set_xy(self.title["start_x"]+title_params.pupil_fst.x-pupil_fst_width/8, self.title["start_y"]+title_params.pupil_fst.y+font_height)
        self.pdf.multi_cell(w=pupil_fst_width*3/4, text=pupil_fst, align="C") # type: ignore

        qrcode = make_qr(f"{pupil.second_name}|{pupil.name}|{pupil.third_name}|69|{pupil.diploma_id}|{self.window.ui.diploma_date.date().toString('dd-MM-yyyy')}")
        qrcode.save("dump.png")
        self.pdf.set_xy(self.title["start_x"]+title_params.qrcode.x, self.title["start_y"]+title_params.qrcode.y)
        self.pdf.image("dump.png", w=20, h=20)
        remove("dump.png")
    
    def save_file(self) -> None:
        if not path.isdir("tests"):
            mkdir("tests")
        self.pdf.output("tests/test.pdf")