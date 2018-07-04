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

        # Abre a página inicial
    	self.ui.stackedWidget.setCurrentWidget(self.ui.page_Inicial)


    def inicializa_botoes(self):
        # Menu
        self.ui.actionCr_ditos.triggered.connect(self.click_creditos)
        self.ui.actionInserir_Informa_es.triggered.connect(self.click_inserir)
        self.ui.actionCarregar_Pre_Defini_es.triggered.connect(self.click_predefinir)
        self.ui.actionRodar_Execu_o.triggered.connect(self.click_MRP)
        self.ui.actionItens_cadastrados.triggered.connect(self.click_itens)
        
        # Cadastrar
        self.ui.btn_cadastrar.clicked.connect(self.click_cadastrar)

        # Item
        self.ui.btn_novoitem.clicked.connect(self.click_inserir)

        # MRP
        self.ui.btn_executar.clicked.connect(self.executarMRP)



    # ############ Declaração de Ações dos Botões

    # ###### Menu

    # Exibe créditos
    def click_creditos(self):
        QMessageBox.about(self.ui.stackedWidget, "Créditos", "Sistema desenvolvido por: Yago Pessoa, Gustavo Moura, Thais Nobre e Alef Segura no âmbito da disciplina de Modelagem da Produção - ICMC - USP - julho de 2018")
    

    # Abre a janela de cadastro de item
    def click_inserir(self):    
    	self.ui.stackedWidget.setCurrentWidget(self.ui.page_Cadastro)
        

    # Insere itens no sistema
    def click_predefinir(self):
        # ao inves de ter que cadastrar todos os itens, já pré-inserir uma quantidade legal suficiente para
        # realizar os testes  (inserir tudo de object.py).

        # Mensagem de informação de sucesso
        QMessageBox.about(self.ui.stackedWidget, "Pré-definido", "Estado do sistema pronto para rodar o MRP.")
    

    # Roda o MRP      
    def click_MRP(self):
    	self.ui.stackedWidget.setCurrentWidget(self.ui.page_MRP)
        

    # Exibe relatório de itens já inseridos no sistema
    def click_itens(self):
    	
    	self.ui.stackedWidget.setCurrentWidget(self.ui.page_Itens)
    	



    # ###### Cadastrar
    def click_cadastrar(self):
        # realizar a verificação: se o item já foi cadastrado, perguntar se quer substituir as informações dele
        # com as informações inseridas agora
        # self, codigo, nome, nivel, tr, lote, emin, eatual
        Item(self.ui.in_cad_codigo.text(), self.ui.in_cad_nome.text(), 
        	self.ui.in_cad_tr.text(), self.ui.in_cad_lote.text(), self.ui.in_cad_emin.text(), self.ui.in_cad_eatual.text())




    # ###### Executar o MRP
    def executarMRP(self):
    	pass







# Abertura do sistema
app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())