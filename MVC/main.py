########################################################################
# IMPORT CUSTOM BUTTONS FILE
# Because ill be frequently updating this package,
# run "pip install --upgrade QT-PyQt-PySide-Custom-Widgets"
# to install any updates
from Custom_Widgets.Widgets import *
import iconify as ico
from iconify.qt import QtGui, QtWidgets, QtCore
from PySide2.QtCore import *
########################################################################

import sys
from controlador.botones import Loginn

if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_ses = Loginn()#Loginn es Cambiable    
    ventana_ses.show()
    sys.exit(app.exec_())