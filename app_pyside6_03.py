from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        boton = QPushButton("CLICK")
        boton.clicked.connect(self.boton_clicado)
        self.setCentralWidget(boton)   
    
    def boton_clicado(self):
        print("Boton clicado")

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   
