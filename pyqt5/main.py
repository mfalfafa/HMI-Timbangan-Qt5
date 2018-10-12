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
import serial.tools.list_ports
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
lbl_berat_gr=''

# variables
timeThread=''
serialThread=''
ready_setup=0
serData=''
ready_to_count=0

class SerialThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        getSerialData()

def getSerialData():
    global serData,lbl_berat_gr,ready_to_count
    ## Establish connection to COM Port
    ## Connection from HMI
    connected = False
    ser_rfid=''
    comlist = serial.tools.list_ports.comports()
    print('wait for serial...')
    ## loop until the device tells us it is ready
    while not connected:
        ## COM Port settings
        for device in comlist: 
            try:
                # print ("Trying...",device)
                ## Serial Initialization
                ser_rfid = serial.Serial(device[0],      #port
                                    9600,              #baudrate
                                    serial.EIGHTBITS,   #bytesize
                                    serial.PARITY_NONE,  #parity
                                    serial.STOPBITS_ONE,#stop bit
                                    0,                  #timeout
                                    False,              #xonxoff
                                    False,              #rtscts
                                    0,                  #write_timeout
                                    False,              #dsrdtr
                                    None,               #inter byte timeout
                                    # None              #exclusive
                                    )
                connected=True
            except Exception as e:
                connected=False
                print ("trying to connect to ", device)
                time.sleep(1.5)

    if connected:
        serin = ser_rfid.read()
        print ("Connected to ",device)
        connected=False

    while 1:
        if ready_to_count==1:
            time.sleep(0.5)
            try:
                if ser_rfid.inWaiting():
                    x=ser_rfid.read()
                    x=x.decode('ascii')
                    serData=serData + str(x)
                    if x == '\r':
                        n=len(str(serData))
                        m=len(str(serData))-4
                        start = n-m
                        end = serData.index( 'kg', start )
                        serData = serData[start:end]
                        # Omit space in string
                        serData = serData.replace(' ','')
                        lbl_berat_gr.setText(str(serData))
                        print(serData)
                        serData=''
            except:
                print ("Serial error")

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
        global rfid_val,loginwin,mainwin,ready_to_count
        if rfid_val.text() == '123':
            self.close()
            mainwin.show()
            ready_to_count=1

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
        global loginwin,rfid_val,ready_to_count
        self.close()
        loginwin.show()
        rfid_val.setText('')
        rfid_val.setFocus()
        ready_to_count=0

    def kirim(self):
        global verificationwin
        verificationwin.show()
        self.setEnabled(False)

    def __init__(self):
        global time_lbl,ready_setup,lbl_berat_gr
        super(self.__class__, self).__init__()
        self.setupUi(self) # gets defined in the UI file
        self.pb_logout.released.connect(self.logout)
        self.pb_kirim.released.connect(self.kirim)
        lbl_berat_gr=self.lbl_berat_gr
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
    serialThread=SerialThread()
except Exception as e:
    print ("Error: unable to start thread!")
    print (str(e))
# Start thread
timeThread.start()
serialThread.start()

# python bit to figure how who started This
if __name__ == "__main__":
    main()
