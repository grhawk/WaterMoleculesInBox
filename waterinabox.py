#!/usr/bin/env python
import sys
from PyQt4 import QtGui, QtCore, uic
from PyQt4.QtGui import QMessageBox
import signal

form_class = uic.loadUiType("waterinabox.ui")[0]

molPerAngc = 0.033456

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # Bind the event handlers to the buttons
        self.btn_convert.clicked.connect(self.btn_convert_clicked)
        self.btn_reset.clicked.connect(self.btn_reset_clicked)
        
    def btn_convert_clicked(self):
        try:
            try:
                box_side = float(self.line_boxside.text())
                box_vol = box_side**3
                mol = int(molPerAngc * box_vol)
                self.line_watermolec.setText(str(mol))
                self.msg.setText('Done')
                self.line_boxside.clear()
            except:
                watermolec = float(self.line_watermolec.text())
                box_vol =  watermolec / molPerAngc
                box_side = box_vol**(1./3.)
                self.line_boxside.setText(str(box_side))
                self.msg.setText('Done')
                self.line_watermolec.clear()
        except ValueError:
            self.msg.setText('You have to provide some initial data\nStupid!')
            pass

    def btn_reset_clicked(self):
        self.line_boxside.clear()
        self.line_watermolec.clear()
        self.msg.clear()

def sigint_handler(*args):
    """Handler for the SIGINT signal"""
    sys.stderr.write('\r')
    # if QMessageBox.question(None, '', 'Are you sure you want to quit?',
    #                         QMessageBox.Yes | QMessageBox.No, 
    #                         QMessageBox.Yes) == QMessageBox.Yes:
    QtGui.QApplication.quit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigint_handler)
    app = QtGui.QApplication(sys.argv)
    timer = QtCore.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)
    myWindow = MyWindowClass(None)
    myWindow.show()
    sys.exit(app.exec_())
    
        
