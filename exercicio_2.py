""""
CRIE UM PROGRAMA QUE RECEBA DADOS DE UM CLIENTE.
NESSE PROGRAMA DEVE TER UM LINE EDIT PARA INFORMAR O NOME.
COMBO BOX PARA INFORMAR SEXO.
LINE EDIT PARA CONSULTA DE CEP
LINEEDIT BAIRRO, CIDADE, LOUGRADOURO DEVE SER PREENHCIDO AUTOMATICAMENTE.
"""
import pycep_correios

from PySide6.QtWidgets import (QApplication, QMainWindow, QLineEdit, QVBoxLayout, 
QFrame, QFrame, QComboBox, QPushButton, QLabel)
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Consulta de dados')

        self.lb_nome = QLabel('Nome')
        self.inpt_nome = QLineEdit()
        self.lb_genero = QLabel('Genero')
        self.cb_genero = QComboBox()
        self.lb_cep = QLabel('CEP')
        self.inpt_cep = QLineEdit()
        self.lb_bairro = QLabel('Bairro')
        self.inpt_bairo = QLineEdit()
        self.lb_cidade = QLabel('Cidade')
        self.inpt_cidade = QLineEdit()
        self.lb_logradouro = QLabel('Logradouro')
        self.inpt_logradouro = QLineEdit()

        self.cb_genero.addItems(['','Masculino', 'Feminino'])

        #define o layout para agrupamento dos itens
        layout = QVBoxLayout()
        layout.addWidget(self.lb_nome)
        layout.addWidget(self.inpt_nome)

        layout.addWidget(self.lb_genero)        
        layout.addWidget(self.cb_genero)

        layout.addWidget(self.lb_cep)
        layout.addWidget(self.inpt_cep)

        layout.addWidget(self.lb_bairro)
        layout.addWidget(self.inpt_bairo)

        layout.addWidget(self.lb_cidade)
        layout.addWidget(self.inpt_cidade)

        layout.addWidget(self.lb_logradouro)
        layout.addWidget(self.inpt_logradouro)

        #insere o layout dentro do frame
        frame = QFrame()
        frame.setLayout(layout)

        self.setCentralWidget(frame)

        self.inpt_cep.editingFinished.connect(self.busca_cep)

    def busca_cep(self):
        resultado = pycep_correios.get_address_from_cep(self.inpt_cep.text())
        self.inpt_bairo.setText(resultado['bairro'])
        self.inpt_cidade.setText(resultado['cidade'])
        self.inpt_logradouro.setText(resultado['logradouro'])

app = QApplication()

window = MainWindow()
window.show()

app.exec()

cep = pycep_correios.get_address_from_cep('07161150')

print(cep)