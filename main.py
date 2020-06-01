from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys
import os
from kisa import MangakisaCrawler
from pprint import pprint
import requests
from urllib.parse import urlparse
from os.path import splitext
import re
from configparser import ConfigParser
from mainwindow import Ui_MainWindow, QLabel2


class Main(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        fname = "darkorange.txt"
        whole_text = ""
        with open(fname, 'r') as f:
            # this way of reading the file gives a list of lines.
            data_text = f.readlines()
            # create a text out of the file
            whole_text = (' '.join(data_text))

        self.setStyleSheet(whole_text)

    #     self.PushButton1.clicked.connect(self.OpenWindow1)
    #     self.PushButton2.clicked.connect(self.OpenWindow2)

    #     self.PushButton3.clicked.connect(self.GoToMain)
    #     self.PushButton4.clicked.connect(self.OpenWindow2)

    #     self.PushButton5.clicked.connect(self.GoToMain)
    #     self.PushButton6.clicked.connect(self.OpenWindow1)
        self.searchButton.clicked.connect(lambda: self.searchForManga())

        self.crawler = MangakisaCrawler()

    # This function is going to populate the search results with the search
    # term
    def click(self):
        print("clicked")
        # self.browseStackedWidget.setCurrentIndex(1)

    """THIS FUNCTION CLEARS ALL THE WIDGETS IN A LAYOUT"""

    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def clearFolder(self, path):
        for root, dirs, files in os.walk(path):
            for file in files:
                os.remove(os.path.join(root, file))

    def get_ext(self, url):
        """Return the filename extension from url, or ''."""
        parsed = urlparse(url)
        root, ext = splitext(parsed.path)
        return ext  # or ext[1:] if you don't want the leading '.'

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.searchForManga()
        elif event.key() == QtCore.Qt.Key_S:
            self.searchBar.setFocus()

    def searchForManga(self):
        self.clearFolder(os.getcwd() + "/resrc/temp/")
        # rm anything that isn't letter or space char
        search_term = re.sub(r'[^a-zA-Z\d\s]', u'', self.searchBar.text(), flags=re.UNICODE) 
        # print(search_term)
        self.clearLayout(self.vLayoutForResults)
        self.populateSearchResults(search_term)


    def populateSearchResults(self, search_term):
        manga_previews = self.crawler.getSearchResults(search_term)
        pprint(manga_previews)
        self.results_label = []

        if len(manga_previews.keys()) > 20:
            total_iterations = 20
        else:
            total_iterations = len(manga_previews.keys())

        for i in range(total_iterations):
            self.results_label.append(QtWidgets.QLabel())
        
        # print(len(self.results_label))

            title = list(manga_previews.keys())[i]   
            status = manga_previews[title][2]
            categories = manga_previews[title][3]
            

            if 'Search Not Found' in manga_previews.keys():
                image_path = os.getcwd() + "/resrc/404.png"
            else:
                url = manga_previews[title][1]
                page = requests.get(url)
                extension = self.get_ext(manga_previews[title][1])
                f_name = '{0}{1}'.format(i,extension)
            # print(f_name)
                with open(os.getcwd() + "/resrc/temp/" + f_name, 'wb') as f:
                    f.write(page.content)

                image_path = os.getcwd() + "/resrc/temp/{0}{1}".format(i, extension)
            # print(image_path)
            
            text = '''
                <div>
                   <div>
                      <img src="{0}" width="110" height="135" style=" float:left;">
                   </div>
                   <div style=" margin-left:150px;">
                      <h4>{1}</h4>
                      <h5><span style="color: darkgrey;"><strong>{2}</strong></span></h5>
                      <h5 style="color: #ffa02f;"><i>{3}</i></h5>
                   </div>
                </div>
        '''.format(image_path, title, status, categories)

            self.results_label[-1] = QLabel2()
            self.results_label[-1].setText(text)
            # self.results_label[-1].setAlignment(QtCore.Qt.AlignCenter)
            self.results_label[-1].setWordWrap(True)
            self.results_label[-1].setTextFormat(QtCore.Qt.RichText)
            self.results_label[-1].setFrameShape(QtWidgets.QFrame.Box)
            self.results_label[-1].setFrameShadow(QtWidgets.QFrame.Raised)
            self.results_label[-1].setLineWidth(1)
            self.results_label[-1].setStyleSheet("QLabel::hover{background-color : #4a4848;}")
            self.vLayoutForResults.addWidget(self.results_label[-1])
            # labelRT.clicked.connect(lambda: self.click())
    def openLibrary(self):
        pass
    # def OpenWindow1(self):
    #     self.QtStack.setCurrentIndex(1)

    # def OpenWindow2(self):
    #     self.QtStack.setCurrentIndex(2)

    # def GoToMain(self):
    #     self.QtStack.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()
    showMain.show()
    # showMain.populateSearchResults("terror man")

    sys.exit(app.exec_())
