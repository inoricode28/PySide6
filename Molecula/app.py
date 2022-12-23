import sys
from PyQt5 import QtWidgets,uic
#contructor
qtCreatorFile = 'UI/ventana.ui' #ruta donde esta estar la interfas UI
Ui_MainWindow,QtBaseClass = uic.loadUiType(qtCreatorFile)
class Formulario(QtWidgets.QMainWindow):
    def __init__(self,parent = None):
        super(Formulario, self).__init__(parent)        
        uic.loadUi('UI/ventana.ui',self) #ruta donde esta estar la interfas UI
        self.show() #Muestra la ventana  
    
#ejecutor
if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Formulario()
    app.exec()



