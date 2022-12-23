# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfasstjbzK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2 import QtWidgets
from PySide2.QtWidgets import *


#Constructor
class Chris(QtWidgets.QMainWindow):
    
    def __init__(self, *args , parent=None):
        
        super(Chris, self).__init__(parent)
        self.venPri = Ui_MainWindow()
        self.venPri.setupUi(self)

#Particula
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(469, 329)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnCerrar = QPushButton(self.centralwidget)
        self.btnCerrar.setObjectName(u"btnCerrar")
        self.btnCerrar.setGeometry(QRect(100, 90, 271, 161))
        font = QFont()
        font.setPointSize(36)
        self.btnCerrar.setFont(font)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnCerrar.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

#Ejecutor
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    ventana_ses = Chris()    
    ventana_ses.show()
    sys.exit(app.exec_())