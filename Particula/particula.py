from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

import sys

class Chris(QtWidgets.QMainWindow):
    
    def __init__(self, *args , parent=None):
        
        super(Chris, self).__init__(parent)
        self.venPri = Ui_MainWindow()
        self.venPri.setupUi(self)