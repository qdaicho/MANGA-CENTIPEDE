# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
# import manga_reader
import subprocess


class Ui_MainWindow(object):



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.go_to_centipede_reader())

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def go_to_centipede_reader(self):
        # self.window = QtWidgets.QMainWindow()
        # self.ui = Reader()
        # self.ui.setup(self.window)
        # MainWindow.hide()
        # self.window.show()
        # QtCore.QCoreApplication.exit()
        subprocess.Popen("python3 manga_reader.py", shell=True)
        # manga_reader.start_app()
        # start_app()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "WE ARE IN THE MAIN LIBRARY WINDOW. THIS IS STILL UNDER CONSTRUCTION."))
        self.pushButton.setText(_translate("MainWindow", "Go to Centipede Reader"))


if __name__ == "__main__":
    import sys  
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    fname="darkorange.txt"
    whole_text = ""
    with open(fname,'r') as f:
        # this way of reading the file gives a list of lines.
        data_text = f.readlines()
        # create a text out of the file
        whole_text =(' '.join(data_text))
    MainWindow.setStyleSheet(whole_text)
    
    
    MainWindow.show()
    sys.exit(app.exec_())
