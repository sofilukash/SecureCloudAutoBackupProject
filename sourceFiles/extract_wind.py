import os
import sys
import shutil
import zipfile

from cryptography.fernet import Fernet

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog

import globals

global user_email

class Ui_extract_wind(object):

    def __init__(self):
        self.comboBox_2 = None
        self.choice_wind = None
        self.pushButton_4 = None
        self.statusbar = None
        self.menubar = None
        self.textBrowser_3 = None
        self.lineEdit = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.textEdit = None
        self.comboBox = None
        self.pushButton = None
        self.textBrowser_2 = None
        self.textBrowser = None
        self.centralwidget = None

    def setupUi(self, extract_wind):
        extract_wind.setObjectName('SecureCloudAutoBackup')
        extract_wind.setFixedSize(800, 560)
        extract_wind.setStyleSheet('background-color: rgb(167, 194, 196);')
        icon = QtGui.QIcon()
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(project_dir, 'logo.png')
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        extract_wind.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(extract_wind)
        self.centralwidget.setObjectName('centralwidget')
        user_email = globals.user_email
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(160, 55, 500, 50))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName('textBrowser')

# Назад
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 15, 100, 34))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(0, 0, 0);')
        self.pushButton_4.setObjectName('pushButton')
        self.pushButton_4.clicked.connect(self.back_to_choice_window)
# Назад

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 100, 200, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName('textBrowser_2')

# Виберіть ключ
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 255, 200, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(self.open_file_dialog)
# Виберіть ключ

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(50, 145, 705, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet('color: rgb(15, 71, 98);')
        self.comboBox.setObjectName('comboBox')
        self.comboBox.addItem("оберіть сценарій")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(50, 200, 705, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet('color: rgb(15, 71, 98);')
        self.comboBox_2.setObjectName('comboBox')
        self.get_backup_folders_and_fill_combobox()
        self.comboBox_2.addItem("оберіть резервну копію")

        self.comboBox.currentIndexChanged.connect(self.update_archives_comboBox)

# Виберіть ключ ПОЛЕ
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(290, 255, 465, 68))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setAutoFillBackground(False)
        self.textEdit.setStyleSheet('\ncolor: rgb(15, 71, 98);\nborder: 1px solid rgb(15, 71, 98);\n'
                                    'background-color: rgb(167, 194, 196);\npadding: 5px;\n')
        self.textEdit.setObjectName('textEdit')
# Виберіть ключ ПОЛЕ

# Видобути
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 420, 160, 55))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.clicked.connect(self.handle_button_click)
# Видобути

# Вибрати місце збереження папки
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 340, 430, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_3.setObjectName('pushButton_3')
        self.pushButton_3.clicked.connect(self.open_folder_dialog)
# Вибрати місце збереження папки

