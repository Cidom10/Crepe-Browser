import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
#importing QtCore to use Qurl
from PyQt5.QtCore import *
from Browser.webEngine import WebEngine

class Window (QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        icons = [
          'SP_ArrowBack',
          'SP_ArrowForward',
          'SP_BrowserReload',
          'SP_TitleBarUnshadeButton'
        ]

        # Layout will include Toolbar and Browser widget

        self.browser = QWebEngineView()
        self.loadHomepage()

        # Used to apply the layout to the whole main window
        self.setCentralWidget(self.browser)


        self.showMaximized()
    
    def loadHomepage(self):
        parent = os.path.abspath(os.path.join(".", os.pardir))
        filename = os.path.join(parent, "Crepe-Browser\homepage\index.html")
        with open(filename, "r") as f:
            print(filename)
            html = f.read()
            self.browser.setHtml(html)
            print("what???")

MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Crêpe Browser')
window = Window()
MyApp.exec()