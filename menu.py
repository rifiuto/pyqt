import sys

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QMenu


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # set name
        self.setObjectName('ma')
        # first menu
        exitAct = QAction("&exit", self)
        exitAct.setShortcut('Ctrl+X')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)
        self.statusBar().showMessage('Are you ok')
        self.setToolTip('Hello, PyQt5')
        #
        menubar = self.menuBar()
        filemenu = menubar.addMenu('file')

        # then, this is check menu
        checkact = QAction('check', self, checkable=True)
        # button use the setToolTip, and menu use the setStatusTip
        checkact.setStatusTip('This is a statusbar')
        # set the default of the check value
        checkact.setChecked(False)
        checkact.triggered.connect(self.toggleMenu)
        filemenu.addAction(checkact)
        filemenu.addAction(exitAct)
        file2m = menubar.addMenu('import')
        # 创建子 menu 需要QMenu
        submenu1 = QMenu('java import', self)
        submenu2 = QMenu('language', self)
        subaction = QAction('static import', self)
        for i in ['java', 'python', 'c', 'c++', 'perl', 'LaTeX', 'js', 'css']:
            submenu2.addAction(QAction(i, self))
        file2m.addMenu(submenu1)
        file2m.addMenu(submenu2)
        file2m.addAction(subaction)
        # add the toolbar
        self.toolbar = self.addToolBar('Test')
        self.toolbar.addAction(checkact)
        self.setGeometry(300, 300, 800, 800)
        # use the object name to get the background image
        self.setStyleSheet("#ma{border-image:url(./1.png);}")
        self.setWindowTitle('StatustBar')
        self.show()

    def toggleMenu(self, state):
        if state:
            self.statusBar().show()
        else:
            self.statusBar().hide()
def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()