# Вибрати місце збереження папки ПОЛЕ
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(520, 340, 235, 40))
        self.lineEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet('\ncolor: rgb(15, 71, 98);\nborder: 1px solid rgb(15, 71, 98);\n'
                                    'background-color: rgb(167, 194, 196);\npadding: 5px;\n')
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName('lineEdit_3')
# Вибрати місце збереження папки ПОЛЕ

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(525, 490, 250, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(7)
        font.setItalic(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setObjectName('textBrowser_3')

        extract_wind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(extract_wind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 18))
        self.menubar.setObjectName('menubar')

        extract_wind.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(extract_wind)
        self.statusbar.setObjectName('statusbar')

        extract_wind.setStatusBar(self.statusbar)
        self.retranslateUi(extract_wind)
        QtCore.QMetaObject.connectSlotsByName(extract_wind)

    def retranslateUi(self, extract_wind):
        _translate = QtCore.QCoreApplication.translate
        extract_wind.setWindowTitle(_translate('extract_wind', 'extract_wind'))
        self.textBrowser.setHtml(_translate('extract_wind', '<html><body><p align="center">'
                                                            'Видобути створені резервні копії</p></body></html>'))
        self.textBrowser_2.setHtml(_translate('extract_wind', '<html><body><p align="left">'
                                                              'Оберіть сценарій</p></body></html>'))
        self.pushButton.setText(_translate('extract_wind', 'Виберіть ключ'))
        self.pushButton_2.setText(_translate('extract_wind', 'Видобути'))
        self.pushButton_3.setText(_translate('extract_wind', 'Вибрати місце збереження папки'))
        self.textBrowser_3.setHtml(_translate('extract_wind', '<html><body><p align="right">'
                                                              'SecureCloudAutoBackupProject<br>'
                                                              'by well-wisher</p></body></html>'))
        self.pushButton_4.setText(_translate('extract_wind', 'Назад'))

    def back_to_choice_window(self):
        from choice_wind import ChoiceWindow
        self.choice_wind = ChoiceWindow()
        self.choice_wind.show()
        self.close_this_window()

    @staticmethod
    def close_this_window():
        main_window = QtWidgets.QApplication.activeWindow()
        if main_window:
            main_window.close()

    def get_backup_folders(self):
        if not globals.user_authenticated:
            print("User is not authenticated.")
            return

        creds = globals.drive.auth.credentials
        drive_service = build("drive", "v3", credentials=creds)

        try:
            results = drive_service.files().list(
                q="name = 'backups' and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            folders = results.get("files", [])
            if not folders:
                print("No folder named 'backups' found.")
                return

            backup_folder_id = folders[0]["id"]

            folder_results = drive_service.files().list(
                q=f"'{backup_folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            folder_names = [folder["name"] for folder in folder_results.get("files", [])]

            for name in folder_names:
                self.comboBox.addItem(name)

        except HttpError as error:
            print(f"An error occurred: {error}")

    def get_backup_folders_and_fill_combobox(self):
        if not globals.user_authenticated:
            print("User is not authenticated.")
            return

        creds = globals.drive.auth.credentials
        drive_service = build("drive", "v3", credentials=creds)

        try:
            results = drive_service.files().list(
                q="name = 'backups' and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            folders = results.get("files", [])
            if not folders:
                print("No folder named 'backups' found.")
                return

            backup_folder_id = folders[0]["id"]

            folder_results = drive_service.files().list(
                q=f"'{backup_folder_id}' in parents and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            folder_names = [folder["name"] for folder in folder_results.get("files", [])]

            self.comboBox.clear()

            for name in folder_names:
                self.comboBox.addItem(name)

        except HttpError as error:
            print(f"An error occurred: {error}")

    def update_archives_comboBox(self):
        selected_folder_name = self.comboBox.currentText()
        if not selected_folder_name:
            return

        self.get_archives_in_folder(selected_folder_name)

    def get_archives_in_folder(self, folder_name):
        if not globals.user_authenticated:
            print("User is not authenticated.")
            return

        creds = globals.drive.auth.credentials
        drive_service = build("drive", "v3", credentials=creds)

        try:
            results = drive_service.files().list(
                q=f"name = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            folder = results.get("files", [])[0]
            folder_id = folder["id"]

            file_results = drive_service.files().list(
                q=f"'{folder_id}' in parents and (mimeType = 'application/zip' or mimeType = 'application/x-tar')",
                fields="files(id, name)"
            ).execute()

            archive_names = [file["name"] for file in file_results.get("files", [])]

            self.comboBox_2.clear()

            for name in archive_names:
                self.comboBox_2.addItem(name)

        except HttpError as error:
            print(f"An error occurred: {error}")

    def close_this_window(self):
        self.close()

    def handle_button_click(self):
        if self.comboBox.currentText() == "Оберіть сценарій" or self.comboBox_2.currentText() == "Оберіть час":
            QtWidgets.QMessageBox.warning(self, "Помилка", "Будь ласка, виберіть сценарій та час.")
            return
        if not self.textEdit.toPlainText():
            QtWidgets.QMessageBox.warning(self, "Помилка", "Введіть Fernet ключ.")
            return
        if not self.lineEdit.text():
            QtWidgets.QMessageBox.warning(self, "Помилка", "Введіть шлях для збереження.")
            return
        fernet_key = self.textEdit.toPlainText().strip()
        try:
            fernet = Fernet(fernet_key)
        except Exception as e:
            QtWidgets.QMessageBox.warning(self, "Помилка", f"Невірний Fernet ключ: {e}")
            return
        selected_folder_name = self.comboBox.currentText()
        selected_archive_name = self.comboBox_2.currentText()

        self.download_and_process_archive(selected_folder_name, selected_archive_name, fernet_key)

    def download_and_process_archive(self, folder_name, archive_name, fernet_key):
        if not globals.user_authenticated:
            print("User is not authenticated.")
            return

        creds = globals.drive.auth.credentials
        drive_service = build("drive", "v3", credentials=creds)

        try:
            project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            backup_dir = "backups"
            local_backup_dir = os.path.join(project_dir, backup_dir)
            if not os.path.exists(local_backup_dir):
                os.makedirs(local_backup_dir)

            folder_results = drive_service.files().list(
                q="name = 'backups' and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            if not folder_results.get("files"):
                print("Папка 'backups' не знайдена на Google Диску.")
                return

            folder_id = folder_results.get("files", [])[0]["id"]
            selected_folder = self.comboBox.currentText()
            selected_folder_results = drive_service.files().list(
                q=f"'{folder_id}' in parents and name = '{selected_folder}' and mimeType = 'application/vnd.google-apps.folder'",
                fields="files(id, name)"
            ).execute()

            if not selected_folder_results.get("files"):
                print(f"Папка '{selected_folder}' не знайдена в папці 'backups'.")
                return

            selected_folder_id = selected_folder_results.get("files", [])[0]["id"]

            selected_archive = self.comboBox_2.currentText()

            archive_results = drive_service.files().list(
                q=f"'{selected_folder_id}' in parents and name = '{selected_archive}'",
                fields="files(id, name)"
            ).execute()

            if not archive_results.get("files"):
                print(f"Архів '{selected_archive}' не знайдений у папці '{selected_folder}'.")
                return

            archive_id = archive_results.get("files", [])[0]["id"]
            request = drive_service.files().get_media(fileId=archive_id)
            file_path = f"{local_backup_dir}/{selected_archive}"

            with open(file_path, "wb") as f:
                downloader = MediaIoBaseDownload(f, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()
                    print(f"Завантажено {int(status.progress() * 100)}%")

            self.extract_and_process_archive(file_path, fernet_key)

        except HttpError as error:
            QtWidgets.QMessageBox.warning(self, "Помилка", f"Помилка при роботі з Google Drive: {error}")

    def extract_and_process_archive(self, archive_path, fernet_key):
        archive_name = os.path.basename(archive_path).replace(".zip", "")

        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        extract_to = os.path.join(project_dir, "backups", archive_name)

        if not os.path.exists(extract_to):
            os.makedirs(extract_to)

        if archive_path.endswith(".zip"):
            with zipfile.ZipFile(archive_path, "r") as zip_ref:
                zip_ref.extractall(extract_to)

        self.decrypt_and_move_folder(extract_to, fernet_key)

    def decrypt_and_move_folder(self, folder_path, fernet_key):
        try:
            fernet = Fernet(fernet_key)
            for root, dirs, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "rb") as f:
                        encrypted_data = f.read()
                    decrypted_data = fernet.decrypt(encrypted_data)
                    with open(file_path, "wb") as f:
                        f.write(decrypted_data)

            destination_path = self.lineEdit.text().strip()
            destination_folder = os.path.join(destination_path, os.path.basename(folder_path))

            shutil.copytree(folder_path, destination_folder)

            project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            backups_folder = "backups"
            path_backups_folder = os.path.join(project_dir, backups_folder)
            for root, dirs, files in os.walk(path_backups_folder, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    os.rmdir(dir_path)

            QtWidgets.QMessageBox.information(self, "Успіх", "Архів успішно розшифровано та переміщено!")

        except Exception as e:
            project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
            backups_folder = "backups"
            path_backups_folder = os.path.join(project_dir, backups_folder)
            for root, dirs, files in os.walk(path_backups_folder, topdown=False):
                for file in files:
                    file_path = os.path.join(root, file)
                    os.remove(file_path)
                for dir in dirs:
                    dir_path = os.path.join(root, dir)
                    os.rmdir(dir_path)
            QtWidgets.QMessageBox.warning(self, "Помилка", f"Помилка при розшифровці: {e}")

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Оберіть файл", "", "Key Files (*.aes);;All Files (*)", options=options)

        if not file_path:
            return
        if not file_path.endswith(".aes"):
            QMessageBox.warning(self, "Помилка", "Будь ласка, оберіть файл з розширенням .aes")
            return

        try:
            with open(file_path, 'r') as file:
                content = file.read()
            if len(content) > 100:
                content = content[:100] + "\n(Вміст обрізано. Ви ввели більше ніж 100 символів.)"
                self.textEdit.setText(content)
            else:
                self.textEdit.setText(content)
        except Exception as e:
            QMessageBox.warning(self, "Помилка", f"Не вдалося відкрити файл: {e}")

    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Оберіть папку")
        if not folder_path:
            return
        self.lineEdit.setText(folder_path)

class ExtractWindow(QtWidgets.QMainWindow, Ui_extract_wind):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    extract_wind = QtWidgets.QMainWindow()
    ui = Ui_extract_wind()
    ui.setupUi(extract_wind)
    extract_wind.show()
    sys.exit(app.exec_())
