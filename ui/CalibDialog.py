# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalibDialog.ui'
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
        self.label.setGeometry(QtCore.QRect(20, 20, 351, 41))
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.next = QtWidgets.QPushButton(Dialog)
        self.next.setGeometry(QtCore.QRect(310, 260, 75, 23))
        self.next.setObjectName("next")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 47, 13))
        self.label_2.setObjectName("label_2")
        self.fruit_name = QtWidgets.QTextEdit(Dialog)
        self.fruit_name.setGeometry(QtCore.QRect(80, 70, 121, 16))
        self.fruit_name.setObjectName("fruit_name")
        self.p = QtWidgets.QRadioButton(Dialog)
        self.p.setGeometry(QtCore.QRect(30, 120, 151, 17))
        self.p.setObjectName("p")
        self.m = QtWidgets.QRadioButton(Dialog)
        self.m.setGeometry(QtCore.QRect(30, 150, 131, 17))
        self.m.setObjectName("m")
        self.g = QtWidgets.QRadioButton(Dialog)
        self.g.setGeometry(QtCore.QRect(30, 180, 131, 17))
        self.g.setObjectName("g")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Calibración"))
        self.label.setText(_translate("Dialog", "Ingrese en nombre de la nueva fruta y seleccione un tamaño. Para continuar presione siguiente."))
        self.next.setText(_translate("Dialog", "Siguiente"))
        self.label_2.setText(_translate("Dialog", "Nombre:"))
        self.p.setText(_translate("Dialog", "Pequeño (3 cm - 5cm )"))
        self.m.setText(_translate("Dialog", "Mediano (5cm - 7cm)"))
        self.g.setText(_translate("Dialog", "Grande (7cm - 9cm)"))


