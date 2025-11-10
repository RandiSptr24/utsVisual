from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QComboBox, QLineEdit, QTableWidget
from PySide6.QtUiTools import QUiLoader
from db import connect_db
from add_user_window import AddUserWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loader = QUiLoader()
        self.ui = loader.load("mainwindow.ui", None)

        # Ambil widget
        self.search_button: QPushButton = self.ui.findChild(QPushButton, "searchButton")
        self.add_user_button: QPushButton = self.ui.findChild(QPushButton, "btnAddTask")
        self.role_combo: QComboBox = self.ui.findChild(QComboBox, "roleComboBox")
        self.search_input: QLineEdit = self.ui.findChild(QLineEdit, "searchLineEdit")
        self.table_widget: QTableWidget = self.ui.findChild(QTableWidget, "tableWidget")

        # Sambungkan tombol
        if self.search_button:
            self.search_button.clicked.connect(self.load_data)
        if self.add_user_button:
            self.add_user_button.clicked.connect(self.open_add_user)

        # Isi combo box role
        self.role_combo.addItems(["All", "Admin", "Peserta", "Trainer"])

        # Load data pertama kali
        self.load_data()

    def load_data(self):
        db = connect_db()
        cursor = db.cursor()

        query = "SELECT user_id, name, email, role, created_at FROM users WHERE 1=1"
        params = []

        selected_role = self.role_combo.currentText()
        if selected_role != "All":
            query += " AND role=%s"
            params.append(selected_role)

        search_text = self.search_input.text().strip()
        if search_text:
            query += " AND (name LIKE %s OR email LIKE %s)"
            params.extend([f"%{search_text}%", f"%{search_text}%"])

        cursor.execute(query, params)
        data = cursor.fetchall()

        self.table_widget.setRowCount(len(data))
        self.table_widget.setColumnCount(5)
        self.table_widget.setHorizontalHeaderLabels(["User ID", "Nama", "Email", "Role", "Tanggal Dibuat"])

        for row_idx, row_data in enumerate(data):
            for col_idx, value in enumerate(row_data):
                self.table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

        cursor.close()
        db.close()

    def open_add_user(self):
        self.add_user_window = AddUserWindow(refresh_callback=self.load_data)
        self.add_user_window.show()
