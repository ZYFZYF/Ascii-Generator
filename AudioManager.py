# coding=utf-8
__author__ = 'ZYF'

import os

def getAudioFromVideo(srcVideoFileName, dstAudioFileName):
    #ffmpeg -i input_file -acodec copy -vn output_file_audio
    cmd = 'ffmpeg -i \"' + srcVideoFileName + '\" -acodec copy -vn \"' + dstAudioFileName + '\" -y'
    print(cmd)
    os.system(cmd)

def getAudioWithVideo(srcVideoFileName, srcAudioFileName, dstVedioFileName):
    #ffmpeg –i video_file –i audio_file –vcodec copy –acodec copy output_file
    cmd = 'ffmpeg -i \"' + srcVideoFileName + '\" -i \"' +  srcAudioFileName +'\" -vcodec copy -acodec copy \"' + dstVedioFileName + '\" -y'
    print(cmd)
    os.system(cmd)

def copyAudioBetweenVideo(srcVideoFileName, dstVideoFileName):
    tmpVideoFileName = os.path.splitext(dstVideoFileName)[0] + '_without_audio' + os.path.splitext(dstVideoFileName)[1]
    print(tmpVideoFileName)
    print('rename ',dstVideoFileName, tmpVideoFileName, os.path.abspath(dstVideoFileName), os.path.abspath(tmpVideoFileName))
    rename = 'ren ' + '\"' + os.path.abspath(dstVideoFileName) + '\"' + ' ' + '\"' +os.path.basename(tmpVideoFileName) + '\"'
    #os.rename(os.path.abspath(dstVideoFileName), os.path.abspath(tmpVideoFileName))
    os.system(rename)
    print(rename)
    tmpAudioFileName = os.path.splitext(srcVideoFileName)[0] + '.aac'
    print('get aac ', srcVideoFileName, tmpAudioFileName)
    getAudioFromVideo(srcVideoFileName, tmpAudioFileName)
    print('copy aac ', tmpVideoFileName, tmpAudioFileName, dstVideoFileName)
    getAudioWithVideo(tmpVideoFileName, tmpAudioFileName, dstVideoFileName)
    print('remove tmpvideo', tmpVideoFileName, os.path.abspath(tmpVideoFileName))
    delete = 'del ' + '\"' + os.path.abspath(tmpVideoFileName) + '\"'
    #os.remove(os.path.abspath(tmpVideoFileName))
    os.system(delete)
    print(delete)
    print('remove tmpaudio', tmpAudioFileName)
    delete = 'del ' + '\"' + os.path.abspath(tmpAudioFileName) + '\"'
    os.system(delete)

if __name__ == '__main__':
    copyAudioBetweenVideo('yuzhou.mp4', 'yuzhou_out.mp4')

