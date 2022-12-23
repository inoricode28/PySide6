from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        self.resize(480,320)
        boton = QPushButton("CLICK")        
        boton.setCheckable(True)

        boton.clicked.connect(self.boton_alternado)
        self.setCentralWidget(boton)  
        self.boton = boton
            
   
    def boton_alternado(self, valor):
        if valor:
            self.boton.setText("Estoy Activado")
        else:
            self.boton.setText("Estoy Desactivado")
        

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   
