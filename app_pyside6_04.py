from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        self.resize(480,320)
        boton = QPushButton("CLICK")
        #boton.clicked.connect(self.boton_clicado)
        #boton.pressed.connect(self.boton_pulsado)
        #boton.released.connect(self.boton_liberado)
        boton.setCheckable(True)
        boton.clicked.connect(self.boton_alternado)
        self.setCentralWidget(boton)   
    
    def boton_clicado(self):
        print("Boton clicado")
    def boton_pulsado(self):
        print("Boton pulsado")
    def boton_liberado(self):
        print("Boton liberado")
    def boton_alternado(self, valor):
        print("Boton Alternado", valor)

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   
