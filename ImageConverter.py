# coding=utf-8
__author__ = 'ZYF'

import Ascii
from PIL import Image, ImageDraw, ImageFont
import numpy
import datetime

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
GREY_ORDERED_ASCII = Ascii.getGreyOrderedAscii()

def fromImageToAsciiArray(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
    width, height = image.size
    blockHeight, blockWidth = blockShape
    blockVerticalCount = int(height / blockHeight)
    blockhorizontalCount = int(width / blockWidth)
    imageGreyArray = numpy.array(image.convert('L'))
    asciiResult = ''
    for row in range(0,blockVerticalCount):
        for col in range(0,blockhorizontalCount):
            upper = row * blockHeight
            left = col * blockWidth
            lower = upper + blockHeight
            right = left + blockWidth
            blockGreyAverage = numpy.mean(imageGreyArray[upper:lower,left:right])
            blockGreyRank = int(blockGreyAverage / 256 * len(GREY_ORDERED_ASCII))
            asciiResult += GREY_ORDERED_ASCII[blockGreyRank]
        asciiResult += '\n'
    return asciiResult

def fromImageToAsciiImage(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
    asciiArray = fromImageToAsciiArray(image, blockShape)
    blockHeight, blockWidth = blockShape
    width, height = image.size
    blockVerticalCount = int(height / blockHeight)
    blockhorizontalCount = int(width / blockWidth)
    imageHeight = blockHeight * blockVerticalCount
    imageWidth = blockWidth * blockhorizontalCount
    asciiImage = Image.new('RGB', (imageWidth, imageHeight), (255,255,255))
    drawer = ImageDraw.Draw(asciiImage)

    font = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc', blockHeight, 0)
    fill = (0, 0, 0)
    for i,line in enumerate(asciiArray.splitlines()):#draw every line
        leftCorner = [0, i * blockHeight]
        drawer.text(leftCorner, line, font=font, fill=fill)
    return asciiImage

if __name__ == '__main__':
    starttime = datetime.datetime.now()
    image = Image.open('sample4_src.jpg')
    array = fromImageToAsciiArray(image)
    endtime = datetime.datetime.now()
    print('Array cost %d.%ds' %((endtime-starttime).seconds, int((endtime-starttime).microseconds/1000)))
    starttime = endtime
    fromImageToAsciiImage(image).save('sample4_dst.jpg')
    endtime = datetime.datetime.now()
    print('Array cost %d.%ds' %((endtime-starttime).seconds, int((endtime-starttime).microseconds/1000)))
