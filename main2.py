# Code to generate Hello_Friend program
# Created November 14, 2018 by: Katie Davis
# 
# This program creates a window with a Hello World label that will change
# based on the text in a textfield at the time of the button press.
import sys
from MainUi import Ui_MainWindow
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        nameField = self.nameField
        nameField.setToolTip('Enter your name')
        submit = self.submitButton
        submit.clicked.connect(self.hello)
        self.show()

    def hello(self):
        """
        param: self

        description: Defines the functionality of the submitButton. 
            The text placed in the nameField will change the text in the helloLabel.
        """
        if self.nameField.text() != '':
            self.helloLabel.setText('Hello ' + self.nameField.text())
        else:
            self.helloLabel.setText('Please enter a name')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
