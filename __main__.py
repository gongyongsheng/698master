'''main'''
import sys
import os
from UI.trans_ui import TransWindow
from PyQt4 import QtGui
import config

if __name__ == "__main__":
    APP = QtGui.QApplication(sys.argv)
    config.trans_window = TransWindow()
    config.trans_window.show()
    APP.exec_()
    os._exit(0)