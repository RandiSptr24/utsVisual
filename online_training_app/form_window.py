from PySide6.QtWidgets import QMainWindow
from PySide6.QtUiTools import QUiLoader
from mainwindow import MainWindow

class FormWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui", None)
        self.ui.show()

        # Hubungkan QAction
        self.action_form_hasil = self.ui.findChild(type(self.ui.findChild(object, "actionForm_Hasil_Ujian")), "actionForm_Hasil_Ujian")
        if self.action_form_hasil:
            self.action_form_hasil.triggered.connect(self.open_mainwindow)

    def open_mainwindow(self):
        self.main_window_instance = MainWindow()
        self.main_window_instance.ui.show()
