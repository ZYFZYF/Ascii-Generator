# coding=utf-8
__author__ = 'ZYF'

import Ascii
from PIL import Image, ImageDraw, ImageFont

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
GREY_ORDERED_ASCII = Ascii.getGreyOrderedAscii()

def fromImageToAsciiArray(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
    height, width = image.size
    blockHeight, blockWidth = blockShape
    asciiResult = ''
    for j in range(0, int(height / blockHeight)):
        for i in range(0, int(width / blockWidth)):
            left = i * blockWidth
            upper = j * blockHeight
            right = left + blockWidth
            lower = upper + blockHeight
            blockGrey = Ascii.getAverageGreyInImage(image.crop((left,upper,right,lower)))
            blockGreyRank = int(blockGrey / (256) * len(GREY_ORDERED_ASCII))
            asciiResult += GREY_ORDERED_ASCII[blockGreyRank]
        asciiResult += '\n'
    return asciiResult

def fromImageToAsciiImage(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
    asciiArray = fromImageToAsciiArray(image, blockShape)
    blockHeight, blockWidth = blockShape
    blockVerticalCount = len(asciiArray.splitlines())
    blockhorizontalCount = len(asciiArray.splitlines()[0])
    imageHeight = blockHeight * blockVerticalCount
    imageWidth = blockWidth * blockhorizontalCount
    asciiImage = Image.new('RGB', (imageWidth, imageHeight), (255,255,255))
    drawer = ImageDraw.Draw(asciiImage)
    for i,line in enumerate(asciiArray.splitlines()):
        for j,ascii in enumerate(line):
            leftCorner = [j * blockWidth, i * blockHeight]
            font = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc', blockHeight, 0)
            fill = (0, 0, 0)
            drawer.text(leftCorner, ascii, font=font, fill=fill)
    return asciiImage

if __name__ == '__main__':
    image = Image.open('sample1_src.jpg')
    file = open('test.txt','w')
    fromImageToAsciiImage(image).show()
