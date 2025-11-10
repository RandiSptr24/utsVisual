from PySide6.QtWidgets import QMainWindow, QMessageBox, QLineEdit, QPushButton, QComboBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from db import connect_db

class AddUserWindow(QMainWindow):
    def __init__(self, refresh_callback=None):
        super().__init__()

        self.refresh_callback = refresh_callback

        # Load UI langsung ke self
        loader = QUiLoader()
        file = QFile("add_user.ui")
        if not file.open(QFile.ReadOnly):
            QMessageBox.critical(None, "Error", "Gagal membuka add_user.ui")
            return

        loader.load(file, self)  # penting: load ke self
        file.close()

        # Ambil widget dari UI
        self.name_input: QLineEdit = self.findChild(QLineEdit, "namaLineEdit")
        self.email_input: QLineEdit = self.findChild(QLineEdit, "emailLineEdit")
        self.password_input: QLineEdit = self.findChild(QLineEdit, "passwordLineEdit")
        self.role_combo: QComboBox = self.findChild(QComboBox, "roleComboBox")
        self.jabatan_combo: QComboBox = self.findChild(QComboBox, "jabatanComboBox")
        self.save_button: QPushButton = self.findChild(QPushButton, "saveButton")

        # Event tombol simpan
        self.save_button.clicked.connect(self.save_user)

        # Load combo box
        self.load_roles()
        self.load_jabatan()

    def load_roles(self):
        self.role_combo.addItems(["HR", "Trainer", "Peserta"])

    def load_jabatan(self):
        try:
            db = connect_db()
            cursor = db.cursor()
            cursor.execute("SELECT jabatan_id, nama_jabatan FROM jabatan")
            jabatan_list = cursor.fetchall()
            cursor.close()
            db.close()

            self.jabatan_combo.addItem("None", None)
            for jabatan_id, nama_jabatan in jabatan_list:
                self.jabatan_combo.addItem(nama_jabatan, jabatan_id)
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Gagal memuat jabatan: {e}")

    def save_user(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        password = self.password_input.text().strip()
        role = self.role_combo.currentText()
        jabatan_id = self.jabatan_combo.currentData()

        if not name or not email or not password or not role:
            QMessageBox.warning(self, "Error", "Semua field harus diisi!")
            return

        try:
            db = connect_db()
            cursor = db.cursor()
            sql = "INSERT INTO users (name, email, password, role, jabatan_id) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (name, email, password, role, jabatan_id))
            db.commit()
            cursor.close()
            db.close()

            QMessageBox.information(self, "Sukses", "User berhasil ditambahkan!")
            self.close()

            if self.refresh_callback:
                self.refresh_callback()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Gagal menambahkan user: {e}")
