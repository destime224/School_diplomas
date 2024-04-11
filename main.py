from __future__ import annotations
from datacls import DiplomaParametrs, PupilFullInformation, PupilInformation, DiplomaTitleLayoutParametrs, Point
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import Slot, QDate
from diploma import DiplomaLayout
from saving import Saver
from ui.main_ui import Ui_MainWindow
import sys
from datetime import date

from file_parsing import ExcelParser

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from PySide6.QtWidgets import QRadioButton


class MainWindow(QMainWindow):
    FILE_FILTERS = ("Excel (*.xlsx)",)

    def __init__(self) -> None:
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # type: ignore

        self.ali_rating = (
            self.ui.left_corner,
            self.ui.center
        )

        self.rating_transcript = (
            self.ui.full,
            self.ui.middle,
            self.ui.short
        )

        self.Z_field = (
            self.ui.per_line,
            self.ui.one,
            self.ui.no_print
        )

        self.saver = Saver("settings.ini")
        self.ui.diploma_school_name.blockCountChanged.connect(self.school_name_blocks_count_changed)
        self.ui.reset_diploma_settings.clicked.connect(self.reset_diploma_parametrs)
        self.ui.save_diploma_settings.clicked.connect(self.save_diploma_parametrs)

        self.ui.load_pupils.clicked.connect(self.load_pupils)
        self.ui.generate_diploma.clicked.connect(self.generate_diploma)
        self.ui.generate_all_diplomas.clicked.connect(self.generate_all_diplomas)
        self.ui.pupils_list.cellClicked.connect(self.cell_index_selected_from_pupils_list)
        self.ui.selected_index.valueChanged.connect(self.cell_index_selected_from_selected_index)

        self.ui.save_title_settings.clicked.connect(self.save_title_parametrs)
        self.ui.reset_title_settings.clicked.connect(self.reset_title_parametrs)

        self.restore_diploma_parametrs()
        self.restore_title_parametrs()

    def get_index_from_radio_buttons(self, t: tuple[QRadioButton, ...]) -> int:
        for i, rb in enumerate(t):
            if rb.isChecked():
                return i
        return 0
    
    def set_diploma_parametrs(self, dp: DiplomaParametrs = DiplomaParametrs()) -> None:
        self.ui.diploma_school_name.setPlainText(dp.diploma_school_name)
        self.ui.diploma_date.setDate(QDate(dp.diploma_date.year, dp.diploma_date.month, dp.diploma_date.day))
        self.ui.diploma_FST_head_of_edu.setText(dp.diploma_fst_head_of_edu)
        self.ui.diploma_print_FST.setChecked(dp.diploma_print_fst)
        self.ali_rating[dp.ali_rating].setChecked(True)
        self.rating_transcript[dp.rating_transcript].setChecked(True)
        self.Z_field[dp.z_field].setChecked(True)
        self.ui.diploma_font_size.setValue(dp.diploma_font_size)
        self.ui.diploma_adv_font_size.setValue(dp.diploma_adv_font_size)
        self.ui.diploma_FST_font_size.setValue(dp.diploma_fst_font_size)
    
    def set_title_parametrs(self, tp: DiplomaTitleLayoutParametrs = DiplomaTitleLayoutParametrs()) -> None:
        self.ui.title_date_x.setValue(tp.date.x)
        self.ui.title_date_y.setValue(tp.date.y)
        self.ui.title_year_x.setValue(tp.year.x)
        self.ui.title_year_y.setValue(tp.year.y)
        self.ui.title_school_name_x.setValue(tp.school_name.x)
        self.ui.title_school_name_y.setValue(tp.school_name.y)
        self.ui.title_head_of_edu_FST_x.setValue(tp.head_of_edu_fst.x)
        self.ui.title_head_of_edu_FST_y.setValue(tp.head_of_edu_fst.y)
        self.ui.title_pupil_FST_x.setValue(tp.pupil_fst.x)
        self.ui.title_pupil_FST_y.setValue(tp.pupil_fst.y)
        self.ui.title_qrcode_x.setValue(tp.qrcode.x)
        self.ui.title_qrcode_y.setValue(tp.qrcode.y)
        self.ui.title_image.setChecked(tp.diploma_title_image)

    def get_diploma_parametrs(self) -> DiplomaParametrs:
        return DiplomaParametrs(
            self.ui.diploma_school_name.toPlainText(),
            date(*self.ui.diploma_date.date().getDate()),
            self.ui.diploma_FST_head_of_edu.text(),
            self.ui.diploma_print_FST.isChecked(),
            self.get_index_from_radio_buttons(self.ali_rating),
            self.get_index_from_radio_buttons(self.rating_transcript),
            self.get_index_from_radio_buttons(self.Z_field),
            self.ui.diploma_font_size.value(),
            self.ui.diploma_adv_font_size.value(),
            self.ui.diploma_FST_font_size.value()
        )

    def get_title_parametrs(self) -> DiplomaTitleLayoutParametrs:
        return DiplomaTitleLayoutParametrs(
            Point(self.ui.title_date_x.value(), self.ui.title_date_y.value()),
            Point(self.ui.title_year_x.value(), self.ui.title_year_y.value()),
            Point(self.ui.title_school_name_x.value(), self.ui.title_school_name_y.value()),
            Point(self.ui.title_head_of_edu_FST_x.value(), self.ui.title_head_of_edu_FST_y.value()),
            Point(self.ui.title_pupil_FST_x.value(), self.ui.title_pupil_FST_y.value()),
            Point(self.ui.title_qrcode_x.value(), self.ui.title_qrcode_y.value()),
            self.ui.title_image.isChecked()
        )

    def get_pupil_info(self, index: int | None = None) -> PupilInformation:
        if not index:
            index = self.ui.selected_index.value()-1
        data: list[str | date]= []
        for x in range(self.ui.pupils_list.columnCount()):
            d = self.ui.pupils_list.item(index, x).text()
            if x == 3:
                d = d.split(".")
                d.reverse()
                d = "-".join(d)
                d = date.fromisoformat(d)
            data.append(d)
        return PupilInformation(*data) # type: ignore
    
    def get_full_pupil_info(self, index: int | None = None) -> PupilFullInformation:
        if not index:
            index = self.ui.selected_index.value()-1
        pupil = self.get_pupil_info(index)
        d: dict[str, int] = {}
        for x in range(self.ui.rating_list.columnCount()):
            k = self.ui.rating_list.horizontalHeaderItem(x).text()
            v = int(self.ui.rating_list.item(index, x).text())
            d[k] = v

        return PupilFullInformation(pupil.second_name, pupil.name, pupil.third_name, pupil.birthday, pupil.diploma_id, d)
    
    def drop_error_message(self, title: str, message: str) -> int:
        return QMessageBox.critical(self, title, message)

    @Slot()
    def save_diploma_parametrs(self):
        self.saver.save_diploma_parametrs(self.get_diploma_parametrs())
    
    @Slot()
    def restore_diploma_parametrs(self) -> None:
        dp = self.saver.get_diploma_parametrs()
        self.set_diploma_parametrs(dp)

    @Slot()
    def reset_diploma_parametrs(self):
        self.set_diploma_parametrs()

    @Slot()
    def save_title_parametrs(self):
        self.saver.save_title_parametrs(self.get_title_parametrs())
    
    @Slot()
    def restore_title_parametrs(self) -> None:
        dp = self.saver.get_title_parametrs()
        self.set_title_parametrs(dp)

    @Slot()
    def reset_title_parametrs(self):
        self.set_title_parametrs()

    @Slot(int)
    def school_name_blocks_count_changed(self, i: int) -> None:
        if i > 6:
            cursor = self.ui.diploma_school_name.textCursor()
            cursor.deletePreviousChar()
            self.ui.diploma_school_name.setTextCursor(cursor)

    @Slot(int, int)
    def pupils_list_cell_changed(self, row: int, col: int) -> None:
        if col <= 2:
            pupil = (
                self.ui.pupils_list.item(row,0).text(),
                self.ui.pupils_list.item(row,1).text(),
                self.ui.pupils_list.item(row,2).text()
            )
            header = QTableWidgetItem(f"{pupil[0]} {pupil[1]} {pupil[2]}")
            self.ui.rating_list.setVerticalHeaderItem(row, header)

    @Slot()
    def load_pupils(self) -> None:
        try:
            self.ui.pupils_list.cellChanged.disconnect(self.pupils_list_cell_changed)
        except RuntimeError:
            pass

        file = QFileDialog.getOpenFileName(self, caption="Выберите файл для загрузки", filter=";;".join(self.FILE_FILTERS))

        parser = ExcelParser(file[0])
        subjects = parser.get_subjects()
        pupils = parser.get_pupils_info()

        self.ui.pupils_list.setRowCount(len(pupils))
        for i, pupil in enumerate(pupils):
            t = (
                QTableWidgetItem(pupil.second_name),
                QTableWidgetItem(pupil.name),
                QTableWidgetItem(pupil.third_name),
                QTableWidgetItem(pupil.birthday.strftime("%d.%m.%Y")),
                QTableWidgetItem(pupil.diploma_id)
            )

            for j, item in enumerate(t):
                self.ui.pupils_list.setItem(i,j,item)

        full_info = parser.get_pupils_full_info()
        self.ui.rating_list.setColumnCount(len(subjects))
        self.ui.rating_list.setRowCount(len(full_info))
        for i, subject in enumerate(subjects):
            header = QTableWidgetItem(subject)
            self.ui.rating_list.setHorizontalHeaderItem(i, header)

        for i, pupil in enumerate(full_info):
            header = QTableWidgetItem(f"{pupil.second_name} {pupil.name} {pupil.third_name}")
            self.ui.rating_list.setVerticalHeaderItem(i, header)
            for j, subject in enumerate(subjects):
                rate = pupil.ratings.get(subject)
                if rate is None:
                    rate = ""
                else:
                    rate = str(rate)
                item = QTableWidgetItem(rate)
                self.ui.rating_list.setItem(i, j, item)

        self.ui.pupils_list.cellChanged.connect(self.pupils_list_cell_changed)

    @Slot(int, int)
    def cell_index_selected_from_pupils_list(self, y: int, _):
        self.ui.selected_index.setValue(y+1)

    @Slot(int)
    def cell_index_selected_from_selected_index(self, v: int):
        if v > self.ui.pupils_list.rowCount():
            self.ui.selected_index.setValue(self.ui.pupils_list.rowCount())
        else:
            self.ui.selected_index.setValue(v)

    @Slot()
    def generate_diploma(self) -> None:
        pdf = DiplomaLayout(self)
        try:
            pdf.generate_title_list(self.get_pupil_info())
        except AttributeError:
            self.drop_error_message("Не удалось распечатать.", "В списке нет выпускников, чтобы распечатать аттестат(ы).")
        pdf.save_file()

    @Slot()
    def generate_all_diplomas(self) -> None:
        pdf = DiplomaLayout(self)
        count = self.ui.pupils_list.rowCount()
        if count == 0:
            self.drop_error_message("Не удалось распечатать.", "В списке нет выпускников, чтобы распечатать аттестат(ы).")
            return
        for i in range(count):
            pdf.generate_title_list(self.get_pupil_info(i))
        pdf.save_file()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        pass