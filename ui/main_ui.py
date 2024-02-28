# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QDateEdit, QDoubleSpinBox,
    QFormLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 572)
        MainWindow.setMinimumSize(QSize(1200, 572))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.layout = QTabWidget(self.centralwidget)
        self.layout.setObjectName(u"layout")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.layout.sizePolicy().hasHeightForWidth())
        self.layout.setSizePolicy(sizePolicy)
        self.layout.setTabPosition(QTabWidget.North)
        self.diploma_settings = QWidget()
        self.diploma_settings.setObjectName(u"diploma_settings")
        self.verticalLayout_5 = QVBoxLayout(self.diploma_settings)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.school_name_label = QLabel(self.diploma_settings)
        self.school_name_label.setObjectName(u"school_name_label")
        self.school_name_label.setScaledContents(False)
        self.school_name_label.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.school_name_label)

        self.verticalSpacer_2 = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Maximum)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.diploma_school_name = QPlainTextEdit(self.diploma_settings)
        self.diploma_school_name.setObjectName(u"diploma_school_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.diploma_school_name.sizePolicy().hasHeightForWidth())
        self.diploma_school_name.setSizePolicy(sizePolicy1)
        self.diploma_school_name.setMaximumSize(QSize(16777215, 130))
        font1 = QFont()
        font1.setPointSize(11)
        self.diploma_school_name.setFont(font1)
        self.diploma_school_name.setAutoFillBackground(False)
        self.diploma_school_name.setLineWidth(1)
        self.diploma_school_name.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.diploma_school_name.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.diploma_school_name.setLineWrapMode(QPlainTextEdit.NoWrap)

        self.horizontalLayout_7.addWidget(self.diploma_school_name)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.diploma_date_label = QLabel(self.diploma_settings)
        self.diploma_date_label.setObjectName(u"diploma_date_label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.diploma_date_label)

        self.diploma_date = QDateEdit(self.diploma_settings)
        self.diploma_date.setObjectName(u"diploma_date")
        self.diploma_date.setDate(QDate(2023, 1, 1))

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.diploma_date)


        self.verticalLayout_5.addLayout(self.formLayout_2)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.FST_head_of_edu_label = QLabel(self.diploma_settings)
        self.FST_head_of_edu_label.setObjectName(u"FST_head_of_edu_label")

        self.verticalLayout.addWidget(self.FST_head_of_edu_label)

        self.diploma_FST_head_of_edu = QLineEdit(self.diploma_settings)
        self.diploma_FST_head_of_edu.setObjectName(u"diploma_FST_head_of_edu")

        self.verticalLayout.addWidget(self.diploma_FST_head_of_edu)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.diploma_print_FST = QCheckBox(self.diploma_settings)
        self.diploma_print_FST.setObjectName(u"diploma_print_FST")
        self.diploma_print_FST.setChecked(True)

        self.horizontalLayout_10.addWidget(self.diploma_print_FST)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ali_rating = QGroupBox(self.diploma_settings)
        self.ali_rating.setObjectName(u"ali_rating")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ali_rating.sizePolicy().hasHeightForWidth())
        self.ali_rating.setSizePolicy(sizePolicy2)
        self.ali_rating.setMinimumSize(QSize(0, 50))
        self.ali_rating.setLayoutDirection(Qt.LeftToRight)
        self.ali_rating.setFlat(False)
        self.horizontalLayout_4 = QHBoxLayout(self.ali_rating)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.left_corner = QRadioButton(self.ali_rating)
        self.left_corner.setObjectName(u"left_corner")
        self.left_corner.setChecked(True)

        self.horizontalLayout_4.addWidget(self.left_corner)

        self.center = QRadioButton(self.ali_rating)
        self.center.setObjectName(u"center")

        self.horizontalLayout_4.addWidget(self.center)


        self.verticalLayout_2.addWidget(self.ali_rating)

        self.rating_transcript = QGroupBox(self.diploma_settings)
        self.rating_transcript.setObjectName(u"rating_transcript")
        sizePolicy2.setHeightForWidth(self.rating_transcript.sizePolicy().hasHeightForWidth())
        self.rating_transcript.setSizePolicy(sizePolicy2)
        self.rating_transcript.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.rating_transcript)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.full = QRadioButton(self.rating_transcript)
        self.full.setObjectName(u"full")

        self.horizontalLayout_3.addWidget(self.full)

        self.middle = QRadioButton(self.rating_transcript)
        self.middle.setObjectName(u"middle")
        self.middle.setChecked(False)

        self.horizontalLayout_3.addWidget(self.middle)

        self.short = QRadioButton(self.rating_transcript)
        self.short.setObjectName(u"short")
        self.short.setChecked(True)

        self.horizontalLayout_3.addWidget(self.short)


        self.verticalLayout_2.addWidget(self.rating_transcript)

        self.Z_field = QGroupBox(self.diploma_settings)
        self.Z_field.setObjectName(u"Z_field")
        sizePolicy2.setHeightForWidth(self.Z_field.sizePolicy().hasHeightForWidth())
        self.Z_field.setSizePolicy(sizePolicy2)
        self.Z_field.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.Z_field)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.per_line = QRadioButton(self.Z_field)
        self.per_line.setObjectName(u"per_line")

        self.horizontalLayout_2.addWidget(self.per_line)

        self.one = QRadioButton(self.Z_field)
        self.one.setObjectName(u"one")
        self.one.setCheckable(True)
        self.one.setChecked(True)

        self.horizontalLayout_2.addWidget(self.one)

        self.no_print = QRadioButton(self.Z_field)
        self.no_print.setObjectName(u"no_print")

        self.horizontalLayout_2.addWidget(self.no_print)


        self.verticalLayout_2.addWidget(self.Z_field)


        self.horizontalLayout_9.addLayout(self.verticalLayout_2)

        self.font = QGroupBox(self.diploma_settings)
        self.font.setObjectName(u"font")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.font.sizePolicy().hasHeightForWidth())
        self.font.setSizePolicy(sizePolicy3)
        self.formLayout = QFormLayout(self.font)
        self.formLayout.setObjectName(u"formLayout")
        self.font_size_label = QLabel(self.font)
        self.font_size_label.setObjectName(u"font_size_label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.font_size_label)

        self.diploma_font_size = QSpinBox(self.font)
        self.diploma_font_size.setObjectName(u"diploma_font_size")
        self.diploma_font_size.setValue(11)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.diploma_font_size)

        self.adv_font_size_label = QLabel(self.font)
        self.adv_font_size_label.setObjectName(u"adv_font_size_label")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.adv_font_size_label)

        self.diploma_adv_font_size = QSpinBox(self.font)
        self.diploma_adv_font_size.setObjectName(u"diploma_adv_font_size")
        self.diploma_adv_font_size.setValue(11)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.diploma_adv_font_size)

        self.FST_font_size_label = QLabel(self.font)
        self.FST_font_size_label.setObjectName(u"FST_font_size_label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.FST_font_size_label)

        self.diploma_FST_font_size = QSpinBox(self.font)
        self.diploma_FST_font_size.setObjectName(u"diploma_FST_font_size")
        self.diploma_FST_font_size.setValue(18)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.diploma_FST_font_size)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_5)


        self.horizontalLayout_9.addWidget(self.font)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.reset_diploma_settings = QPushButton(self.diploma_settings)
        self.reset_diploma_settings.setObjectName(u"reset_diploma_settings")

        self.horizontalLayout.addWidget(self.reset_diploma_settings)

        self.save_diploma_settings = QPushButton(self.diploma_settings)
        self.save_diploma_settings.setObjectName(u"save_diploma_settings")

        self.horizontalLayout.addWidget(self.save_diploma_settings)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.layout.addTab(self.diploma_settings, "")
        self.pupils = QWidget()
        self.pupils.setObjectName(u"pupils")
        self.verticalLayout_10 = QVBoxLayout(self.pupils)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.groupBox = QGroupBox(self.pupils)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pupils_list = QTableWidget(self.groupBox)
        if (self.pupils_list.columnCount() < 5):
            self.pupils_list.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.pupils_list.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.pupils_list.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.pupils_list.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.pupils_list.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.pupils_list.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.pupils_list.setObjectName(u"pupils_list")
        self.pupils_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.pupils_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.pupils_list.horizontalHeader().setCascadingSectionResizes(False)
        self.pupils_list.horizontalHeader().setMinimumSectionSize(50)
        self.pupils_list.horizontalHeader().setDefaultSectionSize(90)
        self.pupils_list.horizontalHeader().setProperty("showSortIndicator", False)
        self.pupils_list.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_6.addWidget(self.pupils_list)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.delete_pupil = QPushButton(self.groupBox)
        self.delete_pupil.setObjectName(u"delete_pupil")

        self.horizontalLayout_5.addWidget(self.delete_pupil)

        self.create_pupil = QPushButton(self.groupBox)
        self.create_pupil.setObjectName(u"create_pupil")

        self.horizontalLayout_5.addWidget(self.create_pupil)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout_10.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.pupils)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy2.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy2)
        self.verticalLayout_9 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)

        self.horizontalLayout_11.addWidget(self.label)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy5)

        self.horizontalLayout_11.addWidget(self.comboBox)


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)

        self.horizontalLayout_14.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.groupBox_2)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy5.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy5)
        self.lineEdit.setMaximumSize(QSize(37, 16777215))
        self.lineEdit.setMaxLength(1)
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_14.addWidget(self.lineEdit)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.verticalSpacer_7 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_7)


        self.horizontalLayout_13.addLayout(self.verticalLayout_7)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)

        self.horizontalLayout_12.addWidget(self.label_3)

        self.selected_index = QSpinBox(self.groupBox_2)
        self.selected_index.setObjectName(u"selected_index")
        sizePolicy5.setHeightForWidth(self.selected_index.sizePolicy().hasHeightForWidth())
        self.selected_index.setSizePolicy(sizePolicy5)
        self.selected_index.setFrame(True)
        self.selected_index.setAlignment(Qt.AlignCenter)
        self.selected_index.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.selected_index.setKeyboardTracking(True)
        self.selected_index.setMinimum(1)
        self.selected_index.setMaximum(9999)
        self.selected_index.setSingleStep(1)

        self.horizontalLayout_12.addWidget(self.selected_index)


        self.verticalLayout_8.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_6 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.MinimumExpanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.horizontalSpacer_4 = QSpacerItem(16, 48, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_13)


        self.verticalLayout_10.addWidget(self.groupBox_2)

        self.verticalSpacer_4 = QSpacerItem(20, 130, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_10.addItem(self.verticalSpacer_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.generate_all_diplomas = QPushButton(self.pupils)
        self.generate_all_diplomas.setObjectName(u"generate_all_diplomas")

        self.horizontalLayout_6.addWidget(self.generate_all_diplomas)

        self.generate_diploma = QPushButton(self.pupils)
        self.generate_diploma.setObjectName(u"generate_diploma")

        self.horizontalLayout_6.addWidget(self.generate_diploma)

        self.clear_pupils = QPushButton(self.pupils)
        self.clear_pupils.setObjectName(u"clear_pupils")

        self.horizontalLayout_6.addWidget(self.clear_pupils)

        self.load_pupils = QPushButton(self.pupils)
        self.load_pupils.setObjectName(u"load_pupils")

        self.horizontalLayout_6.addWidget(self.load_pupils)


        self.verticalLayout_10.addLayout(self.horizontalLayout_6)

        self.layout.addTab(self.pupils, "")
        self.layout_params = QWidget()
        self.layout_params.setObjectName(u"layout_params")
        self.verticalLayout_12 = QVBoxLayout(self.layout_params)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.groupBox_3 = QGroupBox(self.layout_params)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_11 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.groupBox_4 = QGroupBox(self.groupBox_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy2.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy2)
        self.formLayout_17 = QFormLayout(self.groupBox_4)
        self.formLayout_17.setObjectName(u"formLayout_17")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_17.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        sizePolicy4.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy4)

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.title_date_x = QDoubleSpinBox(self.groupBox_4)
        self.title_date_x.setObjectName(u"title_date_x")
        sizePolicy5.setHeightForWidth(self.title_date_x.sizePolicy().hasHeightForWidth())
        self.title_date_x.setSizePolicy(sizePolicy5)
        self.title_date_x.setDecimals(1)
        self.title_date_x.setMaximum(220.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.title_date_x)


        self.horizontalLayout_15.addLayout(self.formLayout_3)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.title_date_y = QDoubleSpinBox(self.groupBox_4)
        self.title_date_y.setObjectName(u"title_date_y")
        sizePolicy5.setHeightForWidth(self.title_date_y.sizePolicy().hasHeightForWidth())
        self.title_date_y.setSizePolicy(sizePolicy5)
        self.title_date_y.setDecimals(1)
        self.title_date_y.setMaximum(220.000000000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.title_date_y)


        self.horizontalLayout_15.addLayout(self.formLayout_4)


        self.formLayout_17.setLayout(0, QFormLayout.FieldRole, self.horizontalLayout_15)

        self.label_11 = QLabel(self.groupBox_4)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_17.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        sizePolicy4.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy4)

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.title_year_x = QDoubleSpinBox(self.groupBox_4)
        self.title_year_x.setObjectName(u"title_year_x")
        sizePolicy5.setHeightForWidth(self.title_year_x.sizePolicy().hasHeightForWidth())
        self.title_year_x.setSizePolicy(sizePolicy5)
        self.title_year_x.setDecimals(1)
        self.title_year_x.setMaximum(220.000000000000000)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.title_year_x)


        self.horizontalLayout_17.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.label_10 = QLabel(self.groupBox_4)
        self.label_10.setObjectName(u"label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.title_year_y = QDoubleSpinBox(self.groupBox_4)
        self.title_year_y.setObjectName(u"title_year_y")
        sizePolicy5.setHeightForWidth(self.title_year_y.sizePolicy().hasHeightForWidth())
        self.title_year_y.setSizePolicy(sizePolicy5)
        self.title_year_y.setDecimals(1)
        self.title_year_y.setMaximum(220.000000000000000)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.title_year_y)


        self.horizontalLayout_17.addLayout(self.formLayout_8)


        self.formLayout_17.setLayout(1, QFormLayout.FieldRole, self.horizontalLayout_17)

        self.label_14 = QLabel(self.groupBox_4)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_17.setWidget(2, QFormLayout.LabelRole, self.label_14)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.formLayout_9 = QFormLayout()
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.label_12 = QLabel(self.groupBox_4)
        self.label_12.setObjectName(u"label_12")
        sizePolicy4.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy4)

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.title_school_name_x = QDoubleSpinBox(self.groupBox_4)
        self.title_school_name_x.setObjectName(u"title_school_name_x")
        sizePolicy5.setHeightForWidth(self.title_school_name_x.sizePolicy().hasHeightForWidth())
        self.title_school_name_x.setSizePolicy(sizePolicy5)
        self.title_school_name_x.setDecimals(1)
        self.title_school_name_x.setMaximum(220.000000000000000)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.title_school_name_x)


        self.horizontalLayout_18.addLayout(self.formLayout_9)

        self.formLayout_10 = QFormLayout()
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.label_13 = QLabel(self.groupBox_4)
        self.label_13.setObjectName(u"label_13")
        sizePolicy6.setHeightForWidth(self.label_13.sizePolicy().hasHeightForWidth())
        self.label_13.setSizePolicy(sizePolicy6)

        self.formLayout_10.setWidget(0, QFormLayout.LabelRole, self.label_13)

        self.title_school_name_y = QDoubleSpinBox(self.groupBox_4)
        self.title_school_name_y.setObjectName(u"title_school_name_y")
        sizePolicy5.setHeightForWidth(self.title_school_name_y.sizePolicy().hasHeightForWidth())
        self.title_school_name_y.setSizePolicy(sizePolicy5)
        self.title_school_name_y.setDecimals(1)
        self.title_school_name_y.setMaximum(220.000000000000000)

        self.formLayout_10.setWidget(0, QFormLayout.FieldRole, self.title_school_name_y)


        self.horizontalLayout_18.addLayout(self.formLayout_10)


        self.formLayout_17.setLayout(2, QFormLayout.FieldRole, self.horizontalLayout_18)

        self.label_17 = QLabel(self.groupBox_4)
        self.label_17.setObjectName(u"label_17")

        self.formLayout_17.setWidget(3, QFormLayout.LabelRole, self.label_17)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.formLayout_11 = QFormLayout()
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.label_15 = QLabel(self.groupBox_4)
        self.label_15.setObjectName(u"label_15")
        sizePolicy4.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy4)

        self.formLayout_11.setWidget(0, QFormLayout.LabelRole, self.label_15)

        self.title_head_of_edu_FST_x = QDoubleSpinBox(self.groupBox_4)
        self.title_head_of_edu_FST_x.setObjectName(u"title_head_of_edu_FST_x")
        sizePolicy5.setHeightForWidth(self.title_head_of_edu_FST_x.sizePolicy().hasHeightForWidth())
        self.title_head_of_edu_FST_x.setSizePolicy(sizePolicy5)
        self.title_head_of_edu_FST_x.setDecimals(1)
        self.title_head_of_edu_FST_x.setMaximum(220.000000000000000)

        self.formLayout_11.setWidget(0, QFormLayout.FieldRole, self.title_head_of_edu_FST_x)


        self.horizontalLayout_19.addLayout(self.formLayout_11)

        self.formLayout_12 = QFormLayout()
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.label_16 = QLabel(self.groupBox_4)
        self.label_16.setObjectName(u"label_16")
        sizePolicy6.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy6)

        self.formLayout_12.setWidget(0, QFormLayout.LabelRole, self.label_16)

        self.title_head_of_edu_FST_y = QDoubleSpinBox(self.groupBox_4)
        self.title_head_of_edu_FST_y.setObjectName(u"title_head_of_edu_FST_y")
        sizePolicy5.setHeightForWidth(self.title_head_of_edu_FST_y.sizePolicy().hasHeightForWidth())
        self.title_head_of_edu_FST_y.setSizePolicy(sizePolicy5)
        self.title_head_of_edu_FST_y.setDecimals(1)
        self.title_head_of_edu_FST_y.setMaximum(220.000000000000000)

        self.formLayout_12.setWidget(0, QFormLayout.FieldRole, self.title_head_of_edu_FST_y)


        self.horizontalLayout_19.addLayout(self.formLayout_12)


        self.formLayout_17.setLayout(3, QFormLayout.FieldRole, self.horizontalLayout_19)

        self.label_20 = QLabel(self.groupBox_4)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_17.setWidget(4, QFormLayout.LabelRole, self.label_20)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.formLayout_13 = QFormLayout()
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.label_18 = QLabel(self.groupBox_4)
        self.label_18.setObjectName(u"label_18")
        sizePolicy4.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy4)

        self.formLayout_13.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.title_pupil_FST_x = QDoubleSpinBox(self.groupBox_4)
        self.title_pupil_FST_x.setObjectName(u"title_pupil_FST_x")
        sizePolicy5.setHeightForWidth(self.title_pupil_FST_x.sizePolicy().hasHeightForWidth())
        self.title_pupil_FST_x.setSizePolicy(sizePolicy5)
        self.title_pupil_FST_x.setDecimals(1)
        self.title_pupil_FST_x.setMaximum(220.000000000000000)

        self.formLayout_13.setWidget(0, QFormLayout.FieldRole, self.title_pupil_FST_x)


        self.horizontalLayout_20.addLayout(self.formLayout_13)

        self.formLayout_14 = QFormLayout()
        self.formLayout_14.setObjectName(u"formLayout_14")
        self.label_19 = QLabel(self.groupBox_4)
        self.label_19.setObjectName(u"label_19")
        sizePolicy6.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy6)

        self.formLayout_14.setWidget(0, QFormLayout.LabelRole, self.label_19)

        self.title_pupil_FST_y = QDoubleSpinBox(self.groupBox_4)
        self.title_pupil_FST_y.setObjectName(u"title_pupil_FST_y")
        sizePolicy5.setHeightForWidth(self.title_pupil_FST_y.sizePolicy().hasHeightForWidth())
        self.title_pupil_FST_y.setSizePolicy(sizePolicy5)
        self.title_pupil_FST_y.setDecimals(1)
        self.title_pupil_FST_y.setMaximum(220.000000000000000)

        self.formLayout_14.setWidget(0, QFormLayout.FieldRole, self.title_pupil_FST_y)


        self.horizontalLayout_20.addLayout(self.formLayout_14)


        self.formLayout_17.setLayout(4, QFormLayout.FieldRole, self.horizontalLayout_20)

        self.label_23 = QLabel(self.groupBox_4)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_17.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.formLayout_15 = QFormLayout()
        self.formLayout_15.setObjectName(u"formLayout_15")
        self.label_21 = QLabel(self.groupBox_4)
        self.label_21.setObjectName(u"label_21")
        sizePolicy4.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy4)

        self.formLayout_15.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.title_qrcode_x = QDoubleSpinBox(self.groupBox_4)
        self.title_qrcode_x.setObjectName(u"title_qrcode_x")
        sizePolicy5.setHeightForWidth(self.title_qrcode_x.sizePolicy().hasHeightForWidth())
        self.title_qrcode_x.setSizePolicy(sizePolicy5)
        self.title_qrcode_x.setDecimals(1)
        self.title_qrcode_x.setMaximum(220.000000000000000)

        self.formLayout_15.setWidget(0, QFormLayout.FieldRole, self.title_qrcode_x)


        self.horizontalLayout_21.addLayout(self.formLayout_15)

        self.formLayout_16 = QFormLayout()
        self.formLayout_16.setObjectName(u"formLayout_16")
        self.label_22 = QLabel(self.groupBox_4)
        self.label_22.setObjectName(u"label_22")
        sizePolicy6.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy6)

        self.formLayout_16.setWidget(0, QFormLayout.LabelRole, self.label_22)

        self.title_qrcode_y = QDoubleSpinBox(self.groupBox_4)
        self.title_qrcode_y.setObjectName(u"title_qrcode_y")
        sizePolicy5.setHeightForWidth(self.title_qrcode_y.sizePolicy().hasHeightForWidth())
        self.title_qrcode_y.setSizePolicy(sizePolicy5)
        self.title_qrcode_y.setDecimals(1)
        self.title_qrcode_y.setMaximum(220.000000000000000)

        self.formLayout_16.setWidget(0, QFormLayout.FieldRole, self.title_qrcode_y)


        self.horizontalLayout_21.addLayout(self.formLayout_16)


        self.formLayout_17.setLayout(5, QFormLayout.FieldRole, self.horizontalLayout_21)


        self.verticalLayout_11.addWidget(self.groupBox_4)

        self.title_image = QCheckBox(self.groupBox_3)
        self.title_image.setObjectName(u"title_image")

        self.verticalLayout_11.addWidget(self.title_image)


        self.verticalLayout_12.addWidget(self.groupBox_3)

        self.verticalSpacer_8 = QSpacerItem(20, 207, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_8)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_5)

        self.reset_title_settings = QPushButton(self.layout_params)
        self.reset_title_settings.setObjectName(u"reset_title_settings")

        self.horizontalLayout_22.addWidget(self.reset_title_settings)

        self.save_title_settings = QPushButton(self.layout_params)
        self.save_title_settings.setObjectName(u"save_title_settings")

        self.horizontalLayout_22.addWidget(self.save_title_settings)


        self.verticalLayout_12.addLayout(self.horizontalLayout_22)

        self.layout.addTab(self.layout_params, "")

        self.horizontalLayout_8.addWidget(self.layout)

        self.rating_list = QTableWidget(self.centralwidget)
        self.rating_list.setObjectName(u"rating_list")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.rating_list.sizePolicy().hasHeightForWidth())
        self.rating_list.setSizePolicy(sizePolicy7)
        self.rating_list.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.rating_list.setSelectionMode(QAbstractItemView.SingleSelection)
        self.rating_list.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.rating_list.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.horizontalLayout_8.addWidget(self.rating_list)

        MainWindow.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.school_name_label.setBuddy(self.diploma_school_name)
        self.diploma_date_label.setBuddy(self.diploma_date)
        self.FST_head_of_edu_label.setBuddy(self.diploma_FST_head_of_edu)
        self.font_size_label.setBuddy(self.diploma_font_size)
        self.adv_font_size_label.setBuddy(self.diploma_adv_font_size)
        self.FST_font_size_label.setBuddy(self.diploma_FST_font_size)
        self.label.setBuddy(self.comboBox)
        self.label_2.setBuddy(self.lineEdit)
        self.label_3.setBuddy(self.selected_index)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.diploma_school_name, self.diploma_date)
        QWidget.setTabOrder(self.diploma_date, self.diploma_FST_head_of_edu)
        QWidget.setTabOrder(self.diploma_FST_head_of_edu, self.left_corner)
        QWidget.setTabOrder(self.left_corner, self.center)
        QWidget.setTabOrder(self.center, self.full)
        QWidget.setTabOrder(self.full, self.middle)
        QWidget.setTabOrder(self.middle, self.short)
        QWidget.setTabOrder(self.short, self.per_line)
        QWidget.setTabOrder(self.per_line, self.one)
        QWidget.setTabOrder(self.one, self.no_print)
        QWidget.setTabOrder(self.no_print, self.diploma_font_size)
        QWidget.setTabOrder(self.diploma_font_size, self.diploma_adv_font_size)
        QWidget.setTabOrder(self.diploma_adv_font_size, self.diploma_FST_font_size)
        QWidget.setTabOrder(self.diploma_FST_font_size, self.reset_diploma_settings)
        QWidget.setTabOrder(self.reset_diploma_settings, self.save_diploma_settings)

        self.retranslateUi(MainWindow)
        self.diploma_print_FST.toggled.connect(self.diploma_FST_head_of_edu.setEnabled)

        self.layout.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Diploma", None))
        self.school_name_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0435 \u043d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0443\u0447\u0435\u0431\u043d\u043e\u0433\u043e \u0437\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u044f", None))
        self.diploma_school_name.setPlainText("")
        self.diploma_date_label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438 \u0430\u0442\u0442\u0435\u0441\u0442\u0430\u0442\u0430", None))
        self.FST_head_of_edu_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e (\u0418\u043d\u0438\u0446\u0438\u0430\u043b) \u0440\u0443\u043a\u043e\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044f \u043e\u0431\u0440. \u0443\u0447\u0440\u0435\u0436\u0434\u0435\u043d\u0438\u044f", None))
        self.diploma_FST_head_of_edu.setText("")
        self.diploma_print_FST.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0424\u0418\u041e", None))
        self.ali_rating.setTitle(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0440\u0430\u0432\u043d\u0438\u0432\u0430\u0442\u044c \u043e\u0446\u0435\u043d\u043a\u0438", None))
        self.left_corner.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u043b\u0435\u0432\u043e\u043c\u0443 \u043a\u0440\u0430\u044e", None))
        self.center.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e \u0446\u0435\u043d\u0442\u0440\u0443", None))
        self.rating_transcript.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u043a\u0430 \u043e\u0446\u0435\u043d\u043e\u043a", None))
        self.full.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u043e\u0441\u0442\u044c\u044e", None))
        self.middle.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u0438\u0447\u043d\u043e \u0441\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043e", None))
        self.short.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043a\u0440\u0430\u0449\u0435\u043d\u043e", None))
        self.Z_field.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0438\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0435\u043c\u044b\u0435 \u043f\u043e\u043b\u044f", None))
        self.per_line.setText(QCoreApplication.translate("MainWindow", u"Z \u0432 \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u0440\u043e\u043a\u0435", None))
        self.one.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0434\u043d\u0430 \u0431\u0443\u043a\u0432\u0430 Z", None))
        self.no_print.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.font.setTitle(QCoreApplication.translate("MainWindow", u"\u0428\u0440\u0438\u0444\u0442", None))
        self.font_size_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u043e\u0441\u043d\u043e\u0432\u043d\u043e\u0433\u043e \u0448\u0440\u0438\u0444\u0442\u0430", None))
        self.adv_font_size_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0434\u043e\u043f. \u0441\u0432\u0435\u0434\u0435\u043d\u0438\u0439", None))
        self.FST_font_size_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440 \u0424\u0418\u041e \u0432\u044b\u043f\u0443\u0441\u043a\u043d\u0438\u043a\u0430", None))
        self.reset_diploma_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.save_diploma_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.layout.setTabText(self.layout.indexOf(self.diploma_settings), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0430\u0442\u0442\u0435\u0441\u0442\u0430\u0442\u0430", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0443\u0447\u0435\u043d\u0438\u043a\u043e\u0432", None))
        ___qtablewidgetitem = self.pupils_list.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u043c\u0438\u043b\u0438\u044f", None));
        ___qtablewidgetitem1 = self.pupils_list.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem2 = self.pupils_list.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e", None));
        ___qtablewidgetitem3 = self.pupils_list.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0440\u043e\u0436\u0434\u0435\u043d\u0438\u044f", None));
        ___qtablewidgetitem4 = self.pupils_list.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0430\u0442\u0442\u0435\u0441\u0442\u0430\u0442\u0430", None));
        self.delete_pupil.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.create_pupil.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u044b\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u043a\u043b\u0430\u0441\u0441\u0430", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"11", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0443\u043a\u0432\u0430 \u043a\u043b\u0430\u0441\u0441\u0430", None))
        self.lineEdit.setInputMask("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0410-\u042f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440", None))
        self.generate_all_diplomas.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0432\u0441\u0435\u043c", None))
        self.generate_diploma.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u043f\u0435\u0447\u0430\u0442\u0430\u0442\u044c", None))
        self.clear_pupils.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.load_pupils.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.layout.setTabText(self.layout.indexOf(self.pupils), QCoreApplication.translate("MainWindow", u"\u0423\u0447\u0435\u043d\u0438\u043a\u0438", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u0442\u0443\u043b\u044c\u043d\u0438\u043a", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0449\u0435\u043d\u0438\u0435", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u0434 \u0432\u044b\u0434\u0430\u0447\u0438", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0448\u043a\u043e\u043b\u044b", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0440\u0443\u043a\u043e\u0432\u0430\u0434\u0438\u0442\u0435\u043b\u044f", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0418\u041e \u0443\u0447\u0435\u043d\u0438\u043a\u0430", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"QR-\u043a\u043e\u0434", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"X:", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Y:", None))
        self.title_image.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0447\u0430\u0442\u0430\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u0442\u0438\u0442\u0443\u043b\u044c\u043d\u0438\u043a\u0430", None))
        self.reset_title_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0431\u0440\u043e\u0441\u0438\u0442\u044c", None))
        self.save_title_settings.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.layout.setTabText(self.layout.indexOf(self.layout_params), QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0435\u0442\u044b", None))
    # retranslateUi

