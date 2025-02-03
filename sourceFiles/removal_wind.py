import os
import sys
import json
from datetime import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import globals

class Ui_removal_wind(object):

    def __init__(self):
        self.choice_wind = None
        self.pushButton_4 = None
        self.textBrowser_3 = None
        self.statusbar = None
        self.menubar = None
        self.pushButton = None
        self.textBrowser_2 = None
        self.textBrowser = None
        self.comboBox = None
        self.centralwidget = None

    def setupUi(self, removal_wind):
        removal_wind.setObjectName('SecureCloudAutoBackup')
        removal_wind.setFixedSize(700, 400)
        removal_wind.setStyleSheet('background-color: rgb(167, 194, 196);')
        icon = QtGui.QIcon()
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(project_dir, 'logo.png')
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        removal_wind.setWindowIcon(icon)

        self.centralwidget = QtWidgets.QWidget(removal_wind)
        self.centralwidget.setObjectName('centralwidget')

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(45, 180, 610, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName('comboBox')
        scenario_handler = ScenarioHandler(globals.user_email)
        scenario_handler.populate_combobox(self.comboBox)

        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(45, 70, 600, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser.setFont(font)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setObjectName('textBrowser')

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

        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(58, 130, 260, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(10)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName('textBrowser_2')

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 260, 250, 50))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(lambda: scenario_handler.delete_scenario(self.comboBox))

        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(440, 335, 250, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(7)
        font.setItalic(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setObjectName('textBrowser_3')

        removal_wind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(removal_wind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 478, 18))
        self.menubar.setObjectName('menubar')
        removal_wind.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(removal_wind)
        self.statusbar.setObjectName('statusbar')
        removal_wind.setStatusBar(self.statusbar)

        self.retranslateUi(removal_wind)

        QtCore.QMetaObject.connectSlotsByName(removal_wind)

    def retranslateUi(self, removal_wind):
        _translate = QtCore.QCoreApplication.translate
        removal_wind.setWindowTitle(_translate('removal_wind', 'removal_wind'))
        self.textBrowser.setHtml(_translate('removal_wind', '<html><body><p align="center">'
                                                            'Переглянути або видалити створені сценарії</p></body></html>'))
        self.textBrowser_2.setHtml(_translate('removal_wind', '<html><body><p align="left">'
                                                              'Виберіть сценарій</p></body></html>'))
        self.pushButton.setText(_translate('removal_wind', 'Видалити сценарій'))
        self.textBrowser_3.setHtml(_translate('removal_wind', '<html><body><p align="right">'
                                                              'SecureCloudAutoBackupProject<br>'
                                                              'by well-wisher</p></body></html>'))
        self.pushButton_4.setText(_translate('removal_wind', 'Назад'))

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

class ScenarioHandler:

    def __init__(self, user_email):
        self.user_email = user_email

    def get_backup_file_path(self):
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        root_folder = "root"
        user_folder = os.path.join(project_dir, root_folder, self.user_email)
        backup_file_path = os.path.join(user_folder, "backup.json")
        return backup_file_path

    def load_scenarios_from_backup(self):
        backup_file_path = self.get_backup_file_path()
        if not os.path.exists(backup_file_path):
            raise FileNotFoundError(f"Файл {backup_file_path} не знайдено.")

        with open(backup_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data

    def save_scenarios_to_backup(self, scenarios):
        backup_file_path = self.get_backup_file_path()
        with open(backup_file_path, 'w', encoding='utf-8') as file:
            json.dump(scenarios, file, indent=4, ensure_ascii=False)

    def format_scenario_data(self, scenario=None):
        folder_name = scenario.get('backup_folder', 'Невідома папка')
        schedule_days = scenario.get('schedule_days', [])
        schedule_time = scenario.get('schedule_time', '')
        date = scenario.get('date', 'Невідома дата')

        formatted_days = ', '.join(schedule_days) if schedule_days else 'Невідомі дні'

        try:
            formatted_time = datetime.strptime(schedule_time, '%H:%M:%S').strftime('%H:%M:%S')
        except ValueError:
            formatted_time = 'Невідомий час'

        formatted_date = f"д.с. {date}"

        return f"{folder_name} - {formatted_days} - {formatted_time} - {formatted_date}"

    def populate_combobox(self, comboBox):
        try:
            scenarios = self.load_scenarios_from_backup()
            for scenario in scenarios:
                formatted_data = self.format_scenario_data(scenario)

                comboBox.addItem(formatted_data)
        except FileNotFoundError as e:
            print(e)

    def delete_scenario(self, comboBox):
        selected_index = comboBox.currentIndex()
        if selected_index == -1:
            self.show_message("Помилка", "Не обрано сценарій для видалення.")
        else:
            scenarios = self.load_scenarios_from_backup()
            selected_scenario = scenarios[selected_index]

            del scenarios[selected_index]
            self.save_scenarios_to_backup(scenarios)
            self.show_message("Успіх", f"Сценарій '{selected_scenario['backup_folder']}' був успішно видалений.")

    @staticmethod
    def show_message(title, message):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

class RemovalWindow(QtWidgets.QMainWindow, Ui_removal_wind):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    removal_wind = QtWidgets.QMainWindow()
    ui = Ui_removal_wind()
    ui.setupUi(removal_wind)
    removal_wind.show()
    sys.exit(app.exec_())
