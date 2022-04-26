import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
#importing QtCore to use Qurl
from PyQt5.QtCore import *

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

        self.showMaximized()
    
    def loadHomepage(self):
        # Gets html file from "homepage" folder and serves it to the QWebEngineView
        parent = os.path.abspath(os.path.join(".", os.pardir))
        filename = os.path.join(parent, "Crepe-Browser\homepage\index.html")
        with open(filename, "r") as f:
            print(filename)
            html = f.read()
            self.browser.setHtml(html)

MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Crêpe Browser')
window = Window()
MyApp.exec()