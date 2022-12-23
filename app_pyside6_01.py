from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

#app = QApplication(sys.argv)
#window = QMainWindow()
#window = setWindowTitle("Hola Mundo")
#botom = QPushButton("Soy un Botón")
#window = setCentralWidget(boton)
#window.show()
#sys.exit(app.exec_())

#Constructor
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hola mundo")
        boton = QPushButton("Soy un Botón")
        self.setCentralWidget(boton)

#Ejecutor
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())   
