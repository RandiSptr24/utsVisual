import mysql.connector
from mysql.connector import Error

def connect_db():
    """
    Membuat koneksi ke database MySQL.
    Pastikan server MySQL aktif dan database 'db_online_training' sudah ada.
    """
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Kosongkan jika MySQL tidak memakai password
            database="db_online_training"
        )
        if db.is_connected():
            print("✅ Koneksi ke database berhasil!")
            return db
    except Error as e:
        print(f"❌ Gagal terhubung ke MySQL: {e}")
        return None
