import sys
from PyQt5.QtWidgets import QApplication, QDialog
from design import Ui_Dialog


class ImageDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super(ImageDialog, self).__init__()

        # # Start Program
        # quotes = pb.program_run()
        # quotes_entry = 0
        # pb.print_quote(quotes, quotes_entry)

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Connect up the buttons.

        # self.Exit.clicked.connect(self.reject)


app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Dialog()
ui.setupUi(window)

window.show()
sys.exit(app.exec_())
