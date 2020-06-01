#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class QLabel2(QtWidgets.QLabel):
    clicked = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(765, 580)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.navMenu = QtWidgets.QTabWidget(self.centralwidget)
        self.navMenu.setEnabled(True)
        font = QtGui.QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.navMenu.setFont(font)
        self.navMenu.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.navMenu.setMouseTracking(False)
        self.navMenu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.navMenu.setAutoFillBackground(False)
        self.navMenu.setStyleSheet("")
        self.navMenu.setTabPosition(QtWidgets.QTabWidget.North)
        self.navMenu.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.navMenu.setObjectName("navMenu")
        self.browseMangaTab = QtWidgets.QWidget()
        self.browseMangaTab.setObjectName("browseMangaTab")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.browseMangaTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.browseStackedWidget = QtWidgets.QStackedWidget(
            self.browseMangaTab)
        self.browseStackedWidget.setObjectName("browseStackedWidget")

        #STACKED WIDGET SETUP###############################################
        self.searchPage = QtWidgets.QWidget()
        self.infoPage = QtWidgets.QWidget()

        self.searchWindow()
        self.infoWindow()

        self.browseStackedWidget.addWidget(self.searchPage)
        self.browseStackedWidget.addWidget(self.infoPage)
        ####################################################################

        self.verticalLayout_2.addWidget(self.browseStackedWidget)

        self.navMenu.addTab(self.browseMangaTab, "")
        self.settingsTab = QtWidgets.QWidget()
        self.settingsTab.setObjectName("settingsTab")
        self.navMenu.addTab(self.settingsTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.navMenu.addTab(self.aboutTab, "")
        self.gridLayout.addWidget(self.navMenu, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 765, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.navMenu.setCurrentIndex(0)
        self.browseStackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def searchWindow(self):
        self.searchPage.setObjectName("searchPage")
        self.searchPageVLayout = QtWidgets.QVBoxLayout(self.searchPage)
        self.searchPageVLayout.setObjectName("searchPageVLayout")

        spacerItem = QtWidgets.QSpacerItem(
            20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.searchPageVLayout.addItem(spacerItem)

        #######################################################################
        #										SEARCH BAR SETUP [FIXED]
        #######################################################################
        self.searchBarHLayout = QtWidgets.QHBoxLayout()
        self.searchBarHLayout.setObjectName("searchBarHLayout")

        self.searchBar = QtWidgets.QLineEdit(self.searchPage)
        self.searchBar.setObjectName("searchBar")

        self.searchBarHLayout.addWidget(self.searchBar)

        self.searchButton = QtWidgets.QPushButton(self.searchPage)
        self.searchButton.setObjectName("searchButton")
        self.searchBarHLayout.addWidget(self.searchButton)

        self.showLocalLibraryButton = QtWidgets.QPushButton(self.searchPage)
        self.showLocalLibraryButton.setObjectName("showLocalLibraryButton")
        self.searchBarHLayout.addWidget(self.showLocalLibraryButton)

        # self.showBookmarksButton = QtWidgets.QPushButton(self.searchPage)
        # self.showBookmarksButton.setObjectName("showBookmarksButton")
        # self.searchBarHLayout.addWidget(self.showBookmarksButton)

        self.searchPageVLayout.addLayout(self.searchBarHLayout)
        #######################################################################
        #										SCROLL AREA SETUP [FIXED]
        #######################################################################

        self.searchPageScrollArea = QtWidgets.QScrollArea(self.searchPage)
        # self.searchPageScrollArea.setFrameShape(QtWidgets.QFrame.Box)
        # self.searchPageScrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.searchPageScrollArea.setLineWidth(2)
        self.searchPageScrollArea.setWidgetResizable(True)
        self.searchPageScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.searchPageScrollArea.setObjectName("searchPageScrollArea")

        resultsLabel = QtWidgets.QLabel()
        resultsLabel.setText(
            """<h4 style="color: #ffa02f;">Search Results</h4>""")
        resultsLabel.setAlignment(QtCore.Qt.AlignCenter)
        resultsLabel.setFrameShape(QtWidgets.QFrame.Box)
        resultsLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        resultsLabel.setLineWidth(1)
        resultsLabel.setFixedHeight(50)
        self.searchPageVLayout.addWidget(resultsLabel)

        self.searchPageVLayout.addWidget(self.searchPageScrollArea)

        self.contents = QtWidgets.QWidget()
        self.contents.setObjectName("contents")
        self.searchPageScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.searchPageScrollArea.setWidget(self.contents)

        self.vLayoutForResults = QtWidgets.QVBoxLayout(self.contents)
        self.vLayoutForResults.setObjectName("vLayoutForResults")
        self.vLayoutForResults.setContentsMargins(10, 5, 10, 500)
        self.vLayoutForResults.setSpacing(5)

        
        #######################################################################

    def infoWindow(self):
        self.infoPage.setObjectName("infoPage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.infoPage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.imageLabel = QtWidgets.QLabel(self.infoPage)
        self.imageLabel.setObjectName("imageLabel")
        self.horizontalLayout.addWidget(self.imageLabel)
        self.mangaInfoForm = QtWidgets.QFormLayout()
        self.mangaInfoForm.setLabelAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.mangaInfoForm.setFormAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.mangaInfoForm.setContentsMargins(20, 10, 10, 10)
        self.mangaInfoForm.setHorizontalSpacing(20)
        self.mangaInfoForm.setVerticalSpacing(10)
        self.mangaInfoForm.setObjectName("mangaInfoForm")
        self.title = QtWidgets.QLabel(self.infoPage)
        self.title.setObjectName("title")
        self.mangaInfoForm.setWidget(
            0, QtWidgets.QFormLayout.LabelRole, self.title)
        self.descriptionLabel = QtWidgets.QLabel(self.infoPage)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.mangaInfoForm.setWidget(
            1, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.categoriesLabel = QtWidgets.QLabel(self.infoPage)
        self.categoriesLabel.setObjectName("categoriesLabel")
        self.mangaInfoForm.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.categoriesLabel)
        self.authorsLabel = QtWidgets.QLabel(self.infoPage)
        self.authorsLabel.setObjectName("authorsLabel")
        self.mangaInfoForm.setWidget(
            3, QtWidgets.QFormLayout.LabelRole, self.authorsLabel)
        self.statusLabel = QtWidgets.QLabel(self.infoPage)
        self.statusLabel.setObjectName("statusLabel")
        self.mangaInfoForm.setWidget(
            4, QtWidgets.QFormLayout.LabelRole, self.statusLabel)
        self.chaptersLabel = QtWidgets.QLabel(self.infoPage)
        self.chaptersLabel.setObjectName("chaptersLabel")
        self.mangaInfoForm.setWidget(
            5, QtWidgets.QFormLayout.LabelRole, self.chaptersLabel)
        self.chaptersValueLabel = QtWidgets.QLabel(self.infoPage)
        self.chaptersValueLabel.setObjectName("chaptersValueLabel")
        self.mangaInfoForm.setWidget(
            5, QtWidgets.QFormLayout.FieldRole, self.chaptersValueLabel)
        self.statusValueLabel = QtWidgets.QLabel(self.infoPage)
        self.statusValueLabel.setObjectName("statusValueLabel")
        self.mangaInfoForm.setWidget(
            4, QtWidgets.QFormLayout.FieldRole, self.statusValueLabel)
        self.authorsValueLabel = QtWidgets.QLabel(self.infoPage)
        self.authorsValueLabel.setObjectName("authorsValueLabel")
        self.mangaInfoForm.setWidget(
            3, QtWidgets.QFormLayout.FieldRole, self.authorsValueLabel)
        self.categoriesValueLabel = QtWidgets.QLabel(self.infoPage)
        self.categoriesValueLabel.setObjectName("categoriesValueLabel")
        self.mangaInfoForm.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.categoriesValueLabel)
        self.descriptionValueLabel = QtWidgets.QLabel(self.infoPage)
        self.descriptionValueLabel.setObjectName("descriptionValueLabel")
        self.mangaInfoForm.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.descriptionValueLabel)
        self.titleValueLabel = QtWidgets.QLabel(self.infoPage)
        self.titleValueLabel.setObjectName("titleValueLabel")
        self.mangaInfoForm.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.titleValueLabel)
        self.downloadChapterButton = QtWidgets.QPushButton(self.infoPage)
        self.downloadChapterButton.setObjectName("downloadChapterButton")
        self.mangaInfoForm.setWidget(
            6, QtWidgets.QFormLayout.LabelRole, self.downloadChapterButton)
        self.chapterRangeSpinBox = QtWidgets.QSpinBox(self.infoPage)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.chapterRangeSpinBox.sizePolicy().hasHeightForWidth())
        self.chapterRangeSpinBox.setSizePolicy(sizePolicy)
        self.chapterRangeSpinBox.setMaximumSize(QtCore.QSize(80, 16777215))
        self.chapterRangeSpinBox.setObjectName("chapterRangeSpinBox")
        self.mangaInfoForm.setWidget(
            6, QtWidgets.QFormLayout.FieldRole, self.chapterRangeSpinBox)
        self.horizontalLayout.addLayout(self.mangaInfoForm)
        self.verticalLayout_6.addLayout(self.horizontalLayout)
        self.chapterListLabel = QtWidgets.QLabel(self.infoPage)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.chapterListLabel.setFont(font)
        self.chapterListLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.chapterListLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.chapterListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chapterListLabel.setObjectName("chapterListLabel")
        self.verticalLayout_6.addWidget(self.chapterListLabel)
        self.chapterListScrollArea = QtWidgets.QScrollArea(self.infoPage)
        self.chapterListScrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chapterListScrollArea.setWidgetResizable(True)
        self.chapterListScrollArea.setObjectName("chapterListScrollArea")
        self.chapterListScrollAreaWidgetContents = QtWidgets.QWidget()
        self.chapterListScrollAreaWidgetContents.setGeometry(
            QtCore.QRect(0, 0, 707, 177))
        self.chapterListScrollAreaWidgetContents.setObjectName(
            "chapterListScrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(
            self.chapterListScrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.chapterListGridLayout = QtWidgets.QGridLayout()
        self.chapterListGridLayout.setObjectName("chapterListGridLayout")
        self.chapter_4 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_4.setObjectName("chapter_4")
        self.chapterListGridLayout.addWidget(self.chapter_4, 1, 0, 1, 1)
        self.chapter_1 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_1.setObjectName("chapter_1")
        self.chapterListGridLayout.addWidget(self.chapter_1, 0, 0, 1, 1)
        self.chapter_7 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_7.setObjectName("chapter_7")
        self.chapterListGridLayout.addWidget(self.chapter_7, 2, 0, 1, 1)
        self.chapter_2 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_2.setObjectName("chapter_2")
        self.chapterListGridLayout.addWidget(self.chapter_2, 0, 1, 1, 1)
        self.chapter_3 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_3.setObjectName("chapter_3")
        self.chapterListGridLayout.addWidget(self.chapter_3, 0, 2, 1, 1)
        self.chapter_5 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_5.setObjectName("chapter_5")
        self.chapterListGridLayout.addWidget(self.chapter_5, 1, 1, 1, 1)
        self.chapter_6 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_6.setObjectName("chapter_6")
        self.chapterListGridLayout.addWidget(self.chapter_6, 1, 2, 1, 1)
        self.chapter_8 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_8.setObjectName("chapter_8")
        self.chapterListGridLayout.addWidget(self.chapter_8, 2, 1, 1, 1)
        self.chapter_9 = QtWidgets.QLabel(
            self.chapterListScrollAreaWidgetContents)
        self.chapter_9.setObjectName("chapter_9")
        self.chapterListGridLayout.addWidget(self.chapter_9, 2, 2, 1, 1)
        self.gridLayout_3.addLayout(self.chapterListGridLayout, 0, 0, 1, 1)
        self.chapterListScrollArea.setWidget(
            self.chapterListScrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.chapterListScrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manga Centipede"))
        self.searchBar.setPlaceholderText(_translate(
            "MainWindow", "Search for manga titles..."))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.showLocalLibraryButton.setText(
            _translate("MainWindow", "Library"))
        # self.showBookmarksButton.setText(_translate("MainWindow", "Bookmarks"))

        self.imageLabel.setText(_translate("MainWindow", "TextLabel"))
        self.title.setText(_translate("MainWindow", "Title:"))
        self.descriptionLabel.setText(_translate("MainWindow", "Description:"))
        self.categoriesLabel.setText(_translate("MainWindow", "Categories:"))
        self.authorsLabel.setText(_translate("MainWindow", "Authors:"))
        self.statusLabel.setText(_translate("MainWindow", "Status:"))
        self.chaptersLabel.setText(_translate("MainWindow", "Chapters:"))
        self.chaptersValueLabel.setText(_translate("MainWindow", "TextLabel"))
        self.statusValueLabel.setText(_translate("MainWindow", "TextLabel"))
        self.authorsValueLabel.setText(_translate("MainWindow", "TextLabel"))
        self.categoriesValueLabel.setText(
            _translate("MainWindow", "TextLabel"))
        self.descriptionValueLabel.setText(
            _translate("MainWindow", "TextLabel"))
        self.titleValueLabel.setText(_translate("MainWindow", "TextLabel"))
        self.downloadChapterButton.setText(
            _translate("MainWindow", "Download To Chapter: "))
        self.chapterListLabel.setText(_translate("MainWindow", "CHAPTER LIST"))
        self.chapter_4.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_1.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_7.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_2.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_3.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_5.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_6.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_8.setText(_translate("MainWindow", "TextLabel"))
        self.chapter_9.setText(_translate("MainWindow", "TextLabel"))
        self.navMenu.setTabText(self.navMenu.indexOf(
            self.browseMangaTab), _translate("MainWindow", "Browse Manga"))
        self.navMenu.setTabText(self.navMenu.indexOf(
            self.settingsTab), _translate("MainWindow", "Settings"))
        self.navMenu.setTabText(self.navMenu.indexOf(
            self.aboutTab), _translate("MainWindow", "About"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)

#     fname = "darkorange.txt"
#     whole_text = ""
#     with open(fname, 'r') as f:
#         # this way of reading the file gives a list of lines.
#         data_text = f.readlines()
#         # create a text out of the file
#         whole_text = (' '.join(data_text))
#     MainWindow.setStyleSheet(whole_text)
#     MainWindow.show()
#     sys.exit(app.exec_())
