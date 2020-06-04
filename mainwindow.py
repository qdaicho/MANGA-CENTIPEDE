#!/usr/bin/python3

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import os



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

        self.searchButton = QtWidgets.QPushButton(self.searchPage, enabled = False)
        self.searchButton.setObjectName("searchButton")
        self.searchBarHLayout.addWidget(self.searchButton)

        self.showLocalLibraryButton = QtWidgets.QPushButton(self.searchPage)
        self.showLocalLibraryButton.setObjectName("showLocalLibraryButton")
        self.searchBarHLayout.addWidget(self.showLocalLibraryButton)

        # self.showBookmarksButton = QtWidgets.QPushButton(self.searchPage)
        # self.showBookmarksButton.setObjectName("showBookmarksButton")
        # self.searchBarHLayout.addWidget(self.showBookmarksButton)

        self.searchPageVLayout.addLayout(self.searchBarHLayout)

        self.downloadProgress = QtWidgets.QProgressBar(self.searchPage)
        self.downloadProgress.setObjectName("downloadProgress")
        self.searchPageVLayout.addWidget(self.downloadProgress)
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
        self.vLayoutForInfoPage = QtWidgets.QVBoxLayout(self.infoPage)
        self.vLayoutForInfoPage.setObjectName("vLayoutForInfoPage")

        spacerItem1 = QtWidgets.QSpacerItem(
            20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.vLayoutForInfoPage.addItem(spacerItem1)

        self.infoBarHLayout = QtWidgets.QHBoxLayout()
        self.infoBarHLayout.setObjectName("infoBarHLayout")

        self.backButton = QtWidgets.QPushButton(self.infoPage)
        self.backButton.setObjectName("backButton")
        self.backButton.setText("Back")
        self.infoBarHLayout.addWidget(self.backButton)

        hspacer = QtWidgets.QSpacerItem(1000, 20, QtWidgets.QSizePolicy.Expanding)
        self.infoBarHLayout.addItem(hspacer)

        self.downloadChaptersButton = QtWidgets.QPushButton(self.infoPage)
        self.downloadChaptersButton.setObjectName("downloadChaptersButton")
        self.downloadChaptersButton.setText("Download Chapters")
        self.infoBarHLayout.addWidget(self.downloadChaptersButton)

        self.chapterNumberSpinBox = QtWidgets.QSpinBox(self.infoPage)
        self.chapterNumberSpinBox.setObjectName("chapterNumberSpinBox")
        self.infoBarHLayout.addWidget(self.chapterNumberSpinBox)



        self.vLayoutForInfoPage.addLayout(self.infoBarHLayout)

        self.downloadProgressForChapters = QtWidgets.QProgressBar(self.infoPage)
        self.downloadProgressForChapters.setObjectName("downloadProgressForChapters")
        self.vLayoutForInfoPage.addWidget(self.downloadProgressForChapters)


        #######################################################################
        #                                       INFO AREA SETUP [FIXED]
        #######################################################################



        self.infoLabel = QLabel2()
        self.infoLabel.setText("dummy text")
        self.infoLabel.setFixedHeight(300)
        # self.infoLabel.addStretch()
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setTextFormat(QtCore.Qt.RichText)
        self.infoLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.infoLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.infoLabel.setLineWidth(1)
        # self.infoLabel.setStyleSheet("QLabel::hover{background-color : #4a4848;}")
        self.vLayoutForInfoPage.addWidget(self.infoLabel)

        self.chapterListLabel = QtWidgets.QLabel(self.infoPage)
        self.chapterListLabel.setText(
            """<h4 style="color: #ffa02f;">Downloaded Chapters List</h4>""")
        self.chapterListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chapterListLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.chapterListLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.chapterListLabel.setLineWidth(1)
        self.chapterListLabel.setFixedHeight(50)
        self.vLayoutForInfoPage.addWidget(self.chapterListLabel)

        self.chapterListScrollArea = QtWidgets.QScrollArea(self.searchPage)
        # self.chapterListScrollArea.setFrameShape(QtWidgets.QFrame.Box)
        # self.chapterListScrollArea.setFrameShadow(QtWidgets.QFrame.Raised)
        # self.chapterListScrollArea.setLineWidth(2)
        self.chapterListScrollArea.setWidgetResizable(True)
        self.chapterListScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.chapterListScrollArea.setObjectName("chapterListScrollArea")

        self.chapterListScrollAreaWidgetContents = QtWidgets.QWidget()
        self.chapterListScrollAreaWidgetContents.setObjectName("chapterListScrollAreaWidgetContents")
        self.chapterListScrollArea.setAlignment(QtCore.Qt.AlignCenter)
        self.chapterListScrollArea.setWidget(self.chapterListScrollAreaWidgetContents)


        self.chapterListGridLayout = QtWidgets.QGridLayout(self.chapterListScrollAreaWidgetContents)
        self.chapterListGridLayout.setObjectName("chapterListGridLayout")
        self.chapterListGridLayout.setContentsMargins(10, 5, 10, 500)
        self.chapterListGridLayout.setSpacing(5)


        self.vLayoutForInfoPage.addWidget(self.chapterListScrollArea)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Manga Centipede"))
        self.searchBar.setPlaceholderText(_translate(
            "MainWindow", "Search for manga titles..."))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.showLocalLibraryButton.setText(
            _translate("MainWindow", "Library"))
        # self.showBookmarksButton.setText(_translate("MainWindow", "Bookmarks"))

        self.navMenu.setTabText(self.navMenu.indexOf(
            self.browseMangaTab), _translate("MainWindow", "Browse Manga"))
        self.navMenu.setTabText(self.navMenu.indexOf(
            self.settingsTab), _translate("MainWindow", "Settings"))
        self.navMenu.setTabText(self.navMenu.indexOf(
            self.aboutTab), _translate("MainWindow", "About"))