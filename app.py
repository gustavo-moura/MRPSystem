import sys
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QMessageBox, QTreeWidgetItem, QTableWidgetItem
from main import Ui_MainWindow
from obj import Item, Item_MRP, Biblioteca

def parsenumber(s):
    try:
        f = float(s)
        i = int(s)
        if f > i:
            return f
        else:
            return i
    except:
        return None

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
        self.ui.combo_MRP.currentIndexChanged.connect(self.prepararMRP)
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
        if(self.predefinido==False):
            # item 1
            i_bk2 = Item("BK-2", "Bicicleta Padrão", 2, 10, 0, 2)
            self.biblioteca.addItem(i_bk2)

            # item 2
            i_sa1 = Item("Sa-1", "Selim", 3, 20, 10, 0)
            self.biblioteca.addItem(i_sa1)

            # item 3
            i_wh1 = Item("WH-1", "Roda", 2, 40, 20, 5)
            self.biblioteca.addItem(i_wh1)

            # item 4
            i_fr2 = Item("FR-2", "Quadro", 7, 20, 30, 10)
            self.biblioteca.addItem(i_fr2)

            # item 5
            i_tr1 = Item("TR-1", "Pneu", 3, 100, 20, 30)
            self.biblioteca.addItem(i_tr1)

            # item 6
            i_rm1 = Item("RM-1", "Aro", 1, 80, 100, 20)
            self.biblioteca.addItem(i_rm1)

            # item 7
            i_hb1 = Item("HB-1", "Cubo", 1, 80, 100, 20)
            self.biblioteca.addItem(i_hb1)

            # item 8
            i_sp1 = Item("SP-1", "Raio", 3, 500, 500, 600)
            self.biblioteca.addItem(i_sp1)

            # item 9
            i_tu1 = Item("TU-1", "Tubo Metálico", 3, 60, 30, 30)
            self.biblioteca.addItem(i_tu1)

            # item 10
            i_ms1 = Item("MS-1", "Tira Metálica", 3, 100, 2, 40)
            self.biblioteca.addItem(i_ms1)

            # item 11
            i_bb1 = Item("BB-1", "Rolamentos", 3, 50, 30, 5)
            self.biblioteca.addItem(i_bb1)

            # item 12
            i_bo1 = Item("BO-1", "Eixo de Roda", 3, 100, 100, 40)
            self.biblioteca.addItem(i_bo1)

            # item 13
            i_ho1 = Item("HO-1", "Cubo Externo", 3, 100, 100, 0)
            self.biblioteca.addItem(i_ho1)

            # dependencias
            i_bk2.addDependencia(i_fr2, 1)
            i_bk2.addDependencia(i_sa1, 1)
            i_bk2.addDependencia(i_wh1, 2)

            i_fr2.addDependencia(i_tu1, 6)

            i_wh1.addDependencia(i_tr1, 1)
            i_wh1.addDependencia(i_rm1, 1)
            i_wh1.addDependencia(i_hb1, 1)
            i_wh1.addDependencia(i_sp1, 32)

            i_rm1.addDependencia(i_ms1, 1.5)

            i_hb1.addDependencia(i_bb1, 1)
            i_hb1.addDependencia(i_bo1, 1)
            i_hb1.addDependencia(i_ho1, 1)


        # Mensagem de informação de sucesso
        QMessageBox.about(self.ui.stackedWidget, "Pré-definido", "Estado do sistema pronto para rodar o MRP.")
        self.predefinido = True
    

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

                for dp in item.dependencias:
                    c = QTreeWidgetItem([dp.item.codigo + " - " + dp.item.nome])

                    l.addChild(c)

                self.ui.tree_itens.addTopLevelItem(l)




    # ###### Cadastrar
    def click_cadastrar(self):
        # realizar a verificação: se o item já foi cadastrado, perguntar se quer substituir as informações dele
        # com as informações inseridas agora
        # self, codigo, nome, nivel, tr, lote, emin, eatual

        # Só cadastra um item novo se ele ainda não estiver no banco
        if(self.biblioteca.naoTem(self.ui.in_cad_codigo.text())):
            itm = Item(self.ui.in_cad_codigo.text(), self.ui.in_cad_nome.text(), 
                self.ui.in_cad_tr.text(), self.ui.in_cad_lote.text(), self.ui.in_cad_emin.text(), self.ui.in_cad_eatual.text())

            self.biblioteca.addItem(itm)

        else:
            # Perguntar se quer fazer modifivações
            pass


    def prepararMRP(self):
        item = self.biblioteca.getItem_index(self.ui.combo_MRP.currentIndex())
        mrp = Item_MRP.find(item)
        self.ui.lb_item_MRP.setText(item.codigo + " - " + item.nome)
        self.setCell(0, 1, item.codigo)
        self.atualizarMRP(mrp)

    # ###### Executar o MRP
    def executarMRP(self):
        item = self.biblioteca.getItem_index(self.ui.combo_MRP.currentIndex())
        mrp = Item_MRP.find(item)
        for i in range(1, mrp.n):
            try:
                col = i+1
                mrp.nb[i] = self.getCell(1, col) or mrp.nb[i]
                mrp.rp[i] = self.getCell(2, col) or mrp.rp[i]
                mrp.ed[i] = self.getCell(3, col) or mrp.ed[i]
                mrp.lp[i] = self.getCell(4, col) or mrp.lp[i]
            except:
                pass
        mrp.atualizar(1)
        self.atualizarMRP(mrp)

    def atualizarMRP(self, mrp):
        for i in range(mrp.n):
            self.setCell(1, i+1, mrp.nb[i])
            self.setCell(2, i+1, mrp.rp[i])
            self.setCell(3, i+1, mrp.ed[i])
            self.setCell(4, i+1, mrp.lp[i])

    def setCell(self, i, j, n):
        self.ui.tableWidget.setItem(i, j, QTableWidgetItem(str(n)))

    def getCell(self, i, j):
        it = self.ui.tableWidget.item(i, j)
        if it:
            return parsenumber(it.text())



# Abertura do sistema
app = QApplication(sys.argv)
window = AppWindow()
window.show()
sys.exit(app.exec_())
