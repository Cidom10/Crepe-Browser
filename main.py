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
        navbar.setStyleSheet("height: 45px; padding-left: 5px; color:#cacaca; background-color: #404040;")

        #*-----------------prev Button-----------------
        self.prevPixmap = QPixmap(r"C:/Users/logan/OneDrive\Documents/Computer Sci/Pi Browser/Crepe-Browser/IconPics/PreviousIconFinal.png")
        self.prevIcon = QIcon(self.prevPixmap)
        prevBtn = QAction("", self)
        prevBtn.setIcon(self.prevIcon)
        #when triggered set connection
        prevBtn.triggered.connect(self.browser.back)
        navbar.addAction(prevBtn)

        #*-----------------next Button---------------
        self.nextPixmap = QPixmap(r"C:/Users/logan/OneDrive\Documents/Computer Sci/Pi Browser/Crepe-Browser/IconPics/NextIconFinal.png")
        self.nextIcon = QIcon(self.nextPixmap)
        nextBtn = QAction("", self)
        nextBtn.setIcon(self.nextIcon)
        #when triggered set connection
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)

        #*-----------refresh Button--------------------
        self.refreshPix = QPixmap("C:/Users/logan/OneDrive/Documents/Computer Sci/Pi Browser/Crepe-Browser/IconPics/RefreshIconFinal.png")
        self.refreshicon = QIcon(self.refreshPix)
        refreshBtn = QAction("", self)
        refreshBtn.setIcon(self.refreshicon)
        
        #when triggered set connection
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)

        #*-----------home button----------------------  
        self.homePix = QPixmap("C:/Users/logan/OneDrive/Documents/Computer Sci/Pi Browser/Crepe-Browser/IconPics/HomeIconFinal.png")
        self.homeicon = QIcon(self.homePix)
        homeBtn = QAction('',self)
        homeBtn.setIcon(self.homeicon)
        #when triggered call home method
        homeBtn.triggered.connect(self.loadHomepage)
        navbar.addAction(homeBtn)

        #*------------search bar------------------------
        self.searchBar = QLineEdit(self)
        self.searchBar.returnPressed.connect(self.searchOnline)
        self.searchBar.setFixedWidth(1300)
        self.searchBar.setStyleSheet("margin-left: 200px; font-size: 20px; margin-right: auto; height: 30%;")
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
        self.settingsPixmap = QPixmap(r"C:/Users/logan/OneDrive\Documents/Computer Sci/Pi Browser/Crepe-Browser/IconPics/settingiconfinal.png")
        self.settingsIcon = QIcon(self.settingsPixmap)
        # Button for menu
        self.optionsMenu = QToolButton(self)
        self.optionsMenu.setIcon(self.settingsIcon)
        self.optionsMenu.setMenu(menu)
        self.optionsMenu.setPopupMode(QToolButton.InstantPopup)
        self.optionsMenu.setStyleSheet("margin-left: 250px; margin-right: 10px; width: 50px")

        navbar.addWidget(self.optionsMenu)
    
    def loadHomepage(self):
        # Gets html file from "homepage" folder and serves it to the QWebEngineView
        url = QUrl('http://localhost:5000/')
        self.browser.setUrl(url)
        self.browser.setZoomFactor(1.75)
    
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
            self.browser.setZoomFactor(4)



MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Cr??pe Browser')
window = Window()
MyApp.exec()