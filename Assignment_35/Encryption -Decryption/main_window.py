# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ENC_CEDReHtXn.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide6.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(954, 339)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Encryption = QPushButton(self.centralwidget)
        self.Encryption.setObjectName(u"Encryption")
        self.Encryption.setGeometry(QRect(230, 130, 101, 51))
        font = QFont()
        font.setPointSize(11)
        self.Encryption.setFont(font)
        self.Encryption.setStyleSheet(u"background-color: rgb(0, 170, 127);")
        self.Decryption = QPushButton(self.centralwidget)
        self.Decryption.setObjectName(u"Decryption")
        self.Decryption.setGeometry(QRect(590, 130, 111, 51))
        self.Decryption.setFont(font)
        self.Decryption.setStyleSheet(u"background-color: rgb(170, 85, 255);")
        self.commandLinkButton = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(330, 130, 41, 48))
        self.commandLinkButton_2 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_2.setObjectName(u"commandLinkButton_2")
        self.commandLinkButton_2.setGeometry(QRect(200, 130, 41, 48))
        self.commandLinkButton_3 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_3.setObjectName(u"commandLinkButton_3")
        self.commandLinkButton_3.setGeometry(QRect(560, 130, 41, 48))
        self.commandLinkButton_4 = QCommandLinkButton(self.centralwidget)
        self.commandLinkButton_4.setObjectName(u"commandLinkButton_4")
        self.commandLinkButton_4.setGeometry(QRect(700, 130, 41, 48))
        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setGeometry(QRect(10, 50, 191, 191))
        self.label_1.setPixmap(QPixmap(u"van.jpg"))
        self.label_1.setScaledContents(True)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 50, 201, 191))
        self.label_2.setPixmap(QPixmap(u"encryption_CipherImage.bmp"))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(730, 50, 201, 191))
        self.label_3.setPixmap(QPixmap(u"decrypted_image.jpg"))
        self.label_3.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 954, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Encryption.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.Decryption.setText(QCoreApplication.translate("MainWindow", u" Decryption", None))
        self.commandLinkButton.setText("")
        self.commandLinkButton_2.setText("")
        self.commandLinkButton_3.setText("")
        self.commandLinkButton_4.setText("")
        self.label_1.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
    # retranslateUi

