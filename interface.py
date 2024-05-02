from PyQt5.QtWidgets import QDialog


from PyQt5 import QtCore, QtGui, QtWidgets


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(646, 439)
        Dialog.setStyleSheet("QLabel#label{\n"
                             "font: 24pt \"MS Shell Dlg 2\";\n"
                             "}\n"
                             "QDialog#Dialog{\n"
                             "background-color: rgb(164, 236, 255);\n"
                             "}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 581, 391))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Для работы с приложением.\n"
                                      " Введите в поле ввода текст вашего\n"
                                      " запроса. Нажмите кнопку отправить\n"
                                      " для отправки запроса."))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1072)
        MainWindow.setMaximumSize(QtCore.QSize(1920, 1085))
        MainWindow.setMouseTracking(False)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("QPushButton#pushButton\n"
                                 "{\n"
                                 "    background-color:#ff6969;\n"
                                 "    border-radius: 70px;\n"
                                 "    font: 75 28pt \"MS Shell Dlg 2\";\n"
                                 "}\n"
                                 "QPlainTextEdit#plainTextEdit{\n"
                                 "     background-color:#fec6d0;\n"
                                 "    font: 18pt \"MS Shell Dlg 2\";\n"
                                 "    padding:40px;\n"
                                 "       border-radius: 70px;\n"
                                 "}\n"
                                 "QMainWindow#MainWindow{\n"
                                 "    background-color:#b2d0d5\n"
                                 "}\n"
                                 "QWidget#centralwidget{\n"
                                 "    background-color:#b2d0d5\n"
                                 "}\n"
                                 "QColumnView#columnView{\n"
                                 "    background-color:#b2d0d5;\n"
                                 "}\n"
                                 "QAbstractItemView::item {\n"
                                 "    color: red;\n"
                                 "}\n"
                                 "QListView\n { background-color: #b2d0d5; font: 18pt \"MS Shell Dlg 2\"; \n min-width: 1600px;\n min-height: 600px;\n }")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 820, 1201, 192))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setMinimumSize(QtCore.QSize(1200, 100))
        self.plainTextEdit.setMaximumSize(QtCore.QSize(1400, 200))
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1570, 850, 300, 150))
        self.pushButton.setMinimumSize(QtCore.QSize(300, 150))
        self.pushButton.setMaximumSize(QtCore.QSize(300, 150))
        self.pushButton.setObjectName("pushButton")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(30, 20, 1861, 771))
        self.columnView.setObjectName("columnView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.action.triggered.connect(lambda: self.help_pressed())
        self.retranslateUi(MainWindow)
        self.dialogue_window = MyDialog()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Send"))
        self.menu.setTitle(_translate("MainWindow", "File"))
        self.action.setText(_translate("MainWindow", "Помощь (F1)"))
        self.action.setStatusTip(_translate(
            "MainWindow", "Открыть меню помощи"))
        self.action.setShortcut(_translate("MainWindow", "F1"))

    def help_pressed(self, *args):
        self.dialogue_window.open()
