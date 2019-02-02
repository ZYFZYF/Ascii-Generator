# coding=utf-8
__author__ = 'ZYF'

import Ascii
from PIL import Image, ImageDraw, ImageFont
import numpy
import datetime
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
GREY_ORDERED_ASCII = Ascii.getGreyOrderedAscii()
class ImageConverter(QObject):
    getNewTasks = pyqtSignal(int)
    setNowTask = pyqtSignal(int)
    finishTask = pyqtSignal()
    stop = False

    def __init__(self):
        super(ImageConverter, self).__init__()

    def setStop(self, stop):
        self.stop = stop


    def fromImageToAsciiArray(self, image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
        width, height = image.size
        blockHeight, blockWidth = blockShape
        blockVerticalCount = int(height / blockHeight)
        blockhorizontalCount = int(width / blockWidth)
        r, g, b = image.split()
        imageGreyArray = numpy.array(image.convert('L'))
        imageBlueArray = numpy.array(r)
        imageGreenArray = numpy.array(g)
        imageRedArray = numpy.array(b)
        asciiResult = ''
        colorResult = numpy.zeros((blockVerticalCount, blockhorizontalCount, 3), dtype=numpy.int)
        for row in range(0,blockVerticalCount):
            for col in range(0,blockhorizontalCount):
                upper = row * blockHeight
                left = col * blockWidth
                lower = upper + blockHeight
                right = left + blockWidth
                blockGreyAverage = numpy.mean(imageGreyArray[upper:lower,left:right])
                blockGreyRank = int(blockGreyAverage / 256 * len(GREY_ORDERED_ASCII))
                asciiResult += GREY_ORDERED_ASCII[blockGreyRank]
                colorResult[row, col]= [int(numpy.mean(imageBlueArray[upper:lower,left:right])),
                                    int(numpy.mean(imageGreenArray[upper:lower,left:right])),
                                    int(numpy.mean(imageRedArray[upper:lower, left:right]))]
            asciiResult += '\n'
        return asciiResult,colorResult

    def fromImageToAsciiImage(self, image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
        self.setStop(False)
        asciiArray, colorArray = self.fromImageToAsciiArray(image, blockShape)
        blockHeight, blockWidth = blockShape
        width, height = image.size
        blockVerticalCount = int(height / blockHeight)
        blockhorizontalCount = int(width / blockWidth)
        imageHeight = blockHeight * blockVerticalCount
        imageWidth = blockWidth * blockhorizontalCount
        asciiImage = Image.new('RGB', (imageWidth, imageHeight), (255,255,255))
        drawer = ImageDraw.Draw(asciiImage)

        font = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc', blockHeight, 0)

        if isColored:
            self.getNewTasks.emit(blockhorizontalCount * blockVerticalCount)
            for i, line in enumerate(asciiArray.splitlines()):
                for j, ascii in enumerate(line):
                    if not self.stop:
                        leftCorner = [j * blockWidth, i * blockHeight]
                        drawer.text(leftCorner, ascii, font=font, fill=(colorArray[i,j,0], colorArray[i,j,1], colorArray[i,j,2]))
                        self.setNowTask.emit(i * blockhorizontalCount + j + 1)
        else:
            self.getNewTasks.emit(blockVerticalCount)
            fill = (0, 0, 0)
            for i, line in enumerate(asciiArray.splitlines()):#draw every line
                if not self.stop:
                    leftCorner = [0, i * blockHeight]
                    drawer.text(leftCorner, line, font=font, fill=fill)
                    self.setNowTask.emit(i + 1)
        return asciiImage

    def fromPictureToPicture(self, srcFileName, dstFileName, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
        image = Image.open(srcFileName)
        self.fromImageToAsciiImage(image, blockShape, isColored).save(dstFileName)
        self.finishTask.emit()

    def fromPictureToText(self, srcFileName, dstFileName, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
        image = Image.open(srcFileName)
        file = open(dstFileName, 'w')
        asciiResult, _ = self.fromImageToAsciiArray(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH))
        file.write(asciiResult)
        file.close()
        self.finishTask.emit()
