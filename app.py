import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox
from main import Ui_MainWindow
from object import Item, Item_MRP

class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  
        self.inicializa_botoes()


    def inicializa_botoes(self):
        self.ui.actionCr_ditos.triggered.connect(self.click_creditos)
        self.ui.actionInserir_Informa_es.triggered.connect(self.click_inserir)
        self.ui.actionCarregar_Pre_Defini_es.triggered.connect(self.click_predefinir)
        self.ui.actionRodar_Execu_o.triggered.connect(self.click_MRP)



    # Declaração de Funções

    def click_creditos(self):
        QMessageBox.about(self.ui.stackedWidget, "Créditos", "Sistema desenvolvido por: Yago Pessoa, Gustavo Moura, Thais Nobre e Alef Segura no âmbito da disciplina de Modelagem da Produção - ICMC - USP - julho de 2018")
    
    def click_inserir(self):
        pass
    
    def click_predefinir(self):
        pass
    
    def click_MRP(self):
        pass



app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())