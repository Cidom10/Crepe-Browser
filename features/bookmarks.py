import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import functions as funcs


class Window(QMainWindow):

    def __init__(self):
        super(Window,self).__init__()

        icons = [
          'SP_ArrowBack',
          'SP_ArrowForward',
          'SP_BrowserReload',
          'SP_TitleBarUnshadeButton'
        ]

        navbar = QToolBar()
        self.addToolBar(navbar)

        menu = QMenu()

        theme = QAction("Switch theme", self)
        theme.triggered.connect(funcs.changeTheme)
        menu.addAction(theme)

        openBookmarks = QAction("Open bookmarks", self)
        openBookmarks.triggered.connect(funcs.openBookmarks)
        openBookmarks.setShortcut("Ctrl+B")
        menu.addAction(openBookmarks)

        # Button for menu
        self.optionsMenu = QToolButton(self)
        self.optionsMenu.setIcon(self.style().standardIcon(getattr(QStyle, icons[3])))
        self.optionsMenu.setMenu(menu)
        self.optionsMenu.setPopupMode(QToolButton.InstantPopup)
        self.optionsMenu.setStyleSheet("margin-left: 50px; margin-right: 30px; width: 50px")

        navbar.addWidget(self.optionsMenu)