import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_choice_wind(object):

    def __init__(self):
        self.main_wind = None
        self.pushButton_4 = None
        self.extract_wind = None
        self.removal_wind = None
        self.new_rule_wind = None
        self.textBrowser_2 = None
        self.statusbar = None
        self.menubar = None
        self.pushButton_3 = None
        self.pushButton_2 = None
        self.pushButton = None
        self.textBrowser = None
        self.centralwidget = None

    def setupUi(self, choice_wind):
        choice_wind.setObjectName('SecureCloudAutoBackup')
        choice_wind.setFixedSize(710, 450)
        choice_wind.setStyleSheet('background-color: rgb(167, 194, 196);')
        icon = QtGui.QIcon()
        project_dir = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
        icon_path = os.path.join(project_dir, 'logo.png')
        icon.addPixmap(QtGui.QPixmap(icon_path), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        choice_wind.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(choice_wind)
        self.centralwidget.setObjectName('centralwidget')
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(70, 20, 550, 150))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(16)
        font.setBold(True)
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
        self.pushButton_4.clicked.connect(self.back_to_main_window)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(440, 380, 250, 80))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(7)
        font.setItalic(True)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setObjectName('textBrowser_3')
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 690, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton.setObjectName('pushButton')
        self.pushButton.clicked.connect(self.get_open_new_rule_window)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 160, 690, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_2.setObjectName('pushButton_2')
        self.pushButton_2.clicked.connect(self.get_open_removal_window)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 230, 690, 40))
        font = QtGui.QFont()
        font.setFamily('Cambria')
        font.setPointSize(11)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet('color: rgb(167, 194, 196);\nbackground-color: rgb(15, 71, 98);')
        self.pushButton_3.setObjectName('pushButton_3')
        self.pushButton_3.clicked.connect(self.get_open_extract_window)
        choice_wind.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(choice_wind)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 18))
        self.menubar.setObjectName('menubar')
        choice_wind.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(choice_wind)
        self.statusbar.setObjectName('statusbar')
        choice_wind.setStatusBar(self.statusbar)
        self.retranslateUi(choice_wind)
        QtCore.QMetaObject.connectSlotsByName(choice_wind)

    def retranslateUi(self, choice_wind):
        _translate = QtCore.QCoreApplication.translate
        choice_wind.setWindowTitle(_translate('choice_wind', 'choice_wind'))
        self.textBrowser.setHtml(_translate('choice_wind', '<html><body><p align="center">Оберіть дію</p></body></html>'))
        self.textBrowser_2.setHtml(_translate('choice_wind', '<html><body><p align="right">SecureCloudAutoBackupProject<br>by well-wisher</p></body></html>'))
        self.pushButton.setText(_translate('choice_wind', 'Створити нове правило для резервного копіювання'))
        self.pushButton_2.setText(_translate('choice_wind', 'Переглянути або видалити наявні правила резервного копіювання'))
        self.pushButton_3.setText(_translate('choice_wind', 'Видобути дані з реервної копії'))
        self.pushButton_4.setText(_translate('choice_wind', 'Назад'))

    def get_open_new_rule_window(self):
        from new_rule_wind import NewRuleWindow
        self.new_rule_wind = NewRuleWindow()
        self.new_rule_wind.show()
        self.close_this_window()

    def get_open_removal_window(self):
        from removal_wind import RemovalWindow
        self.removal_wind = RemovalWindow()
        self.removal_wind.show()
        self.close_this_window()

    def get_open_extract_window(self):
        from extract_wind import ExtractWindow
        self.extract_wind = ExtractWindow()
        self.extract_wind.show()
        self.close_this_window()

    def back_to_main_window(self):
        from main_wind import MainWindow
        self.main_wind = MainWindow()
        self.main_wind.show()
        self.close_this_window()

    def close_this_window(self):
        main_window = QtWidgets.QApplication.activeWindow()
        if main_window:
            main_window.close()

class ChoiceWindow(QtWidgets.QMainWindow, Ui_choice_wind):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    choice_wind = QtWidgets.QMainWindow()
    ui = Ui_choice_wind()
    ui.setupUi(choice_wind)
    choice_wind.show()
    sys.exit(app.exec_())