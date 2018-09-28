# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Qt\HMI_Timbangan\verificationwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 400)
        Form.setStyleSheet("background-color: rgb(0, 85, 255);")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(155, 10, 290, 50))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 18pt \"Arial Black\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pb_submit = QtWidgets.QPushButton(Form)
        self.pb_submit.setGeometry(QtCore.QRect(0, 340, 600, 60))
        self.pb_submit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.pb_submit.setObjectName("pb_submit")
        self.gridWidget = QtWidgets.QWidget(Form)
        self.gridWidget.setGeometry(QtCore.QRect(20, 100, 561, 221))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.cb_mesin = QtWidgets.QComboBox(self.gridWidget)
        self.cb_mesin.setMinimumSize(QtCore.QSize(0, 35))
        self.cb_mesin.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.cb_mesin.setObjectName("cb_mesin")
        self.cb_mesin.addItem("")
        self.cb_mesin.addItem("")
        self.cb_mesin.addItem("")
        self.gridLayout.addWidget(self.cb_mesin, 0, 1, 1, 1)
        self.cb_line = QtWidgets.QComboBox(self.gridWidget)
        self.cb_line.setMinimumSize(QtCore.QSize(0, 35))
        self.cb_line.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.cb_line.setObjectName("cb_line")
        self.cb_line.addItem("")
        self.cb_line.addItem("")
        self.cb_line.addItem("")
        self.gridLayout.addWidget(self.cb_line, 0, 3, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(80, 0))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.cb_kategori = QtWidgets.QComboBox(self.gridWidget)
        self.cb_kategori.setMinimumSize(QtCore.QSize(0, 35))
        self.cb_kategori.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(225, 225, 225);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.cb_kategori.setObjectName("cb_kategori")
        self.cb_kategori.addItem("")
        self.cb_kategori.addItem("")
        self.cb_kategori.addItem("")
        self.gridLayout.addWidget(self.cb_kategori, 1, 1, 1, 3)
        self.lbl_berat = QtWidgets.QLabel(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_berat.sizePolicy().hasHeightForWidth())
        self.lbl_berat.setSizePolicy(sizePolicy)
        self.lbl_berat.setMinimumSize(QtCore.QSize(0, 50))
        self.lbl_berat.setStyleSheet("color: rgb(255, 0, 0);\n"
"background-color: rgb(225, 225, 225);\n"
"font: 87 14pt \"Arial Black\";")
        self.lbl_berat.setObjectName("lbl_berat")
        self.gridLayout.addWidget(self.lbl_berat, 2, 1, 1, 3)
        self.exit_pb = QtWidgets.QPushButton(Form)
        self.exit_pb.setGeometry(QtCore.QRect(540, 10, 50, 41))
        self.exit_pb.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(243, 0, 0);\n"
"font: 75 28pt \"Arial\";")
        self.exit_pb.setObjectName("exit_pb")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Verifikasi Timbangan"))
        self.pb_submit.setText(_translate("Form", "SUBMIT"))
        self.label_3.setText(_translate("Form", "Mesin :"))
        self.cb_mesin.setItemText(0, _translate("Form", "Mesin 1"))
        self.cb_mesin.setItemText(1, _translate("Form", "Mesin 2"))
        self.cb_mesin.setItemText(2, _translate("Form", "Mesin 3"))
        self.cb_line.setItemText(0, _translate("Form", "Line 1"))
        self.cb_line.setItemText(1, _translate("Form", "Line 2"))
        self.cb_line.setItemText(2, _translate("Form", "Line 3"))
        self.label_4.setText(_translate("Form", "Kategori :"))
        self.label_5.setText(_translate("Form", "Berat (gr) :"))
        self.label_2.setText(_translate("Form", "Line :"))
        self.cb_kategori.setItemText(0, _translate("Form", "Kategori 1"))
        self.cb_kategori.setItemText(1, _translate("Form", "Kategori 2"))
        self.cb_kategori.setItemText(2, _translate("Form", "Kategori 3"))
        self.lbl_berat.setText(_translate("Form", "100"))
        self.exit_pb.setText(_translate("Form", "x"))

