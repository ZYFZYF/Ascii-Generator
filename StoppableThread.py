# coding=utf-8
__author__ = 'ZYF'

import threading

class StoppableThread(threading.Thread):

    def __init__(self):
        super(StoppableThread, self).__init__()
        self.__running = threading.Event()
        self.__running.set()

    def stop(self):
        self.__running.clear()
