# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionForm_Hasil_Ujian = QAction(MainWindow)
        self.actionForm_Hasil_Ujian.setObjectName(u"actionForm_Hasil_Ujian")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.labelHeader = QLabel(self.centralwidget)
        self.labelHeader.setObjectName(u"labelHeader")
        self.labelHeader.setGeometry(QRect(200, 40, 281, 31))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.labelHeader.setFont(font)
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(70, 210, 501, 131))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 350, 131, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setItalic(True)
        self.label_2.setFont(font1)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(120, 100, 421, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadButton = QPushButton(self.horizontalLayoutWidget)
        self.loadButton.setObjectName(u"loadButton")

        self.horizontalLayout.addWidget(self.loadButton)

        self.addUserButton = QPushButton(self.horizontalLayoutWidget)
        self.addUserButton.setObjectName(u"addUserButton")

        self.horizontalLayout.addWidget(self.addUserButton)

        self.roleComboBox = QComboBox(self.horizontalLayoutWidget)
        self.roleComboBox.setObjectName(u"roleComboBox")

        self.horizontalLayout.addWidget(self.roleComboBox)

        self.searchLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.searchLineEdit.setObjectName(u"searchLineEdit")

        self.horizontalLayout.addWidget(self.searchLineEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuForm_Hasil_Ujian = QMenu(self.menubar)
        self.menuForm_Hasil_Ujian.setObjectName(u"menuForm_Hasil_Ujian")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuForm_Hasil_Ujian.menuAction())
        self.menuForm_Hasil_Ujian.addSeparator()
        self.menuForm_Hasil_Ujian.addAction(self.actionForm_Hasil_Ujian)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionForm_Hasil_Ujian.setText(QCoreApplication.translate("MainWindow", u"Form Hasil Ujian", None))
        self.labelHeader.setText(QCoreApplication.translate("MainWindow", u"ONLINE TRAINING APP", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"User ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Role", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Created At", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2025 PT MSM/TTN", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"Load Data", None))
        self.addUserButton.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.menuForm_Hasil_Ujian.setTitle(QCoreApplication.translate("MainWindow", u"Pilih Form", None))
    # retranslateUi

