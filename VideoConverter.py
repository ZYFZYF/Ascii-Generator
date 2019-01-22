# coding=utf-8
__author__ = 'ZYF'

import cv2
import ImageConverter
from PIL import Image
import numpy


def fromVideoToAsciiVideo(srcFileName, dstFileName):
    src = cv2.VideoCapture(srcFileName)
    dst = ''
    isFirst = True
    count = 0
    while (True):
        ret, frame = src.read()
        if ret:
            image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            image.convert()
            asciiImage = ImageConverter.fromImageToAsciiImage(image)
            asciiFrame = cv2.cvtColor(numpy.asarray(asciiImage), cv2.COLOR_RGB2BGR)
            if isFirst:
                isFirst = False
                dst = cv2.VideoWriter(dstFileName, cv2.VideoWriter_fourcc('M','J','P','G'), 25.0, asciiImage.size)
            dst.write(asciiFrame)
            count += 1
            print("frame %d" % count)
        else:
            break

    src.release()
    dst.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    fromVideoToAsciiVideo('720OP1.mp4', '720op1_out.mp4')