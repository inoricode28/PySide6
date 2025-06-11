from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QFont, QPixmap
from PySide6.QtCore import Qt
from pathlib import Path
import sys

def absPath(file):
    return str(Path(__file__).parent.absolute() / file)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.setWindowTitle("Pyside6")       
        self.resize(1280,720)

        etiqueta=QLabel("Soy una etiqueta")       
        fuente=QFont("Comic Sans MS", 24)
        etiqueta.setFont(fuente)
        etiqueta.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Centra en Vertical y Horizontal
        imagen= QPixmap(absPath("img.jpg"))
        etiqueta.setPixmap(imagen)
        etiqueta.setScaledContents(True)
        self.setCentralWidget(etiqueta)




#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 