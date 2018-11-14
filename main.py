# Code to generate Hello_Friend program
# Created November 14, 2018 by: Katie Davis
# 
# This program creates a window with a Hello World label that will change
# based on the text in a textfield at the time of the button press.

import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

def setupUI(uifilename, parent=None):
    '''
        param: uifilename - the name/location of the ui file

        This function will read the ui file and store it in a 
        variable for further usage. 

        returns: ui - access to elements of the ui file
    '''
    loader = QUiLoader()
    uifile = QFile(uifilename)
    uifile.open(QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui

def hello():
    """
        param: self

        description: Defines the functionality of the submitButton. 
            The text placed in the nameField will change the text in the helloLabel.
    """
    if nameField.text() != '':
        helloLabel.setText('Hello ' + nameField.text())
    else:
        helloLabel.setText('Please enter a name')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = setupUI('Hello.ui')
    #calling elements of ui for function assignment
    global nameField
    global helloLabel
    nameField = window.nameField
    nameField.setToolTip('Enter your name')
    helloLabel = window.helloLabel
    submit = window.submitButton
    submit.clicked.connect(hello)
    #open window
    window.show()
    
    sys.exit(app.exec_())
