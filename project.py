'''
This is project is used for leaning PyQt5
Use PyQt5 to get the origin Emacs UI
Maybe I will add the function sooner.
'''


import sys
from PyQt5.QtWidgets import QApplication, QMenu, QAction, QMainWindow


class Project(QMainWindow):

    def __init__(self):
        super().__init__()

    def initUI(self):
        # add the toolbar
        self.toolbar = self.addToolBar('Main')
        for toolb in ['New File', 'Open', 'Open Directory', 'Close', 'Save', 'Undo',\
                  'Cut', 'Copy', 'Paste', 'Search']:
            self.toolbar.addAction(QAction(toolb, self))
        # add the menu
        emenubar = self.menuBar()
        for menu in ['File', 'Edit', 'Buffers', 'Tools', 'Help']:
            emenubar.addMenu(menu)
        opmenu = emenubar.addMenu('Options')
        opcheck = QAction('Highlight Active Region', self, checkable=True)
        opcheck.setChecked(True)
        opmenu.addAction(opcheck)
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle('Emacs')
        # set the background
        self.setStyleSheet('QMainWindow{border-image:url(./1.png);}')
        self.show()


def main():
    app = QApplication(sys.argv)
    pro = Project()
    pro.initUI()
    sys.exit(app.exec_())


main()
# if __name__ == '__main__':
#     main()
