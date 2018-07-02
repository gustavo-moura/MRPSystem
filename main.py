# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(829, 579)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 821, 581))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(410, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 829, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuProdutos = QtWidgets.QMenu(self.menubar)
        self.menuProdutos.setObjectName("menuProdutos")
        self.menuMRP = QtWidgets.QMenu(self.menubar)
        self.menuMRP.setObjectName("menuMRP")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionCarregar_pre_defini_es = QtWidgets.QAction(MainWindow)
        self.actionCarregar_pre_defini_es.setObjectName("actionCarregar_pre_defini_es")
        self.actionInserir_Informa_es = QtWidgets.QAction(MainWindow)
        self.actionInserir_Informa_es.setObjectName("actionInserir_Informa_es")
        self.actionCarregar_Pre_Defini_es = QtWidgets.QAction(MainWindow)
        self.actionCarregar_Pre_Defini_es.setObjectName("actionCarregar_Pre_Defini_es")
        self.actionCr_ditos = QtWidgets.QAction(MainWindow)
        self.actionCr_ditos.setObjectName("actionCr_ditos")
        self.actionRodar_Execu_o = QtWidgets.QAction(MainWindow)
        self.actionRodar_Execu_o.setObjectName("actionRodar_Execu_o")
        self.menuArquivo.addSeparator()
        self.menuArquivo.addAction(self.actionCr_ditos)
        self.menuProdutos.addAction(self.actionInserir_Informa_es)
        self.menuProdutos.addSeparator()
        self.menuProdutos.addAction(self.actionCarregar_Pre_Defini_es)
        self.menuMRP.addAction(self.actionRodar_Execu_o)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuProdutos.menuAction())
        self.menubar.addAction(self.menuMRP.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MRP Systema"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuProdutos.setTitle(_translate("MainWindow", "Produtos"))
        self.menuMRP.setTitle(_translate("MainWindow", "MRP"))
        self.actionCarregar_pre_defini_es.setText(_translate("MainWindow", "Carregar pre-definições"))
        self.actionInserir_Informa_es.setText(_translate("MainWindow", "Inserir Informações"))
        self.actionCarregar_Pre_Defini_es.setText(_translate("MainWindow", "Carregar Pré-Definições"))
        self.actionCr_ditos.setText(_translate("MainWindow", "Créditos"))
        self.actionRodar_Execu_o.setText(_translate("MainWindow", "Rodar Execução"))

