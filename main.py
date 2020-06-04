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
import yaml
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

        self.searchBar.textChanged[str].connect(lambda: self.searchButton.setEnabled(self.searchBar.text() != ""))
        self.searchButton.clicked.connect(lambda: self.searchForManga())
        self.backButton.clicked.connect(lambda: self.goToSearchPage())
        self.downloadChaptersButton.clicked.connect(lambda: self.downloadManga())

        self.crawler = MangakisaCrawler()

    def downloadManga(self):
        number_of_chapters = self.chapterNumberSpinBox.value()
        if number_of_chapters > 0:
            self.crawler.downloadChaptersAndOrganize(self.manga_info, self.manga_info.get("Title"), 
                    self.manga_info.get("Chapter Links"), self.manga_info.get("Poster"), number_of_chapters)

    def goToSearchPage(self):
        self.browseStackedWidget.setCurrentIndex(0)
    # This function is going to populate the search results with the search
    # term
    def goToInfoPage(self, manga_url, image_path):
        self.manga_info = self.crawler.getMangaInfo(manga_url)
        # pprint(self.manga_info)
        self.browseStackedWidget.setCurrentIndex(1)
        self.clearLayout(self.chapterListGridLayout)
        self.chapterNumberSpinBox.setMaximum(int(self.manga_info["Total Chapters"]))

        text = '''
            <div>
            <div><img src="{0}"  width="235" height="300" style=" float:left; padding:30px"></div>
            <div style="margin-left:260px; margin-right:40px;">
                <h4>{1}</h4>
                <p style="color:darkgrey;font-size:11px;">{2}</p>
                <div style="font-size:10px;">
                    <b style="color:darkgrey;">Categories: </b><i style="color:#ffa02f;">{3}</i>
                    <br><br>
                    <b style="color:darkgrey;">Authors: </b> <i style="color:#ffa02f;">{4}</i>
                    <br><br>
                    <b style="color:darkgrey;">Status: </b> <i style="color:#ffa02f;">{5}</i>
                    <br><br>
                    <b style="color:darkgrey;">Chapters: </b> <i style="color:#ffa02f;">{6}</i>
                </div>
                <div>
                </div>
            </div>
        '''.format(image_path, self.manga_info["Title"],
            self.manga_info["Description"], ", ".join(self.manga_info["Categories"]),
            self.manga_info["Author"],self.manga_info["Status"],self.manga_info["Total Chapters"])

        self.infoLabel.setText(text)

        self.chapter_label = [QLabel2() for i in range(int(self.manga_info["Total Chapters"]))]
        # pprint(self.chapter_label)
        # print(len(self.chapter_label))

        x = 0
        y = 0
        for i in range(len(self.chapter_label)):               
            self.chapter_label[i] = QLabel2()
            self.chapter_label[i].setTextFormat(QtCore.Qt.RichText)
            self.chapter_label[i].setText("""<h5><br>chapter_{}<br></h5>""".format(str(i+1)))
            self.chapter_label[i].setAlignment(QtCore.Qt.AlignCenter)
            self.chapter_label[i].setWordWrap(True)
            self.chapter_label[i].setFrameShape(QtWidgets.QFrame.Box)
            self.chapter_label[i].setFrameShadow(QtWidgets.QFrame.Raised)
            self.chapter_label[i].setLineWidth(1)
            self.chapter_label[i].setStyleSheet("QLabel::hover{background-color : #4a4848;}")
            self.vLayoutForResults.addWidget(self.chapter_label[i]) 
            # self.chapter_label[-1].clicked.connect()
            # print("x: {}\n y:{}".format(str(x), str(y)))
            self.chapterListGridLayout.addWidget(self.chapter_label[i], x, y)

            if y < 2:
                y+=1
            else:
                y = 0
                x+=1


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
            self.searchButton.animateClick();
            # self.searchForManga()
        elif event.key() == QtCore.Qt.Key_S:
            self.searchBar.setFocus()

    def searchForManga(self):
        if self.searchBar.text() != "":
            self.clearFolder(os.path.join(os.getcwd(), os.path.join("resrc", "temp")))
            # rm anything that isn't letter or space char
            search_term = re.sub(r'[^a-zA-Z\d\s]', u'', self.searchBar.text(), flags=re.UNICODE) 
            # print(search_term)
            self.clearLayout(self.vLayoutForResults)
            self.populateSearchResults(search_term)


    def populateSearchResults(self, search_term):
        manga_previews = self.crawler.getSearchResults(search_term)
        self.searchBar.setEnabled(False)
        self.searchButton.setEnabled(False)
        # pprint(manga_previews)
        self.results_label = []

        if len(manga_previews.keys()) > 20:
            total_iterations = 20
        else:
            total_iterations = len(manga_previews.keys())

        self.downloadProgress.setMaximum(total_iterations)

        for i in range(total_iterations):
            self.results_label.append(QLabel2())
        
        # print(len(self.results_label))

            title = list(manga_previews.keys())[i]   
            status = manga_previews[title][2]
            categories = manga_previews[title][3]
            

            if 'Search Not Found' in manga_previews.keys():
                image_path = os.path.join(os.getcwd(), os.path.join("resrc", "404.png"))
            else:
                url = manga_previews[title][1]
                page = requests.get(url)
                extension = self.get_ext(manga_previews[title][1])
                f_name = '{0}{1}'.format(i,extension)
            # print(f_name)
                x = os.path.join(os.getcwd(), os.path.join("resrc", os.path.join("temp", f_name)))
                with open(x, 'wb') as f:
                    f.write(page.content)

                # image_path = os.path.join(x, "{0}{1}".format(i, extension))
                image_path = x
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

            # self.results_label[-1] = QLabel2()
            self.results_label[-1].setText(text)
            # self.results_label[-1].setAlignment(QtCore.Qt.AlignCenter)
            self.results_label[-1].setWordWrap(True)
            self.results_label[-1].setTextFormat(QtCore.Qt.RichText)
            self.results_label[-1].setFrameShape(QtWidgets.QFrame.Box)
            self.results_label[-1].setFrameShadow(QtWidgets.QFrame.Raised)
            self.results_label[-1].setLineWidth(1)
            self.results_label[-1].setStyleSheet("QLabel::hover{background-color : #4a4848;}")
            self.vLayoutForResults.addWidget(self.results_label[-1]) 
            self.results_label[-1].clicked.connect(
                lambda link=manga_previews[title][0], p =image_path: self.goToInfoPage(link, p))
            self.downloadProgress.setValue(i+1)
        self.searchBar.clear()
        self.searchBar.setEnabled(True)
        self.searchButton.setEnabled(True)
        self.downloadProgress.reset()

    def openLibrary(self):
        pass


    def yaml_loader(self, filepath):
        """loads a YAML FILE"""
        with open(filepath, "r") as filedescriptor:
            data = yaml.safe_load(filedescriptor)
        return data

    def yaml_dump(self, filepath, data):
        """dumps data to a yaml file"""
        with open(filepath, "w") as filedescriptor:
            yaml.safe_dump(data, filedescriptor)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    showMain = Main()

    sizeObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
    w = int(sizeObject.width()/2)
    h = int(sizeObject.height())
    showMain.resize(w, h)

    showMain.show()
    sys.exit(app.exec_())
