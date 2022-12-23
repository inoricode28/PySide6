from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        boton = QPushButton("Soy un Botón")
        self.setCentralWidget(boton)

        #self.setMinimumSize(QSize(480,320))
        #self.setMaximumSize(QSize(480,320))
        #self.setFixedSize(QSize(480,320))
        #self.resize(480,320)
        

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   
