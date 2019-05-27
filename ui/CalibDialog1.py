# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalibDialog1.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 20, 331, 41))
        self.label.setObjectName("label")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.next.setObjectName("next")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 120, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.falta = QtWidgets.QLabel(Dialog)
        self.falta.setGeometry(QtCore.QRect(160, 120, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.falta.setFont(font)
        self.falta.setObjectName("falta")
        self.start = QtWidgets.QPushButton(Dialog)
        self.start.setGeometry(QtCore.QRect(30, 260, 75, 23))
        self.start.setObjectName("start")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calibración"))
        self.label.setText(_translate("Dialog", "Presione iniciar y luego ingrese 5 frutas que se encuentren maduras."))
        self.next.setText(_translate("Dialog", "Finalizar"))
        self.label_2.setText(_translate("Dialog", "Frutas restantes:"))
        self.falta.setText(_translate("Dialog", "5"))
        self.start.setText(_translate("Dialog", "Inicio"))


