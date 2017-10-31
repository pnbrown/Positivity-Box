import sys
import design as gui
import functions as pb

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDesktopWidget, QLabel, QMainWindow
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon
from PyQt5.QtCore import pyqtSlot, QSize


class ExampleApp(QMainWindow, gui.Ui_Dialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

    # class App(QWidget):
    #     def __init__(self):
    #         super().__init__()
    #         self.title = 'Positivity Box'
    #         self.left = 10
    #         self.top = 10
    #         self.width = 320
    #         self.height = 200
    #         self.initUI()
    #
    #
    #         self.show()
    #
    #
    #     def initUI(self):
    #         self.setWindowTitle(self.title)
    #         self.setGeometry(self.left, self.top, self.width, self.height)
    #         self.setWindowIcon(QIcon('Untitled.png'))
    #
    #         button = QPushButton('Show me some love!', self)
    #         button.setToolTip('Click here to ')
    #         button.move(70, 70)
    #         button.clicked.connect(self.on_click)
    #
    #         oImage = QImage("Untitled.png")
    #         sImage = oImage.scaled(QSize(320, 200))  # resize Image to widgets size
    #         palette = QPalette()
    #         palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
    #         self.setPalette(palette)
    #
    #         self.label = QLabel('Test', self)  # test, if it's really backgroundimage
    #         self.label.setGeometry(50, 50, 200, 50)
    #
    #         self.show()
    #
    #     def center(self):
    #         qr = self.frameGeometry()
    #         cp = QDesktopWidget().availableGeometry().center()
    #         qr.moveCenter(cp)
    #         self.move(qr.topLeft())
    #
    # @pyqtSlot()
    # def on_click(self):
    #     print('I love you!')
