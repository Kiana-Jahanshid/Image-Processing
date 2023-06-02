import cv2
import numpy as np
import random
from PySide6.QtWidgets import *
from PySide6.QtCore import * 
from PySide6.QtGui import *
from main_window import Ui_MainWindow
from PySide6 import QtWidgets 
from PySide6.QtGui import QPixmap 
from PySide6 import QtGui
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication
from encryptor import encryption
from decryptor import decryption


class MainWindow(QMainWindow ):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self )

        self.initUI()
        self.label_1 =  QLabel()
        self.label_2 =  QLabel()
        self.label_3 =  QLabel()

        self.ui.Encryption.clicked.connect(self.encryption)
        self.ui.Decryption.clicked.connect(self.decryption)


    def encryption(self):
        global enc_image , key
        enc_image , key = encryption()


    def decryption(self):
        dec_image = decryption(enc_image , key)


    def initUI(self):
        self.label = QtWidgets.QLabel()
        self.label.setPixmap(QtGui.QPixmap("van.jpg"))

        self.Encription = QtWidgets.QPushButton()
        self.Encription.setText("Encription")

        self.Decryption = QtWidgets.QPushButton()
        self.Decryption.setText("Decryption")

        self.possition(self.Encription ,self.Decryption , self.label)

    def possition(self,enc,dec,label):
        hBox = QtWidgets.QHBoxLayout()
        vBox = QtWidgets.QVBoxLayout()
        vBox.addWidget(enc)
        vBox.addWidget(dec)
        vBox.addWidget(label)
        hBox.addLayout(vBox)
        self.setLayout(hBox)


    def dec(self):
        self.label.setPixmap(QtGui.QPixmap("decrypted_image.jpg"))
    def enc(self):
        self.label.setPixmap(QtGui.QPixmap("encrypted_cipher_image.bmp"))

if __name__ == "__main__" :

    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()
