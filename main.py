#!/usr/bin/python
import sys

from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox
from PyQt5.QtGui import QFont
now = QDate.currentDate()


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # set font for this window.
        QToolTip.setFont(QFont('DejaVu Sans Mono', 8))
        self.setToolTip('This is a <b>Qwidget</b> widget')
        # generate a button
        btn = QPushButton('button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.setGeometry(0, 0, 100, 20)
        # generate a button use for quit the window.
        qtn = QPushButton('quit', self)
        qtn.setToolTip('This is a <b>QPushButton</b> widget, for quit the window')
        qtn.clicked.connect(QApplication.instance().quit)
        qtn.resize(qtn.sizeHint())
        qtn.setGeometry(100, 0, 100, 20)
        # generate a message box.
        self.setGeometry(300, 300, 550, 660)
        self.setWindowTitle('Test')
        self.setWindowOpacity(0.8)
        print(f'窗口透明度为{self.windowOpacity()}, 窗口标题为{self.windowTitle()}')
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'message', "Do you want to quit"\
                , QMessageBox.Yes|QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()