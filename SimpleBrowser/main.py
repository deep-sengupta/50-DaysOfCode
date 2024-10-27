import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

HOME_URL = 'https://www.google.com'

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(HOME_URL))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('⮌ Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('Forward ➔', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        reload_btn = QAction('⟳ Reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        stop_btn = QAction('Stop ✖', self)
        stop_btn.triggered.connect(self.browser.stop)
        navbar.addAction(stop_btn)

        home_btn = QAction('🏠 Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        zoom_in_btn = QAction('Zoom In ➕', self)
        zoom_in_btn.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() + 0.1))
        navbar.addAction(zoom_in_btn)

        zoom_out_btn = QAction('Zoom Out ➖', self)
        zoom_out_btn.triggered.connect(lambda: self.browser.setZoomFactor(self.browser.zoomFactor() - 0.1))
        navbar.addAction(zoom_out_btn)

        bookmark_btn = QAction('⭐ Bookmark', self)
        bookmark_btn.triggered.connect(self.add_bookmark)
        navbar.addAction(bookmark_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        self.bookmarks = self.load_bookmarks()
        bookmarks_menu = QMenu('Bookmarks', self)
        self.menuBar().addMenu(bookmarks_menu)
        self.populate_bookmarks_menu(bookmarks_menu)

        self.browser.urlChanged.connect(self.update_url)
        self.browser.titleChanged.connect(self.update_title)
        self.browser.loadStarted.connect(lambda: self.status.showMessage("Loading..."))
        self.browser.loadFinished.connect(lambda: self.status.showMessage("Ready"))

    def navigate_home(self):
        self.browser.setUrl(QUrl(HOME_URL))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if not url.startswith(('http://', 'https://')):
            url = 'http://' + url
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())

    def update_title(self, title):
        self.setWindowTitle(title)

    def add_bookmark(self):
        url = self.browser.url().toString()
        self.bookmarks.append(url)
        self.save_bookmarks()
        self.status.showMessage("Bookmark added!", 2000)

    def load_bookmarks(self):
        if os.path.exists('bookmarks.txt'):
            with open('bookmarks.txt', 'r') as f:
                return [line.strip() for line in f]
        return []

    def save_bookmarks(self):
        with open('bookmarks.txt', 'w') as f:
            f.write('\n'.join(self.bookmarks))

    def populate_bookmarks_menu(self, menu):
        menu.clear()
        for url in self.bookmarks:
            action = QAction(url, self)
            action.triggered.connect(lambda checked, url=url: self.browser.setUrl(QUrl(url)))
            menu.addAction(action)

app = QApplication(sys.argv)
QApplication.setApplicationName('Advanced Browser')
window = MainWindow()
app.exec_()