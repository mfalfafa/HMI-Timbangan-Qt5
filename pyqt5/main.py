# always seem to need this
import sys
 
# For PostgreSQL database 
import psycopg2

# This gets the Qt stuff
import PyQt5
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QThread

# for serial communication
import serial
import time
import threading

# This is our window from QtCreator
import mainwindow
import loginwindow
import verificationwindow

class VerificationWindow(QMainWindow, verificationwindow.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.lbl_berat.setMargin(10)
        
# create class for our Raspberry Pi GUI
class LoginWindow(QMainWindow, loginwindow.Ui_Form):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def pb_rework_press(self):
        pass
        
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        
# I feel better having one of these
def main():
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    loginwin = LoginWindow()
    verwin = VerificationWindow()
    mainwin.show()
    loginwin.show()
    verwin.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
