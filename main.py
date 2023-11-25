import sys
from PyQt6 import QtWidgets

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.uic import loadUi
from livegetitall import livegetit


class MainWindow(QMainWindow):
    # MainWindow Login Screen index 0
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("liveplay.ui", self)
        self.pushButton.clicked.connect(self.liveplay)
        self.pushButton_2.clicked.connect(self.clearAll)


    def liveplay(self):
        self.label_2.setText(livegetit())



    def clearAll(self):
        self.label_2.setText("LIVEPLAY")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()

    # outer widgets
    liveplay_obj = MainWindow()

    # add widgets to the pos

    # outer widgets

    # internal widgets
    widget.addWidget(liveplay_obj)

    # start the application
    # widget.setFixedHeight(1982)
    # widget.setFixedWidth(1080)
    widget.show()
    sys.exit(app.exec())
