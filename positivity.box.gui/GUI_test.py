import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, Qt


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Positivity Box'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()


        self.show()


    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Show me some love!', self)
        button.setToolTip('Click here to ')
        button.move(70, 70)
        button.clicked.connect(self.on_click)

        self.show()

#Here we can control what happens when you click the button, ie change it to pull from the dictionary

    @pyqtSlot()
    def on_click(self):
        print('I love you!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())