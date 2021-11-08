import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox, QDesktopWidget


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(400, 400)
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'message', "Do you want to quit",\
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

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