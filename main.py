import sys

from PyQt5.QtWidgets import QApplication, QDialog
from design import Ui_Dialog
# from test_environment.design import Ui_Dialog

class ImageDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
        self.colorDepthCombo.addItem("2 colors (1 bit per pixel)")

        # Connect up the buttons.
        self.okButton.clicked.connect(self.accept)
        self.cancelButton.clicked.connect(self.reject)


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())



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
