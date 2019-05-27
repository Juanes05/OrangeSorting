# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1210, 787)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 20, 891, 681))
        self.groupBox_2.setObjectName("groupBox_2")
        self.display = QtWidgets.QLabel(self.groupBox_2)
        self.display.setGeometry(QtCore.QRect(130, 60, 640, 480))
        self.display.setText("")
        self.display.setObjectName("display")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 600, 231, 71))
        self.groupBox.setObjectName("groupBox")
        self.captura = QtWidgets.QPushButton(self.groupBox)
        self.captura.setGeometry(QtCore.QRect(10, 30, 93, 28))
        self.captura.setObjectName("captura")
        self.stop = QtWidgets.QPushButton(self.groupBox)
        self.stop.setGeometry(QtCore.QRect(120, 30, 93, 28))
        self.stop.setObjectName("stop")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(700, 590, 171, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(20, 40, 55, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit.setGeometry(QtCore.QRect(70, 40, 71, 16))
        self.lineEdit.setObjectName("lineEdit")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(960, 20, 211, 171))
        self.groupBox_4.setObjectName("groupBox_4")
        self.new_2 = QtWidgets.QPushButton(self.groupBox_4)
        self.new_2.setGeometry(QtCore.QRect(10, 90, 121, 28))
        self.new_2.setObjectName("new_2")
        self.calib = QtWidgets.QPushButton(self.groupBox_4)
        self.calib.setGeometry(QtCore.QRect(10, 130, 121, 28))
        self.calib.setObjectName("calib")
        self.select = QtWidgets.QComboBox(self.groupBox_4)
        self.select.setGeometry(QtCore.QRect(10, 50, 121, 28))
        self.select.setObjectName("select")
        #self.select.addItem("")
        #self.select.addItem("")
        self.label_2 = QtWidgets.QLabel(self.groupBox_4)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 91, 21))
        self.label_2.setObjectName("label_2")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1210, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Estamos Melos 2.0"))
        self.groupBox_2.setTitle(_translate("mainWindow", "Visualización"))
        self.groupBox.setTitle(_translate("mainWindow", "Control"))
        self.captura.setText(_translate("mainWindow", "Clasificar"))
        self.stop.setText(_translate("mainWindow", "Parar"))
        self.groupBox_3.setTitle(_translate("mainWindow", "Area Superficial"))
        self.label.setText(_translate("mainWindow", "Medida:"))
        self.groupBox_4.setTitle(_translate("mainWindow", "Configuración"))
        self.new_2.setText(_translate("mainWindow", "Ingresar nueva fruta"))
        self.calib.setText(_translate("mainWindow", "Calibrar distancia"))
        #self.select.setItemText(0, _translate("mainWindow", "Naranja Valencia"))
        #self.select.setItemText(1, _translate("mainWindow", "test"))
        self.label_2.setText(_translate("mainWindow", "Fruta selecionada"))


