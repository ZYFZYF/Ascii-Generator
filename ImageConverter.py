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

def fromImageToAsciiImage(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH), isColored = False):
    asciiArray, colorArray = fromImageToAsciiArray(image, blockShape)
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
        print('TAT')
        for i, line in enumerate(asciiArray.splitlines()):
            for j, ascii in enumerate(line):
                leftCorner = [j * blockWidth, i * blockHeight]
                drawer.text(leftCorner, ascii, font=font, fill=(colorArray[i,j,0], colorArray[i,j,1], colorArray[i,j,2]))
    else:
        fill = (0, 0, 0)
        for i, line in enumerate(asciiArray.splitlines()):#draw every line
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
    fromImageToAsciiImage(image, isColored=True).save('sample4_dst.jpg')
    endtime = datetime.datetime.now()
    print('Array cost %d.%ds' %((endtime-starttime).seconds, int((endtime-starttime).microseconds/1000)))
