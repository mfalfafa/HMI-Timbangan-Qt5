# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:/Qt/HMI-Timbangan-Qt5/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 480)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(225, 0, 0);\n"
"font: 75 18pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(20, 70, 121, 31))
        self.label.setStyleSheet("color: rgb(229, 0, 0);\n"
"font: 75 18pt \"Arial\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(710, 70, 71, 31))
        self.label_3.setStyleSheet("color: rgb(229, 0, 0);\n"
"font: 87 14pt \"Arial Black\";")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalWidget.setGeometry(QtCore.QRect(20, 110, 761, 41))
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.horizontalWidget)
        self.label_6.setMinimumSize(QtCore.QSize(280, 0))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 255);\n"
"font: 75 18pt \"Arial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.verticalWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.verticalWidget_2.setGeometry(QtCore.QRect(50, 180, 181, 241))
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setBaseSize(QtCore.QSize(0, 0))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.comboBox = QtWidgets.QComboBox(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.label_8 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.verticalLayout.addWidget(self.comboBox_2)
        self.label_9 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.verticalLayout.addWidget(self.comboBox_3)
        self.verticalWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalWidget.setGeometry(QtCore.QRect(270, 180, 211, 241))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.verticalWidget)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.label_11.setFrameShape(QtWidgets.QFrame.Box)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 0);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_2.addWidget(self.pushButton_2)
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(20, 150, 761, 300))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-right-color: rgb(0, 170, 255);")
        self.label_12.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(500, 150, 2, 300))
        self.label_13.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.hmi_type = QtWidgets.QLabel(self.centralWidget)
        self.hmi_type.setGeometry(QtCore.QRect(620, 20, 161, 41))
        self.hmi_type.setStyleSheet("color: rgb(0, 155, 232);\n"
"font: 75 18pt \"Arial\";\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 170, 255);")
        self.hmi_type.setFrameShape(QtWidgets.QFrame.Box)
        self.hmi_type.setAlignment(QtCore.Qt.AlignCenter)
        self.hmi_type.setObjectName("hmi_type")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(590, 290, 91, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_12.raise_()
        self.pushButton.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.horizontalWidget.raise_()
        self.verticalWidget_2.raise_()
        self.label_13.raise_()
        self.hmi_type.raise_()
        self.verticalWidget.raise_()
        self.label_2.raise_()
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Logout"))
        self.label.setText(_translate("MainWindow", "Operator 1"))
        self.label_3.setText(_translate("MainWindow", "09:45"))
        self.label_5.setText(_translate("MainWindow", "Info"))
        self.label_4.setText(_translate("MainWindow", "Berat"))
        self.label_6.setText(_translate("MainWindow", "Histori"))
        self.label_7.setText(_translate("MainWindow", "Mesin"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Mesin 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Mesin 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Mesin 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Mesin 4"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Mesin 5"))
        self.label_8.setText(_translate("MainWindow", "Line"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Line 1"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Line 2"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Line 3"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Line 4"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Line 5"))
        self.label_9.setText(_translate("MainWindow", "Kategori"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "Kategori 1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "Kategori 2"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "Kategori 3"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "Kategori 4"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "Kategori 5"))
        self.label_10.setText(_translate("MainWindow", "Berat (gr)"))
        self.label_11.setText(_translate("MainWindow", "100"))
        self.pushButton_2.setText(_translate("MainWindow", "Kirim"))
        self.hmi_type.setText(_translate("MainWindow", "Timbangan"))
        self.label_2.setText(_translate("MainWindow", "Tidak ada data."))

