# coding=utf-8
__author__ = 'ZYF'

import cv2
import ImageConverter
from PIL import Image
import numpy
import datetime
import AudioManager


def fromVideoToAsciiVideo(srcFileName, dstFileName):
    src = cv2.VideoCapture(srcFileName)
    fps = round(src.get(cv2.CAP_PROP_FPS))
    frames = src.get(cv2.CAP_PROP_FRAME_COUNT)
    fourcc = int(src.get(cv2.CAP_PROP_FOURCC))
    print(fourcc, cv2.VideoWriter_fourcc('M', 'P', '4', '2'))
    print(fps,frames)
    dst = ''
    isFirst = True
    count = 0
    while (True):
        starttime = datetime.datetime.now()
        ret, frame = src.read()
        if ret:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            asciiImage = ImageConverter.fromImageToAsciiImage(image)
            asciiFrame = cv2.cvtColor(numpy.asarray(asciiImage), cv2.COLOR_RGB2BGR)
            if isFirst:
                isFirst = False
                dst = cv2.VideoWriter(dstFileName, fourcc, fps, asciiImage.size)
            dst.write(asciiFrame)
            count += 1
            endtime = datetime.datetime.now()
            print('Frame %d/%d cost %d.%ds' % (count,frames,(endtime - starttime).seconds, int((endtime - starttime).microseconds / 1000)))
        else:
            break

    src.release()
    dst.release()
    cv2.destroyAllWindows()
    AudioManager.copyAudioBetweenVideo(srcFileName, dstFileName)

if __name__ == '__main__':
    fromVideoToAsciiVideo('chaopao.mp4', 'chaopao_out.mp4')