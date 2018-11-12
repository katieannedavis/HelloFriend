import sys
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile

def setupUI(uifilename, parent=None):
    loader = QUiLoader()
    uifile = QFile(uifilename)
    uifile.open(QFile.ReadOnly)
    ui = loader.load(uifile, parent)
    uifile.close()
    return ui

def hello():
    if nameField.text() != '':
        helloLabel.setText('Hello ' + nameField.text())
    else:
        helloLabel.setText('Please enter a name')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = setupUI('Hello.ui')
    global nameField
    global helloLabel
    nameField = window.nameField
    nameField.setToolTip('Enter your name')
    helloLabel = window.helloLabel
    submit = window.submitButton
    submit.clicked.connect(hello)
    window.show()
    
    sys.exit(app.exec_())
