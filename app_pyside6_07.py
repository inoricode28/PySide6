from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        
        self.resize(480,320)
        etiqueta=QLabel("Soy una etiqueta")
        self.setCentralWidget(etiqueta)
        



#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec()) 