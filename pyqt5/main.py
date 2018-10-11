# always seem to need this
import sys
 
# For PostgreSQL database 
# import psycopg2

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
time_lbl=''

# variables
timeThread=''
ready_setup=0

class TimeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        timeValue()

def timeValue():
    global time_lbl,ready_setup
    while 1:        
        current_time=time.localtime(time.time())
        time_now=[0]*3
        time_now[0]=str(current_time.tm_hour)
        time_now[1]=str(current_time.tm_min)
        time_now[2]=str(current_time.tm_sec)
        current_time=''
        for i in range(3):
            if len(time_now[i])==1:
                time_now[i]='0'+time_now[i]
        current_time=time_now[0]+':'+time_now[1]+':'+time_now[2]
        if ready_setup==1:
            time_lbl.setText(current_time)
        time.sleep(1)

class VerificationWindow(QMainWindow, verificationwindow.Ui_Form):
    def submit(self):
        global mainwin
        self.close()
        mainwin.setEnabled(True)
    
    def closed(self):
        global mainwin
        self.close()
        mainwin.setEnabled(True)

    def __init__(self):
        global mainwin
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
        self.exit_pb.released.connect(self.closed)
        
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
        self.setEnabled(False)

    def __init__(self):
        global time_lbl,ready_setup
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pb_logout.released.connect(self.logout)
        self.pb_kirim.released.connect(self.kirim)
        time_lbl=self.time_lbl
        ready_setup=1
        
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

# Create new thread for sending data every second
try:
    timeThread=TimeThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
timeThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
