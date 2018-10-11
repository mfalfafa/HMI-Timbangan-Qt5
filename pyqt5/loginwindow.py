# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/HMI-Timbangan-Qt5/loginwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 480)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(260, 215, 280, 50))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 170, 0);\n"
"font: 75 18pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.corner = QtWidgets.QLabel(Form)
        self.corner.setGeometry(QtCore.QRect(690, 390, 111, 91))
        self.corner.setText("")
        self.corner.setPixmap(QtGui.QPixmap("corner.png"))
        self.corner.setObjectName("corner")
        self.copyright = QtWidgets.QLabel(Form)
        self.copyright.setGeometry(QtCore.QRect(20, 440, 161, 31))
        self.copyright.setStyleSheet("font: 75 12pt \"Arial\";")
        self.copyright.setObjectName("copyright")
        self.hmi_type = QtWidgets.QLabel(Form)
        self.hmi_type.setGeometry(QtCore.QRect(620, 20, 161, 41))
        self.hmi_type.setStyleSheet("color: rgb(0, 155, 232);\n"
"font: 75 17pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.hmi_type.setFrameShape(QtWidgets.QFrame.Box)
        self.hmi_type.setAlignment(QtCore.Qt.AlignCenter)
        self.hmi_type.setObjectName("hmi_type")
        self.rfid_val = QtWidgets.QLineEdit(Form)
        self.rfid_val.setGeometry(QtCore.QRect(350, 270, 0, 0))
        self.rfid_val.setObjectName("rfid_val")
        self.logo_mv = QtWidgets.QLabel(Form)
        self.logo_mv.setGeometry(QtCore.QRect(20, 20, 91, 81))
        self.logo_mv.setText("")
        self.logo_mv.setPixmap(QtGui.QPixmap("MMM.png"))
        self.logo_mv.setScaledContents(True)
        self.logo_mv.setObjectName("logo_mv")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_5.setText(_translate("Form", "Tempelkan RFID"))
        self.copyright.setText(_translate("Form", "@MachineVision2018"))
        self.hmi_type.setText(_translate("Form", "Timbangan"))

