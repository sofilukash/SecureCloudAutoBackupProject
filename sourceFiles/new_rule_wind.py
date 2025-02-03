import os
import sys
import json
import shutil
import base64
import io
from datetime import datetime

from cryptography.fernet import Fernet

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

from PyQt5 import QtCore, QtGui, QtWidgets

import globals

class BackupWorker(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)

    def run(self):
        for i in range(1, 101):
            self.progress.emit(i)
            QtCore.QThread.msleep(50)

        self.progress.emit(100)

class Ui_new_rule_wind(object):
    def __init__(self):
        self.worker = None
        self.is_closable = True
        self.is_button_pressed = False
        self.lineEdit_4 = None
        self.days = None
        self.on_pushButton_clicked = None
        self.choose_folder = None
        self.choice_wind = None
        self.textBrowser_3 = None
        self.statusbar = None
        self.menubar = None
        self.line_2 = None
        self.pushButton_6 = None
        self.pushButton_5 = None
        self.pushButton_8 = None
        self.progressBar_2 = None
        self.pushButton_4 = None
        self.textBrowser_2 = None
        self.checkBox_1 = None
        self.checkBox_7 = None
        self.checkBox_4 = None
        self.checkBox_6 = None
        self.checkBox_5 = None
        self.checkBox_3 = None
        self.checkBox_2 = None
        self.timeEdit = None
        self.lineEdit_3 = None
        self.centralwidget = None
        self.checkBox = None
        self.pushButton_3 = None
        self.line = None
        self.pushButton_2 = None
        self.textBrowser = None
        self.pushButton = None

    def setupUi(self, new_rule_wind):
        new_rule_wind.setObjectName('SecureCloudAutoBackup')
        new_rule_wind.setFixedSize(800, 835)
        new_rule_wind.setStyleSheet('background-color: rgb(167, 194, 196);')
        new_rule_wind.setUnifiedTitleAndToolBarOnMac(False)
        icon = QtGui.QIcon()
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(project_dir, 'logo.png')
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        new_rule_wind.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(new_rule_wind)
        self.centralwidget.setObjectName('centralwidget')

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 238, 180, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(self.get_file_path)

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(50, 15, 100, 34))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(0, 0, 0);')
        self.pushButton_8.setObjectName('pushButton')
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.clicked.connect(self.back_to_choice_window)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(50, 65, 700, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setBold(True)
        font.setPointSize(13)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName('textBrowser')

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(480, 308, 270, 40))
        self.lineEdit_3.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setAutoFillBackground(False)
        self.lineEdit_3.setStyleSheet('color: rgb(15, 71, 98); border: 1px solid rgb(15, 71, 98); '
                                      'background-color: rgb(167, 194, 196); padding: 5px;')
        self.lineEdit_3.setFrame(True)
        self.lineEdit_3.setObjectName('lineEdit_3')

        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(280, 240, 100, 40))
        self.timeEdit.setStyleSheet('QTimeEdit {border: 1px solid rgb(15, 71, 98);color: rgb(15, 71, 98);'
                                    'font-family: Cambria;font-size: 10pt;} ')
        self.timeEdit.setObjectName('timeEdit')

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 400, 270, 50))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_2.setObjectName('pushButton_2')

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(720, 8, 60, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet('background-color: rgb(167, 194, 196);\nborder-color: rgb(167, 194, 196);\n'
                                        'border-bottom-color: rgb(167, 194, 196);\ncolor: rgb(0, 0, 0);\n')
        self.pushButton_3.setAutoDefault(True)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName('pushButton_3')

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(30, 480, 750, 10))
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName('line')

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(60, 220, 150, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                    'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox.setObjectName('checkBox')

        self.checkBox_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_1.setGeometry(QtCore.QRect(60, 255, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_1.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_1.setFont(font)
        self.checkBox_1.setObjectName('checkBox_2')

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(60, 285, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_2.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName('checkBox_3')

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(60, 315, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_3.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n        ')
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName('checkBox_4')

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(60, 345, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_4.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName('checkBox_5')

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(60, 375, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_5.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_5.setFont(font)
        self.checkBox_5.setObjectName('checkBox_6')

        self.checkBox_6 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_6.setGeometry(QtCore.QRect(60, 405, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_6.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_6.setFont(font)
        self.checkBox_6.setObjectName('checkBox_7')

        self.checkBox_7 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_7.setGeometry(QtCore.QRect(60, 435, 150, 21))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.checkBox_7.setStyleSheet('\nQCheckBox::indicator {border: 2px solid rgb(15, 71, 98); background-color: white;}\n'
                                      'QCheckBox::indicator:checked {background-color: rgb(15, 71, 98);}\n')
        self.checkBox_7.setFont(font)
        self.checkBox_7.setObjectName('checkBox_8')

        self.checkBox.stateChanged.connect(self.toggle_all_days)
        self.checkBox_1.stateChanged.connect(self.update_days)
        self.checkBox_2.stateChanged.connect(self.update_days)
        self.checkBox_3.stateChanged.connect(self.update_days)
        self.checkBox_4.stateChanged.connect(self.update_days)
        self.checkBox_5.stateChanged.connect(self.update_days)
        self.checkBox_6.stateChanged.connect(self.update_days)
        self.checkBox_7.stateChanged.connect(self.update_days)

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(50, 140, 500, 58))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName('textBrowser_2')

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(60, 510, 350, 50))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_4.setObjectName('pushButton_4')
        self.pushButton_4.clicked.connect(self.on_pushButton_4_clicked)

        self.pushButton_2.clicked.connect(self.apply_changes)
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(450, 520, 300, 30))
        self.progressBar_2.setProperty('value', 0)
        self.progressBar_2.setMaximum(100)
        self.progressBar_2.setObjectName('progressBar_2')
        self.progressBar_2.setStyleSheet("""
            QProgressBar {
                background-color: rgb(167, 194, 196);color: black;border: 1px solid rgb(15, 71, 98);border-radius: 4px;
                font-weight: bold;padding: 4px;text-align: center;}
            QProgressBar::chunk {
                background-color: rgb(145, 172, 143); border-radius: 2px;
                }""")

        self.progressBar_2.setTextVisible(True)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(550, 640, 200, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_5.setObjectName('pushButton_5')
# Завантажити ключ

        #
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 640, 220, 40))
        self.lineEdit_4.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setAutoFillBackground(False)
        self.lineEdit_4.setStyleSheet('\ncolor: rgb(15, 71, 98);\nborder: 1px solid rgb(15, 71, 98);\n'
                                      'background-color: rgb(167, 194, 196);\npadding: 5px;\n')
        self.lineEdit_4.setFrame(True)
        self.lineEdit_4.setObjectName('lineEdit_3')
        #

# Оберіть папку
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(50, 640, 200, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_6.setObjectName('pushButton_6')
# Оберіть папку

        #
        self.pushButton_2.setDisabled(True)
        self.pushButton_5.setDisabled(True)
        self.pushButton_6.setDisabled(True)
        self.pushButton_4.setEnabled(False)
        #

        #
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(30, 590, 750, 10))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName('line_2')
        #

# сноска
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(520, 770, 250, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(7)
        font.setItalic(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setObjectName('textBrowser_3')
# сноска

        new_rule_wind.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(new_rule_wind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 18))
        self.menubar.setObjectName('menubar')

        new_rule_wind.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(new_rule_wind)
        self.statusbar.setObjectName('statusbar')

        new_rule_wind.setStatusBar(self.statusbar)

        self.retranslateUi(new_rule_wind)

        QtCore.QMetaObject.connectSlotsByName(new_rule_wind)

    def retranslateUi(self, new_rule_wind):
        _translate = QtCore.QCoreApplication.translate
        new_rule_wind.setWindowTitle(_translate('new_rule_wind', 'new_rule_wind'))
        self.pushButton.setText(_translate('new_rule_wind', 'Оберіть папку'))
        self.textBrowser.setHtml(_translate('new_rule_wind', '<html><body><p align=\"center\">'
                                                             'Створити нове правило для резервного копіювання</p></body></html>'))
        self.textBrowser_3.setHtml(_translate('new_rule_wind', '<html><body><p align=\"right\">'
                                                               'SecureCloudAutoBackupProject<br>'
                                                               'by well-wisher</p></body></html>'))
        self.checkBox.setText(_translate('new_rule_wind', 'Кожен день'))
        self.checkBox_2.setText(_translate('new_rule_wind', 'Вівторок'))
        self.checkBox_3.setText(_translate('new_rule_wind', 'Середа'))
        self.checkBox_5.setText(_translate('new_rule_wind', 'П\'ятниця'))
        self.checkBox_6.setText(_translate('new_rule_wind', 'Субота'))
        self.checkBox_4.setText(_translate('new_rule_wind', 'Четверг'))
        self.checkBox_7.setText(_translate('new_rule_wind', 'Неділя'))
        self.checkBox_1.setText(_translate('new_rule_wind', 'Понеділок'))
        self.textBrowser_2.setHtml(_translate('new_rule_wind', '<html><body><p align=\"left\">'
                                                               'Як часто має відбуватися резервне копіювання?<br>'
                                                               'Оберіть дні та години</p></body></html>'))
        self.pushButton_4.setText(_translate('new_rule_wind', 'Створити автоматичний сценарій'))
        self.pushButton_5.setText(_translate('new_rule_wind', 'Завантажити ключ'))
        self.pushButton_6.setText(_translate('new_rule_wind', 'Оберіть папку'))
        self.pushButton_8.setText(_translate('new_rule_wind', 'Назад'))
        self.pushButton_2.setText(_translate('new_rule_wind', 'Підтвердити дані'))
        self.pushButton_3.setText(_translate('new_rule_wind', '?'))

    def closeEvent(self, event):
        if not self.is_closable:
            QtWidgets.QMessageBox.warning(None, 'Попередження', 'Будь ласка, завершіть поточну дію.')
            event.ignore()
        else:
            event.accept()

    def get_file_path(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Вибір папки')
        if folder_path:
            self.lineEdit_3.setText(folder_path)
        self.pushButton_2.setEnabled(True)

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

    def toggle_all_days(self, state):
        checked = state == QtCore.Qt.Checked
        self.checkBox_1.setChecked(checked)
        self.checkBox_2.setChecked(checked)
        self.checkBox_3.setChecked(checked)
        self.checkBox_4.setChecked(checked)
        self.checkBox_5.setChecked(checked)
        self.checkBox_6.setChecked(checked)
        self.checkBox_7.setChecked(checked)
        self.update_days()

    def update_days(self):
        self.days = []
        if self.checkBox.isChecked():
            self.days = ['Кожен день']
            return
        if self.checkBox_1.isChecked():
            self.days.append('Понеділок')
        if self.checkBox_2.isChecked():
            self.days.append('Вівторок')
        if self.checkBox_3.isChecked():
            self.days.append('Середа')
        if self.checkBox_4.isChecked():
            self.days.append('Четверг')
        if self.checkBox_5.isChecked():
            self.days.append('П\'ятниця')
        if self.checkBox_6.isChecked():
            self.days.append('Субота')
        if self.checkBox_7.isChecked():
            self.days.append('Неділя')

    def get_selected_days(self):
        days = []
        if self.checkBox_1.isChecked():
            days.append('Monday')
        if self.checkBox_2.isChecked():
            days.append('Tuesday')
        if self.checkBox_3.isChecked():
            days.append('Wednesday')
        if self.checkBox_4.isChecked():
            days.append('Thursday')
        if self.checkBox_5.isChecked():
            days.append('Friday')
        if self.checkBox_6.isChecked():
            days.append('Saturday')
        if self.checkBox_7.isChecked():
            days.append('Sunday')
        return days

    def get_time(self):
        time = self.timeEdit.time()
        time = time.toString('HH:mm:ss')
        return time

    def apply_changes(self):
        if any(cb.isChecked() for cb in (self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4,
                                         self.checkBox_5, self.checkBox_6, self.checkBox_7)) \
                and self.lineEdit_3.text().strip():
            for widget in [self.pushButton, self.checkBox, self.checkBox_1, self.checkBox_2, self.checkBox_3,
                           self.checkBox_4, self.checkBox_5, self.checkBox_6, self.checkBox_7, self.timeEdit]:
                widget.setDisabled(True)

            self.pushButton_4.setEnabled(True)
            self.pushButton_8.setDisabled(True)
            self.is_closable = False
        else:
            if not any(cb.isChecked() for cb in (self.checkBox_1, self.checkBox_2, self.checkBox_3,
                                                 self.checkBox_4, self.checkBox_5, self.checkBox_6, self.checkBox_7)):
                QtWidgets.QMessageBox.warning(None, 'Попередження', 'Виберіть хоча б один чекбокс!')

    def on_pushButton_4_clicked(self):
        if self.is_button_pressed:
            return
        self.is_button_pressed = True
        self.pushButton_6.setEnabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.start_process()
        self.aes_key_password()
        self.save_user_data()
        self.save_cloud_backup()

    def start_process(self):
        self.worker = BackupWorker()
        self.worker.progress.connect(self.progressBar_2.setValue)
        self.worker.start()

    def on_pushButton_6_clicked(self):
        if not self.lineEdit_4.text():
            self.get_file_path_for_key()
        else:
            print('Шлях вже вибрано!')
        if self.lineEdit_4.text():
            self.pushButton_5.setEnabled(True)
        else:
            print('Шлях до папки не обрано!')

    def on_pushButton_5_clicked(self):
        if not self.lineEdit_4.text():
            print('Будь ласка, виберіть папку для збереження файлу.')
            return
        self.pushButton_6.setDisabled(True)
        self.download_key()
        self.pushButton_5.setDisabled(True)
        self.pushButton_8.setEnabled(True)
        self.is_closable = True

    def get_file_path_for_key(self):
        folder_path = QtWidgets.QFileDialog.getExistingDirectory(None, 'Вибір папки')
        if folder_path:
            self.lineEdit_4.setText(folder_path)
        else:  # inserted
            print('Папка не була вибрана.')

    def download_key(self):
        download_directory = self.lineEdit_4.text()
        user_email = str(globals.user_email)
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        user_folder = os.path.join(project_dir, 'root', user_email)
        aes_file_path = os.path.join(user_folder, 'key.aes')

        if os.path.exists(aes_file_path):
            try:
                if not os.path.exists(download_directory):
                    os.makedirs(download_directory)

                base_name = 'key.aes'
                file_name, file_extension = os.path.splitext(base_name)
                counter = 1

                new_file_path = os.path.join(download_directory, base_name)
                while os.path.exists(new_file_path):
                    new_file_path = os.path.join(download_directory, f'{file_name}_{counter}{file_extension}')
                    counter += 1

                shutil.copy(aes_file_path, new_file_path)
                print(f'Key file downloaded to {new_file_path}')

                os.remove(aes_file_path)
                print(f'Deleted Fernet key file: {aes_file_path}')
            except Exception as e:
                print(f'Error downloading or deleting key file: {str(e)}')
        else:
            print(f'Файл з ключем не знайдений за адресою: {aes_file_path}')

    @staticmethod
    def aes_key_password():
        key = Fernet.generate_key()
        user_email = str(globals.user_email)
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        user_folder = os.path.join(project_dir, 'root', user_email)
        os.makedirs(user_folder, exist_ok=True)
        aes_file_path = os.path.join(user_folder, 'key.aes')

        with open(aes_file_path, 'wb') as f:
            f.write(key)

        print(f'Fernet Key (Saved to {aes_file_path}): {base64.urlsafe_b64encode(key).decode()}')

    def save_user_data(self):
        user_email = globals.user_email
        file_path = self.lineEdit_3.text()
        days = self.get_selected_days()
        backup_time = self.get_time()
        existing_data = []
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        root_dir = os.path.join(project_dir, 'root')
        user_dir = os.path.join(root_dir, user_email)
        os.makedirs(user_dir, exist_ok=True)
        filename = os.path.join(user_dir, 'backup.json')

        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    existing_data = json.load(f)
                    if not isinstance(existing_data, list):
                        existing_data = []
                except json.JSONDecodeError:
                    pass
        else:
            existing_data = []

        aes_file_path = os.path.join(user_dir, 'key.aes')
        key = None

        if os.path.exists(aes_file_path):
            with open(aes_file_path, 'rb') as f:
                key = f.read()
            print(f'Fernet Key (Loaded from {aes_file_path}): {base64.urlsafe_b64encode(key).decode()}')

        if key:
            encoded_key = base64.urlsafe_b64encode(key).decode()
        else:
            encoded_key = None

        new_entry = {
            'user_email': user_email,
            'backup_folder': file_path,
            'schedule_days': days,
            'schedule_time': backup_time,
            'date': datetime.today().strftime('%Y-%m-%d'),
            'password_hash': encoded_key
        }

        existing_data.append(new_entry)

        with open(filename, 'w') as f:
            json.dump(existing_data, f, indent=4)

    def save_cloud_backup(self):
        user_email = globals.user_email
        file_path = self.lineEdit_3.text()
        days = self.get_selected_days()
        backup_time = self.get_time()

        if not globals.user_authenticated:
            print("User is not authenticated.")
            return

        creds = globals.drive.auth.credentials
        drive_service = build("drive", "v3", credentials=creds)

        folder_name = "backups"
        folder_id = None
        query = f"name='{folder_name}' and mimeType='application/vnd.google-apps.folder' and trashed=false"
        response = drive_service.files().list(q=query, fields="files(id)").execute()

        if response.get("files"):
            folder_id = response["files"][0]["id"]
        else:
            folder_metadata = {"name": folder_name, "mimeType": "application/vnd.google-apps.folder"}
            folder = drive_service.files().create(body=folder_metadata, fields="id").execute()
            folder_id = folder["id"]

        file_name = "recovery.json"
        file_id = None
        query = f"name='{file_name}' and '{folder_id}' in parents and trashed=false"
        response = drive_service.files().list(q=query, fields="files(id)").execute()

        existing_data = []

        if response.get("files"):
            file_id = response["files"][0]["id"]

            request = drive_service.files().get_media(fileId=file_id)
            file_content = io.BytesIO()
            file_content.write(request.execute())
            file_content.seek(0)

            try:
                existing_data = json.load(file_content)
                if not isinstance(existing_data, list):
                    existing_data = []
            except json.JSONDecodeError:
                existing_data = []

        new_entry = {
            "user_email": user_email,
            "backup_folder": file_path,
            "schedule_days": days,
            "schedule_time": backup_time,
            "date": datetime.today().strftime("%Y-%m-%d")
        }

        existing_data.append(new_entry)

        file_stream = io.BytesIO(json.dumps(existing_data, indent=4).encode())
        media = MediaIoBaseUpload(file_stream, mimetype="application/json", resumable=True)

        if not file_id:
            file_metadata = {"name": file_name, "parents": [folder_id]}
            drive_service.files().create(body=file_metadata, media_body=media).execute()
            print("Файл 'recovery.json' успішно створено на Google Drive")
        else:
            drive_service.files().update(fileId=file_id, media_body=media).execute()
            print("Файл 'recovery.json' успішно оновлено на Google Drive")

class NewRuleWindow(QtWidgets.QMainWindow, Ui_new_rule_wind):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    new_rule_wind = QtWidgets.QMainWindow()
    ui = Ui_new_rule_wind()
    ui.setupUi(new_rule_wind)
    new_rule_wind.show()
    sys.exit(app.exec_())