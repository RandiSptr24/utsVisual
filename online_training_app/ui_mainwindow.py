# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 80, 521, 41))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnTakeExam = QPushButton(self.widget)
        self.btnTakeExam.setObjectName(u"btnTakeExam")

        self.horizontalLayout.addWidget(self.btnTakeExam)

        self.btnAddTask = QPushButton(self.widget)
        self.btnAddTask.setObjectName(u"btnAddTask")

        self.horizontalLayout.addWidget(self.btnAddTask)

        self.btnViewResults = QPushButton(self.widget)
        self.btnViewResults.setObjectName(u"btnViewResults")

        self.horizontalLayout.addWidget(self.btnViewResults)

        self.btnAddQuestion = QPushButton(self.widget)
        self.btnAddQuestion.setObjectName(u"btnAddQuestion")

        self.horizontalLayout.addWidget(self.btnAddQuestion)

        self.widget1 = QWidget(self.centralwidget)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(120, 155, 521, 271))
        self.gridLayout = QGridLayout(self.widget1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.widget1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.searchLineEdit = QLineEdit(self.widget1)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.gridLayout.addWidget(self.searchLineEdit, 0, 1, 1, 1)

        self.searchButton = QPushButton(self.widget1)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 0, 2, 1, 1)

        self.roleComboBox = QComboBox(self.widget1)
        self.roleComboBox.setObjectName(u"roleComboBox")

        self.gridLayout.addWidget(self.roleComboBox, 0, 4, 1, 1)

        self.tableWidget = QTableWidget(self.widget1)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout.addWidget(self.tableWidget, 1, 1, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnTakeExam.setText(QCoreApplication.translate("MainWindow", u"Kerjakan Ujian", None))
        self.btnAddTask.setText(QCoreApplication.translate("MainWindow", u"Tambah Ujian", None))
        self.btnViewResults.setText(QCoreApplication.translate("MainWindow", u"Lihat Hasil Ujian", None))
        self.btnAddQuestion.setText(QCoreApplication.translate("MainWindow", u"Tambah Soal", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pencarian :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Filter Role:", None))
        self.searchButton.setText(QCoreApplication.translate("MainWindow", u"Cari", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Data User", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ujian", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Hasil", None));
    # retranslateUi

