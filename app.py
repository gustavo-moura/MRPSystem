import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QTreeWidgetItem
from main import Ui_MainWindow
from obj import Item, Item_MRP, Biblioteca

class AppWindow(QMainWindow):
    biblioteca = None
    predefinido = False

    def __init__(self):
        super(AppWindow, self).__init__()

        # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()  
        self.inicializa_botoes()

        # Abre a página inicial
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Inicial)

        self.biblioteca = Biblioteca()


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
        self.ui.comboBox.addItems(self.biblioteca.getItems())
        

    # Insere itens no sistema
    def click_predefinir(self):

        # ao inves de ter que cadastrar todos os itens, já pré-inserir uma quantidade legal suficiente para
        # realizar os testes  (inserir tudo de obj.py).

        # Item(codigo, nome, tr_leadtime, lote_mínimo, emin, eatual)
        if(self.predefinir==False):
            # item 1
            itm1 = Item("BK-2", "Bicicleta Padrão", 2, 10, 0, 2)
            self.biblioteca.addItem(itm1)

            # item 2
            itm2 = Item("Ex", "Exemplo exclua esse", 2, 10, 0, 2)
            self.biblioteca.addItem(itm2)



            # teste de dependencia
            itm1.addDependencia(itm2)

        # Mensagem de informação de sucesso
        QMessageBox.about(self.ui.stackedWidget, "Pré-definido", "Estado do sistema pronto para rodar o MRP.")
        self.predefinir = True
    

    # Roda o MRP      
    def click_MRP(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_MRP)
        self.ui.combo_MRP.addItems(self.biblioteca.getItems())
        

    # Exibe relatório de itens já inseridos no sistema
    def click_itens(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_Itens)

        self.ui.tree_itens.clear()

        # Inclusão dos itens cadastrados na árvore
        if (self.biblioteca.estaVazia()):
            l = QTreeWidgetItem(["Não há itens cadastrados"])
            self.ui.tree_itens.addTopLevelItem(l)

        else:
            for i in range(self.biblioteca.lenght()):
                item = self.biblioteca.getItem_index(i)
                l = QTreeWidgetItem([item.codigo + " - " + item.nome])

                for j in range(len(item.dependencias)):
                    c = QTreeWidgetItem([item.dependencias[j].codigo + " - " + item.dependencias[j].nome])

                    l.addChild(c)

                self.ui.tree_itens.addTopLevelItem(l)




    # ###### Cadastrar
    def click_cadastrar(self):
        # realizar a verificação: se o item já foi cadastrado, perguntar se quer substituir as informações dele
        # com as informações inseridas agora
        # self, codigo, nome, nivel, tr, lote, emin, eatual

        # Só cadastra um item novo se ele ainda não estiver no banco
        if(biblioteca.naoTem(self.ui.in_cad_codigo.text())):
            itm = Item(self.ui.in_cad_codigo.text(), self.ui.in_cad_nome.text(), 
                self.ui.in_cad_tr.text(), self.ui.in_cad_lote.text(), self.ui.in_cad_emin.text(), self.ui.in_cad_eatual.text())

            self.biblioteca.addItem(itm)

        else:
            # Perguntar se quer fazer modifivações
            pass



    # ###### Executar o MRP
    def executarMRP(self):
        pass







# Abertura do sistema
app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())