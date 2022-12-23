from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,QLineEdit
from PySide6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide6")
        self.resize(480,320)
        texto = QLineEdit()
        texto.textChanged.connect(self.texto_modificado)

        self.setCentralWidget(texto)  

        self.texto = texto
        
    def texto_modificado(self):
        text_recuperado = self.texto.text()
        self.setWindowTitle(text_recuperado)
   
    
        

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())   
