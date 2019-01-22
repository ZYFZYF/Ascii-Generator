# coding=utf-8
__author__ = 'ZYF'

from PIL import Image, ImageDraw, ImageFont
import numpy

GREY_ORDER = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
ASCII_GROUP = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()*+,-./:;\"<=>?@[\\]^_{|}~ "
FONT_SIZE = 32 #32px
IMAGE_WIDTH = 16 #32px = (16px,32px)
IMAGE_HEIGHT = 32

def getAverageGreyInImage(image):
    image = image.convert('L')
    greyArray = numpy.array(image)
    width,height = greyArray.shape
    return numpy.average(greyArray.reshape(width * height))

def getGreyOrderedAscii():
    greyGroup = {}
    for i in ASCII_GROUP:
        image = Image.new('RGB',(IMAGE_WIDTH,IMAGE_HEIGHT),(255,255,255))
        drawer = ImageDraw.Draw(image)
        font = ImageFont.truetype('C:\\Windows\\Fonts\\simsun.ttc',FONT_SIZE,0)
        fill = (0,0,0)
        drawer.text([0,0],i,font = font,fill = fill)
        greyGroup[i] = getAverageGreyInImage(image)
    greyGroup = sorted(greyGroup.items(), key = lambda x : x[1])#sort by grey
    resultOrder = ''
    for i in greyGroup:
        resultOrder = resultOrder + i[0]
    return resultOrder

if __name__ == '__main__':
    print(getGreyOrderedAscii())