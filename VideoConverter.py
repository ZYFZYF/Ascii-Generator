# coding=utf-8
__author__ = 'ZYF'

import cv2
from ImageConverter import *
from PIL import Image
import numpy
import datetime
import AudioManager
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
class VideoConverter(QObject):

    getNewTasks = pyqtSignal(int)
    setNowTask = pyqtSignal(int)
    finishTask = pyqtSignal()
    stop = False
    imageConverter = ImageConverter()
    def __init__(self):
        super(VideoConverter, self).__init__()

    def setStop(self, stop):
        self.stop = stop

    def fromVideoToAsciiVideo(self, srcFileName, dstFileName, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
        self.setStop = True
        src = cv2.VideoCapture(srcFileName)
        fps = round(src.get(cv2.CAP_PROP_FPS))
        frames = src.get(cv2.CAP_PROP_FRAME_COUNT)
        self.getNewTasks.emit(frames)
        fourcc = int(src.get(cv2.CAP_PROP_FOURCC))
        dst = ''
        isFirst = True
        count = 0
        while (True):
            starttime = datetime.datetime.now()
            ret, frame = src.read()
            if ret and not self.stop:
                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                asciiImage = self.imageConverter.fromImageToAsciiImage(image, blockShape=blockShape, isColored=isColored)
                asciiFrame = cv2.cvtColor(numpy.asarray(asciiImage), cv2.COLOR_RGB2BGR)
                if isFirst:
                    isFirst = False
                    dst = cv2.VideoWriter(dstFileName, fourcc, fps, asciiImage.size)
                dst.write(asciiFrame)
                count += 1
                self.setNowTask.emit(count)
                endtime = datetime.datetime.now()
                print('Frame %d/%d cost %d.%ds' % (count,frames,(endtime - starttime).seconds, int((endtime - starttime).microseconds / 1000)))
            else:
                break

        src.release()
        dst.release()
        cv2.destroyAllWindows()
        if not self.stop:
            AudioManager.copyAudioBetweenVideo(srcFileName, dstFileName)
        self.finishTask.emit()

if __name__ == '__main__':
    videoConverter = VideoConverter()
    videoConverter.fromVideoToAsciiVideo('720OP1.mp4', '四月OP.mp4', isColored=True)