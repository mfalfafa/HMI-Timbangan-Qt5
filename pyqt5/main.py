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

# Window variables
mainwin=''
loginwin=''
verificationwin=''

# Component variables
rfid_val=''

class VerificationWindow(QMainWindow, verificationwindow.Ui_Form):
    def submit(self):
        self.close()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        # Move to the center of window
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())
        # Always on top
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.lbl_berat.setMargin(10)
        self.pb_submit.released.connect(self.submit)
        self.exit_pb.released.connect(self.close)
        
# create class for our Raspberry Pi GUI
class LoginWindow(QMainWindow, loginwindow.Ui_Form):
    def retPressed(self):
        global rfid_val,loginwin,mainwin
        if rfid_val.text() == '123':
            self.close()
            mainwin.show()

    def __init__(self):
        global rfid_val
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        rfid_val=self.rfid_val
        rfid_val.returnPressed.connect(self.retPressed)

# create class for our Raspberry Pi GUI
class MainWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def pb_rework_press(self):
        pass
    def logout(self):
        global loginwin,rfid_val
        self.close()
        loginwin.show()
        rfid_val.setText('')
        rfid_val.setFocus()

    def kirim(self):
        global verificationwin
        verificationwin.show()

    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pb_logout.released.connect(self.logout)
        self.pb_kirim.released.connect(self.kirim)
        
# I feel better having one of these
def main():
    global mainwin,loginwin,verificationwin,rfid_val
    # a new app instance
    app = QApplication(sys.argv)
    mainwin = MainWindow()
    loginwin = LoginWindow()
    verificationwin = VerificationWindow()
    # mainwin.show()
    loginwin.show()
    rfid_val.setFocus()
    # verificationwin.show()
    # without this, the script exits immediately.
    sys.exit(app.exec_())

# python bit to figure how who started This
if __name__ == "__main__":
    main()
