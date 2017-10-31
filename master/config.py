"""config"""
import os
import sys


MASTER_SOFTWARE_VERSION = 'V5.5Beta2'
MASTER_SOFTWARE_DT = '2017.10'
MASTER_WINDOW_TITLE_ADD = '_%s(%s)'%(MASTER_SOFTWARE_VERSION, MASTER_SOFTWARE_DT)
MASTER_ICO_PATH = 'imgs/698_v5.png'
TRANS_SOFTWARE_VERSION = 'VT1.2Beta2'
TRANS_SOFTWARE_DT = '2017.08'
TRANS_WINDOW_TITLE_ADD = '_%s(%s)'%(TRANS_SOFTWARE_VERSION, TRANS_SOFTWARE_DT)
TRANS_ICO_PATH = 'imgs/698_o.png'

TRANS_WINDOW = None
ABOUT_WINDOW = None
MASTER_WINDOW = None

COMMU = None

K_DATA = None

M_PRIORITY_COLOR = {0: 'grey', 1: 'black', 2: 'blue', 3: 'red'}

MSG_TABLE_ROW_MAX = 256

RE_MSG_TIMEOUT = 15
class Service():
    """service class"""
    def __init__(self):
        self.service_no = 0

    def get_service_no(self):
        """get service no"""
        self.service_no += 1
        if self.service_no >= 64:
            self.service_no = 1
        return self.service_no
SERVICE = Service()

CONFIG_FILE_PATH = os.path.join(os.path.expanduser('~'), '.698master/698master.conf')
MSG_LOG_DIR = os.path.join(os.path.expanduser('~'), '.698master/logs/')

IS_USE_PYSIDE = False

IS_FILETER_CA = True

RUN_EXE_PATH = ''
LOG_PATH = ''

if getattr(sys, 'frozen', False):
    SORTWARE_PATH = sys._MEIPASS
else:
    SORTWARE_PATH = os.path.join(os.path.split(os.path.realpath(__file__))[0], '..')
