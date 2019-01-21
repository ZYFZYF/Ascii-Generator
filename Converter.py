# coding=utf-8
__author__ = 'ZYF'

import Ascii
from PIL import Image

DEFAULT_BLOCK_WIDTH = 5
DEFAULT_BLOCK_HEIGHT = 10
GREY_ORDERED_ASCII = Ascii.getGreyOrderedAscii()

def fromImageToAscii(image, blockShape=(DEFAULT_BLOCK_HEIGHT, DEFAULT_BLOCK_WIDTH)):
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

if __name__ == '__main__':
    image = Image.open('copyright.jpg')
    file = open('test.txt','w')
    file.write(fromImageToAscii(image))
