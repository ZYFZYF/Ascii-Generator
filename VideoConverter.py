# coding=utf-8
__author__ = 'ZYF'

import cv2
from ImageConverter import *
from PIL import Image
import numpy
import datetime
import AudioManager
from Converter import Converter

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
class VideoConverter(Converter):
    imageConverter = ImageConverter()

    def __init__(self):
        super(VideoConverter, self).__init__()

    def fromVideoToAsciiVideo(self, srcFileName, dstFileName, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
        self.start()
        self.setNowTask.emit(0)
        self.describeTask.emit('解析视频中...')
        src = cv2.VideoCapture(srcFileName)
        fps = round(src.get(cv2.CAP_PROP_FPS))
        frames = src.get(cv2.CAP_PROP_FRAME_COUNT)
        self.getNewTasks.emit(frames)
        fourcc = int(src.get(cv2.CAP_PROP_FOURCC))
        print(('video description: fps = %d, frames = %d, fourcc = %d') % (fps, frames, fourcc))
        if src.isOpened() == False:
            self.describeTask.emit('解析视频失败╮(╯▽╰)╭')
            self.finishTask.emit()
            return
        dst = ''
        isFirst = True
        count = 0
        while (True):
            starttime = datetime.datetime.now()
            ret, frame = src.read()
            if self.isCanceled():
                self.setNowTask.emit(0)
                self.describeTask.emit('您取消了任务╮(╯▽╰)╭')
                break
            else:
                if ret:
                    self.describeTask.emit('正在转换第%d帧,共%d帧' % (count + 1, frames))
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
        if not self.isCanceled():
            self.describeTask.emit('正在拷贝音频...')
            print(srcFileName, dstFileName)
            AudioManager.copyAudioBetweenVideo(srcFileName, dstFileName)
            self.describeTask.emit('转换成功!╮(￣▽￣)╭')
        self.finishTask.emit()
