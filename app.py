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
        # Menu
        self.ui.actionCr_ditos.triggered.connect(self.click_creditos)
        self.ui.actionInserir_Informa_es.triggered.connect(self.click_inserir)
        self.ui.actionCarregar_Pre_Defini_es.triggered.connect(self.click_predefinir)
        self.ui.actionRodar_Execu_o.triggered.connect(self.click_MRP)

        # Cadastrar
        self.ui.btn_cadastrar.clicked.connect(self.click_cadastrar)



    # Declaração de Ações dos Botões

    # Menu
    def click_creditos(self):
        # Exibe créditos
        QMessageBox.about(self.ui.stackedWidget, "Créditos", "Sistema desenvolvido por: Yago Pessoa, Gustavo Moura, Thais Nobre e Alef Segura no âmbito da disciplina de Modelagem da Produção - ICMC - USP - julho de 2018")
    
    def click_inserir(self):
        # abrir a janela de cadastro de item
        pass
    
    def click_predefinir(self):
        # ao inves de ter que cadastrar todos os itens, já pré-inserir uma quantidade legal suficiente para
        # realizar os testes  (inserir tudo de object.py).

        # Mensagem de informação de sucesso
        QMessageBox.about(self.ui.stackedWidget, "Pré-definido", "Estado do sistema pronto para rodar o MRP.")
    
    
    def click_MRP(self):
        # roda o MRP
        pass

    # Cadastrar
    def click_cadastrar(self):
        # realizar a verificação: se o item já foi cadastrado, perguntar se quer substituir as informações dele
        # com as informações inseridas agora
        pass




app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())