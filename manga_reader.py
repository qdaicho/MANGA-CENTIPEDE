# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'image_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import re
import os
import pprint
import os.path
import time
import sys
# from configparser import ConfigParser
import yaml

EXIT_CODE_REBOOT = -11231351


class Reader(QtWidgets.QWidget):

    def setup(self, MainWindow):
        #######################################################################
        MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        # MAIN WINDOW SETUP AND LAYOUT
        #######################################################################
        self.topHorizontalLayout = QtWidgets.QHBoxLayout()
        self.topHorizontalLayout.setObjectName("topHorizontalLayout")

        self.backToLibraryButton = QtWidgets.QPushButton(self.centralwidget)
        self.backToLibraryButton.setObjectName("backToLibraryButton")
        self.topHorizontalLayout.addWidget(self.backToLibraryButton, alignment=QtCore.Qt.AlignLeft)
        self.backToLibraryButton.setFixedWidth(50)



        self.hlay1 = QtWidgets.QHBoxLayout()
        self.hlay1.setObjectName("hlay1")

        self.toggle_hbar = QtWidgets.QRadioButton("HScroll")
        self.toggle_hbar.setChecked(False)
        self.toggle_hbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.toggle_hbar.toggled.connect(lambda: self.fix_horizontal_scrolling())
        self.toggle_hbar.setToolTip("Enable or disable horizontal scroll bar")
        self.topHorizontalLayout.addWidget(self.toggle_hbar)


        self.zoomOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomOutButton.setObjectName("zoomOutButton")
        self.zoomOutButton.clicked.connect(lambda: self.zoomfunc(3))
        self.zoomOutButton.setFixedWidth(30)

        self.zoomComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.zoomComboBox.setEditable(False)
        self.zoomComboBox.setObjectName("zoomComboBox")
        self.zoom_options_list = ['30%', '50%', '100%', '130%', '200%', '500%', '']
        self.zoomComboBox.addItems(self.zoom_options_list)
        self.zoomComboBox.setCurrentIndex(2)
        self.zoomComboBox.currentTextChanged.connect(lambda: self.zoomfunc(1))
        self.zoomComboBox.setFixedWidth(85)

        self.zoomInButton = QtWidgets.QPushButton(self.centralwidget)
        self.zoomInButton.setObjectName("zoomInButton")
        self.zoomInButton.clicked.connect(lambda: self.zoomfunc(2))
        self.zoomInButton.setFixedWidth(30)

        # self.hlay1.addWidget(self.toggle_hbar)
        self.hlay1.addWidget(self.zoomOutButton)      
        self.hlay1.addWidget(self.zoomComboBox)
        self.hlay1.addWidget(self.zoomInButton)
        self.topHorizontalLayout.addLayout(self.hlay1)

        self.verticalLayout.addLayout(self.topHorizontalLayout)
        # ATTACH TOP NAVIGATION BAR
        #######################################################################
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Box)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        self.scrollArea.setLineWidth(2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()#################################  THIS SHIT WASN'T EVEN NECESSARY
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 774, 508))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)

        self.hbar = self.scrollArea.horizontalScrollBar()

        # ATTACH MIDDLE SCROLL AREA FOR MANGA READING
        #######################################################################
        content_widget = QtWidgets.QWidget()
        self.scrollArea.setWidget(content_widget)
        self.image_viewer_layout = QtWidgets.QVBoxLayout(content_widget)

        # self.config = ConfigParser()
        # self.config.read('config.ini')
        # # self.config.set('main', 'a', 'orange')#set key-value pair in section main
        # with open('config.ini', 'w') as f:
        #     self.config.write(f)

        self.data = self.yaml_loader('config.yaml')
        # print(self.data)

        # url = "/home/emsee/Documents/Manga/Tokyo Ghoul/chapter_3"
        url = os.path.join(os.getcwd(),self.data.get('chapter_url'))
        # print(url)

        #used once in bottom nav bar to set combo box text
        self.current_chap = re.search(r'chapter_(\d+)', url).group(0)
        # print(self.current_chap)

        # gets all the images from given url
        self.image_url_list = self.sorted_nicely(
            [os.path.join(url, file) for file in os.listdir(url)])
        self.image_url_list = self.image_url_list[1:-1]
        # p# print.pprint(self.image_url_list)

        self.hundred_percent_zoom = 730
        self.zoomValue = 100

        self.counter = 0  # This counts the pages as window gets populated w/ images
        self.image_pixmap_list = []
        self.image_label_list = []
        for i in range(len(self.image_url_list)):
            self.image_label_list.append(QtWidgets.QLabel())

        # print(str(self.hundred_percent_zoom))
        self.populate_img(self.hundred_percent_zoom, self.hundred_percent_zoom, False)

        # STILL UNDER CONSTRUCTION
        #######################################################################

        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")

        self.mangaChapterComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.mangaChapterComboBox.setEditable(False)
        self.mangaChapterComboBox.setStyleSheet("combobox-popup: 0;");
        self.mangaChapterComboBox.setObjectName("mangaChapterComboBox")
        self.bottomHorizontalLayout.addWidget(self.mangaChapterComboBox)
        self.manga_chapter_list = [f for f in sorted(os.listdir(re.search(r'.+?(?=chapter_(\d+))', url).group(0)))]
        self.manga_chapter_list = self.sorted_nicely(self.manga_chapter_list)
        self.mangaChapterComboBox.addItems(self.manga_chapter_list)
        self.mangaChapterComboBox.setCurrentIndex(self.manga_chapter_list.index(self.current_chap))
        self.mangaChapterComboBox.currentTextChanged.connect(lambda: self.restartApp(" "))


        self.lastChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.lastChapterButton.setObjectName("lastChapterButton")
        self.bottomHorizontalLayout.addWidget(self.lastChapterButton)

        lastIndex = 0
        if self.manga_chapter_list.index(self.current_chap)-1 <= 0:
            pass
        else:
            lastIndex = self.manga_chapter_list.index(self.current_chap)-1

        lastChapURL = self.data.get('chapter_url').replace(self.current_chap, self.manga_chapter_list[lastIndex])
        self.lastChapterButton.clicked.connect(lambda: self.restartApp(lastChapURL))


        self.verticalLayout.addLayout(self.bottomHorizontalLayout)

        self.nextChapterButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextChapterButton.setObjectName("nextChapterButton")
        self.bottomHorizontalLayout.addWidget(self.nextChapterButton)

        nextIndex = 0
        if self.manga_chapter_list.index(self.current_chap)+1 >= len(self.manga_chapter_list):
            pass
        else:
            nextIndex = self.manga_chapter_list.index(self.current_chap)+1

        nextChapURL = self.data.get('chapter_url').replace(self.current_chap, self.manga_chapter_list[nextIndex])
        self.nextChapterButton.clicked.connect(lambda: self.restartApp(nextChapURL))



        # ATTACH BOTTOM NAVIGATION BAR
        #######################################################################
        MainWindow.setCentralWidget(self.centralwidget)
        # MainWindow.showMaximized()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # UI TRANSLATE
        #######################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Manga Centipede Reader"))
        self.backToLibraryButton.setText(
            _translate("MainWindow", "\tBack\t"))
        self.zoomOutButton.setText(_translate("MainWindow", "-"))
        self.zoomInButton.setText(_translate("MainWindow", "+"))
        self.nextChapterButton.setText(
            _translate("MainWindow", "Next Chapter"))
        self.lastChapterButton.setText(
            _translate("MainWindow", "Last Chapter"))

    def yaml_loader(self, filepath):
        """loads a YAML FILE"""
        with open(filepath, "r") as filedescriptor:
            data = yaml.safe_load(filedescriptor)
        return data

    def yaml_dump(self, filepath, data):
        """dumps data to a yaml file"""
        with open(filepath, "w") as filedescriptor:
            yaml.safe_dump(data, filedescriptor)

    def sorted_nicely(self, l):
        """ Sort the given iterable in the way that humans expect."""
        convert = lambda text: int(text) if text.isdigit() else text
        alphanum_key = lambda key: [convert(c)
                                    for c in re.split('([0-9]+)', key)]
        return sorted(l, key=alphanum_key)

    def fix_horizontal_scrolling(self):
        if self.toggle_hbar.isChecked() == True:
            self.hbar.setDisabled(True)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        else:
            self.hbar.setDisabled(False)
            self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)

    def zoomfunc(self, widget_input):
        #type 1 for comboinput, 2 for zoomInButton input, 3 for zoomOutButton input
        if widget_input == 1:
            self.zoomValue = int(self.zoomComboBox.currentText().strip('%'))
            # print("just zoomed from comboinput: " + str(self.zoomValue))
            zoomDimensions = int(self.hundred_percent_zoom*(self.zoomValue/100))
            self.populate_img(zoomDimensions, zoomDimensions, True)
        elif widget_input == 2:
            self.zoomValue = self.zoomValue + 25
            self.zoomComboBox.setItemText(6, str(self.zoomValue) + '%')
            self.zoomComboBox.setCurrentIndex(6)
        else:
            self.zoomValue = self.zoomValue - 25
            self.zoomComboBox.setItemText(6, str(self.zoomValue) + '%')
            self.zoomComboBox.setCurrentIndex(6)

    def populate_img(self, width, height, update):

        if update == True:

            for label in self.image_label_list:
                label.clear()

            total_pages = len(self.image_url_list)
            for i in range(len(self.image_url_list)):
                pic = self.image_pixmap_list[i].scaled(
                    width, height, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
                self.image_label_list[i].setPixmap(pic)
                time.sleep(.001)
                self.image_label_list[i].setAlignment(QtCore.Qt.AlignCenter)
                self.image_label_list[i].setStyleSheet("QLabel {background-color: black;}")
                self.image_label_list[i].setToolTip('Page: ' + str(i+1) + "/" + str(total_pages))
                self.image_label_list[i].setToolTipDuration(500)
                self.image_viewer_layout.addWidget(self.image_label_list[i])
        elif update == False:

            for image in self.image_url_list:
                self.image_pixmap_list.append(QtGui.QPixmap(image, str(self.counter)))

            # if len(self.image_pixmap_list) == len(self.image_url_list):
            #     p# print.pprint(self.image_pixmap_list)
            total_pages = len(self.image_url_list)
            for i in range(len(self.image_url_list)):
                pic = self.image_pixmap_list[i].scaled(
                    width, height, QtCore.Qt.KeepAspectRatio, transformMode = QtCore.Qt.SmoothTransformation)
                self.image_label_list[i].setPixmap(pic)
                time.sleep(.001)
                self.image_label_list[i].setAlignment(QtCore.Qt.AlignCenter)
                self.image_label_list[i].setStyleSheet("QLabel {background-color: black;}")
                self.image_label_list[i].setToolTip('Page: ' + str(i+1) + "/" + str(total_pages))
                self.image_label_list[i].setToolTipDuration(500)
                self.image_viewer_layout.addWidget(self.image_label_list[i])

    def restartApp(self, chapter_url_plus_number):
        if chapter_url_plus_number == " ":
            chapter_url_plus_number =  self.data.get('chapter_url').replace(self.current_chap, self.mangaChapterComboBox.currentText())
        # print(chapter_url_plus_number)
        self.data["chapter_url"] = chapter_url_plus_number        
        self.yaml_dump("config.yaml", self.data)
        # os.execv(sys.executable, ['python3'] + sys.argv)
        return QtCore.QCoreApplication.exit( EXIT_CODE_REBOOT )          
 




    # CLASS FUNCTION AND UTILITY FUNCTION DECLARATION
    ##########################################################################

def start_app():

    exit_code = 0

    try:
        app = QtWidgets.QApplication(sys.argv)
    except RuntimeError:
        app = QtCore.QCoreApplication.instance()
        
    while True:   

        MainWindow = QtWidgets.QMainWindow()
        ui = Reader()
        ui.setup(MainWindow)

        sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        w = int(sizeObject.width()/2)
        h = int(sizeObject.height())
        MainWindow.resize(w, h)

        MainWindow.show()

        fname="darkorange.txt"
        whole_text = ""
        with open(fname,'r') as f:
            # this way of reading the file gives a list of lines.
            data_text = f.readlines()
            # create a text out of the file
            whole_text =(' '.join(data_text))
        MainWindow.setStyleSheet(whole_text)
        exit_code = app.exec_()            
        if exit_code != EXIT_CODE_REBOOT:
            break        
    return exit_code

if __name__ == "__main__":
    start_app()
    # print("we are out of the application")

