# coding=utf-8
__author__ = 'ZYF'

import os

def getAudioFromVideo(srcVideoFileName, dstAudioFileName):
    #ffmpeg -i input_file -acodec copy -vn output_file_audio
    print('ffmpeg -i ' + srcVideoFileName + ' -acodec copy -vn ' + dstAudioFileName)
    os.system('ffmpeg -i ' + srcVideoFileName + ' -acodec copy -vn ' + dstAudioFileName)

def getAudioWithVideo(srcVideoFileName, srcAudioFileName, dstVedioFileName):
    print('ffmpeg –i ' + srcVideoFileName + ' –i ' +  srcAudioFileName +' –vcodec copy –acodec copy ' + dstVedioFileName)
    #ffmpeg –i video_file –i audio_file –vcodec copy –acodec copy output_file
    os.system('ffmpeg -i ' + srcVideoFileName + ' -i ' + srcAudioFileName + ' –vcodec copy –acodec copy ' + dstVedioFileName)

def copyAudioBetweenVideo(srcVideoFileName, dstVideoFileName):
    tmpVideoFileName = dstVideoFileName.split('.')[0] + '_without_audio.' + dstVideoFileName.split('.')[1]
    print('rename ' + dstVideoFileName + ' ' + tmpVideoFileName)
    os.system('rename ' + dstVideoFileName + ' ' + tmpVideoFileName)
    tmpAudioFileName = srcVideoFileName.split('.')[0] + '.aac'
    getAudioFromVideo(srcVideoFileName, tmpAudioFileName)
    getAudioWithVideo(tmpVideoFileName, tmpAudioFileName, dstVideoFileName)
    os.system('del ' + tmpVideoFileName)

if __name__ == '__main__':
    copyAudioBetweenVideo('testsrc.mp4', 'testdst.mp4')
