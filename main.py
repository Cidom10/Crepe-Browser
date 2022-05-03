import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
#importing QtCore to use Qurl
from PyQt5.QtCore import *
from URLFunctions.parseURL import parseURL

class Window (QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        icons = [
          'SP_ArrowBack',
          'SP_ArrowForward',
          'SP_BrowserReload',
          'SP_TitleBarUnshadeButton'
        ]

        # Layout of QMainWindow will include Toolbar and central widget

        self.browser = QWebEngineView()
        # Opens up to homepage off of start
        self.loadHomepage()

        self.setCentralWidget(self.browser)

        navbar = QToolBar()
        self.addToolBar(navbar)

        #*-----------------prev Button-----------------
        prevBtn = QAction("", self)
        prevBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[0])))
        #when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        #*-----------------next Button---------------
        nextBtn = QAction("", self)
        nextBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[1])))
        #when triggered set connection
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #*-----------refresh Button--------------------
        refreshBtn = QAction("", self)
        refreshBtn.setIcon(self.style().standardIcon(getattr(QStyle, icons[2])))
        
        #when triggered set connection
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #*-----------home button----------------------  
        homeBtn = QAction('Home',self)
        #when triggered call home method
        homeBtn.triggered.connect(self.loadHomepage)
        navbar.addAction(homeBtn)

        #*------------search bar------------------------
        self.searchBar = QLineEdit(self)
        self.searchBar.returnPressed.connect(self.searchOnline)
        self.searchBar.setFixedWidth(1300)
        self.searchBar.setStyleSheet("margin-left: 250px; margin-right: auto")
        navbar.addWidget(self.searchBar)

        self.showMaximized()

        menu = QMenu()

        # theme = QAction("Switch theme", self)
        # theme.triggered.connect(funcs.changeTheme)
        # menu.addAction(theme)

        # openBookmarks = QAction("Open bookmarks", self)
        # openBookmarks.triggered.connect(funcs.openBookmarks)
        # openBookmarks.setShortcut("Ctrl+B")
        # menu.addAction(openBookmarks)

        # Button for menu
        self.optionsMenu = QToolButton(self)
        self.optionsMenu.setIcon(self.style().standardIcon(getattr(QStyle, icons[3])))
        self.optionsMenu.setMenu(menu)
        self.optionsMenu.setPopupMode(QToolButton.InstantPopup)
        self.optionsMenu.setStyleSheet("margin-left: 350px; margin-right: 10px; width: 50px")

        navbar.addWidget(self.optionsMenu)
    
    def loadHomepage(self):
        # Gets html file from "homepage" folder and serves it to the QWebEngineView
        url = QUrl('http://localhost:5000/')
        self.browser.setUrl(url)
    
    # UserInput will be given if sent through homepage search bar
    def searchOnline(self):
        userInput = self.searchBar.text()
        if userInput == "" or userInput == " ":
            self.loadHomepage()
            self.searchBar.setText("")
        else:
            url = QUrl(parseURL(self.searchBar.text()))
            self.browser.setUrl(url)
            self.searchBar.setText(url.toString())
            print(self.browser.history)

MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Crêpe Browser')
window = Window()
MyApp.exec()