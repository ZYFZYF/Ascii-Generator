# coding=utf-8
__author__ = 'ZYF'
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

class Converter(QObject):
    getNewTasks = pyqtSignal(int)
    setNowTask = pyqtSignal(int)
    finishTask = pyqtSignal()
    describeTask = pyqtSignal(str)
    cancelFlag = False

    def __init__(self):
        super(Converter, self).__init__()

    def cancel(self):
        self.cancelFlag = True

    def isCanceled(self):
        return self.cancelFlag

    def start(self):
        self.cancelFlag = False