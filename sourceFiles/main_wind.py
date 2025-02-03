import os
import sys
from urllib.request import Request

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QThreadPool, QRunnable

from httplib2 import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import globals

def authenticate_google_drive():
    try:
        gauth = GoogleAuth()
        gauth.Scope(['https://www.googleapis.com/auth/drive.file'])
        gauth.LocalWebserverAuth()
        globals.drive = GoogleDrive(gauth)
        about = globals.drive.GetAbout()
        globals.user_email = about['user']['emailAddress']

        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

        root_dir = os.path.join(project_dir, 'root')

        user_dir = os.path.join(root_dir, globals.user_email)
        os.makedirs(user_dir, exist_ok=True)

        credentials_path = os.path.join(user_dir, 'credentials.json')
        gauth.SaveCredentialsFile(credentials_path)

        token_path = os.path.join(user_dir, 'token.json')
        creds = None

        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path, ['https://www.googleapis.com/auth/drive.file'])

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secrets.json', ['https://www.googleapis.com/auth/drive.file'])
                creds = flow.run_local_server(port=0)

            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        drive_service = build('drive', 'v3', credentials=creds)
        about = drive_service.about().get(fields="user").execute()
        user_email = about['user']['emailAddress']
        print('Автентифікація успішна:', user_email)
        globals.user_authenticated = True

        return drive_service

    except Exception as e:
        print('Помилка автентифікації:', e)
        globals.user_authenticated = False


def is_authenticated():
    return globals.user_authenticated

class Worker(QRunnable):

    def __init__(self, func, *args, **kwargs):
        super().__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.func(*self.args, **self.kwargs)

class Ui_main_wind(object):

    def __init__(self):
        self.main = None
        self.choice_wind = None
        self.centralwidget = None
        self.statusbar = None
        self.textBrowser = None
        self.textBrowser_3 = None
        self.menubar = None
        self.textBrowser_2 = None
        self.pushButton_2 = None
        self.pushButton_4 = None
        self.label = None
        self.pushButton = None
        self.threadpool = QThreadPool()

    @staticmethod
    def show_error(message):
        QtWidgets.QMessageBox.critical(None, 'Помилка', message)

    def setupUi(self, main_wind):
        main_wind.setObjectName('SecureCloudAutoBackup')
        main_wind.setFixedSize(710, 450)
        main_wind.setAcceptDrops(False)
        icon = QtGui.QIcon()
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(project_dir, 'logo.png')
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_wind.setWindowIcon(icon)
        main_wind.setAutoFillBackground(False)
        main_wind.setStyleSheet('background-color: rgb(167, 194, 196);')
        main_wind.setIconSize(QtCore.QSize(18, 18))
        self.centralwidget = QtWidgets.QWidget(main_wind)
        self.centralwidget.setObjectName('centralwidget')
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(35, 170, 151, 141))
        self.label.setText('')
        label_path = os.path.join(project_dir, 'logo.svg')
        self.label.setPixmap(QtGui.QPixmap(label_path))
        self.label.setObjectName('label')

        def on_pushButton_clicked():
            worker = Worker(authenticate_google_drive)
            self.threadpool.start(worker)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 205, 250, 60))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('\nbackground-color: rgb(15, 71, 98);\nborder-bottom-color: rgb(0, 0, 0);\n'
                                      'color: rgb(167, 194, 196);\n')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(on_pushButton_clicked)

        def on_pushButton_2_clicked():
            if is_authenticated():
                print('Користувач автентифікований:', globals.user_email)
                self.pushButton_2.clicked.connect(self.get_open_choice_window)
            else:
                QMessageBox.warning(None, 'Помилка', 'Будь ласка, пройдіть автентифікацію перед продовженням.')
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 295, 90, 35))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('\nbackground-color: rgb(15, 71, 98);\nborder-bottom-color: rgb(0, 0, 0);\n'
                                        'color: rgb(167, 194, 196);\n')
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.clicked.connect(on_pushButton_2_clicked)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 295, 90, 35))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet('\nbackground-color: rgb(15, 71, 98);\nborder-bottom-color: rgb(0, 0, 0);\n'
                                        'color: rgb(167, 194, 196);\n')
        self.pushButton_4.setObjectName('pushButton_4')
        self.pushButton_4.clicked.connect(self.close_this_window)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 20, 550, 150))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(16)
        font.setBold(True)
        self.textBrowser.setFont(font)
        self.textBrowser.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName('textBrowser')
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(260, 145, 360, 41))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName('textBrowser_2')
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(440, 380, 250, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(7)
        font.setItalic(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setObjectName('textBrowser_3')
        self.menubar = QtWidgets.QMenuBar(main_wind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 18))
        self.menubar.setObjectName('menubar')
        main_wind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_wind)
        self.statusbar.setObjectName('statusbar')
        main_wind.setStatusBar(self.statusbar)
        self.retranslateUi(main_wind)
        QtCore.QMetaObject.connectSlotsByName(main_wind)
        main_wind.setCentralWidget(self.centralwidget)

    def retranslateUi(self, main_wind):
        _translate = QtCore.QCoreApplication.translate
        main_wind.setWindowTitle(_translate('main_wind', 'main_wind'))
        main_wind.setAccessibleName(_translate('main_wind', 'main_wind'))
        self.pushButton.setText(_translate('main_wind', 'Аутентифікація'))
        self.pushButton_2.setText(_translate('main_wind', 'Далі'))
        self.pushButton_4.setText(_translate('main_wind', 'Вийти'))
        self.textBrowser.setHtml(_translate('main_wind', '<html><body><p align="center">'
                                                         'Автоматизоване резервне копіювання папок до Google Drive</p></body></html>'))
        self.textBrowser_2.setHtml(_translate('main_wind', '<html><body><p>'
                                                           'Будь ласка, пройдіть аутентифікацію!</p></body></html>'))
        self.textBrowser_3.setHtml(_translate('main_wind', '<html><body><p align="right">'
                                                           'SecureCloudAutoBackupProject<br>by well-wisher</p></body></html>'))

    def get_open_choice_window(self):
        from choice_wind import ChoiceWindow
        self.choice_wind = ChoiceWindow()
        self.choice_wind.show()
        self.close_this_window()

    @staticmethod
    def close_this_window():
        main_window = QtWidgets.QApplication.activeWindow()
        if main_window:
            main_window.close()

class MainWindow(QtWidgets.QMainWindow, Ui_main_wind):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_wind = QtWidgets.QMainWindow()
    ui = Ui_main_wind()
    ui.setupUi(main_wind)
    main_wind.show()
    sys.exit(app.exec_())