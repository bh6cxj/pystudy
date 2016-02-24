from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.MyTable = QTableWidget(100,5)

        layout = QHBoxLayout()
        layout.addWidget(self.MyTable)
        self.setLayout(layout)

if __name__ == '__main__':
    import sys    app = QApplication(sys.argv)
    myWindow = MyDialog()
    myWindow.show()
    sys.exit(app.exec_())
