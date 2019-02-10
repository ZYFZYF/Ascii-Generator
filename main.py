# coding=utf-8
__author__ = 'ZYF'

import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QProgressDialog
from mainWindow import *
from VideoConverter import *
from ImageConverter import *
from threading import Thread
import chardet

ALL_SRC_FILE_TYPE = '图片(*.jpg;*.png);;视频(*.mp4;*.avi;*.mov;*.wmv;*.flv;*.rmvb)'
PICTURE_DST_FILE_TYPE = '图片(*.jpg;*.png);;文本文件(*.txt)'

VIDEO_FILE_SUFFIX = {'.mp4', '.avi', '.mov', '.wmv', '.flv', '.rmvb'}
PICTURE_FILE_SUFFIX = {'.jpg', '.png'}
TEXT_FILE_SUFFIX = {'.txt'}

def isVideo(fileName):
    try:
        return os.path.splitext(fileName)[1] in VIDEO_FILE_SUFFIX
    except:
        return False

def isPicture(fileName):
    try:
        return os.path.splitext(fileName)[1] in PICTURE_FILE_SUFFIX
    except:
        return False

def isText(fileName):
    try:
        return os.path.splitext(fileName)[1] in TEXT_FILE_SUFFIX
    except:
        return False

class MyWindow(QMainWindow, Ui_MainWindow):
    blockSize = 5
    isColored = False
    srcFileName = ''
    dstFileName = ''
    videoConverter = VideoConverter()
    imageConverter = ImageConverter()
    convertThread = Thread()

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.src_selector.clicked.connect(self.selectSrc)
        self.dst_selector.clicked.connect(self.selectDst)

        self.operate_button.clicked.connect(self.operateSelect)

        for i in range(1, 61):
            self.block_size_selector.addItem('%dpx'%(i))
        self.block_size_selector.setCurrentIndex(4)
        self.block_size_selector.currentIndexChanged.connect(self.setBlockSize)

        self.color_selector.addItems(['黑白','彩色'])
        self.color_selector.setCurrentIndex(0)
        self.color_selector.currentIndexChanged.connect(self.setIsColored)

        self.src_file_name_show.textChanged.connect(self.setSrcFileName)
        self.dst_file_name_show.textChanged.connect(self.setDstFileName)

        self.videoConverter.getNewTasks.connect(self.progress_show.setMaximum)
        self.videoConverter.setNowTask.connect(self.progress_show.setValue)
        self.videoConverter.finishTask.connect(self.finishTask)
        self.videoConverter.describeTask.connect(self.process_show.setText)

        self.imageConverter.getNewTasks.connect(self.progress_show.setMaximum)
        self.imageConverter.setNowTask.connect(self.progress_show.setValue)
        self.imageConverter.finishTask.connect(self.finishTask)
        self.imageConverter.describeTask.connect(self.process_show.setText)

        self.setFixedSize(self.width(), self.height())
        self.setAutoFillBackground(True)
        #window_pale = QtGui.QPalette()
        #window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("images/bg.png")))
        #self.setPalette(window_pale)
        #self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.process_show.setText('正在准备中...')

    def getDefaultPath(self, path):
        if path == '':
            return 'C:/'
        else:
            return path

    def setSrcFileName(self, srcFileName):
        print(type(srcFileName), type(self.srcFileName))
        self.srcFileName = srcFileName
        print(srcFileName,self.srcFileName)
        print(type(srcFileName), type(self.srcFileName))

    def setDstFileName(self, dstFileName):
        self.dstFileName = dstFileName

    def setBlockSize(self, currentIndex):
        self.blockSize = currentIndex + 1

    def setIsColored(self, currentIndex):
        self.isColored = False if(currentIndex == 0) else True

    def selectSrc(self):
        self.process_show.setText('正在准备中...')
        defaultPath = self.getDefaultPath(self.srcFileName)
        srcFileName, _ = QFileDialog.getOpenFileName(self,
                                                     "选取要转换的文件",
                                                     defaultPath,
                                                     ALL_SRC_FILE_TYPE)
        print(srcFileName, type(srcFileName), '中文')
        print(srcFileName.encode('gbk'))
        print(srcFileName.encode('utf-8'))
        #print(chardet.detect(srcFileName))
        if srcFileName:
            self.src_file_name_show.setText(srcFileName)
            dstFileName = os.path.splitext(srcFileName)[0] + '_ascii'+ os.path.splitext(srcFileName)[1]
            self.dst_file_name_show.setText(dstFileName)
            self.progress_show.setMaximum(100)
            self.progress_show.setValue(0)

    def selectDst(self):
        self.process_show.setText('正在准备中...')
        defaultPath = self.getDefaultPath(self.dstFileName)
        if isVideo(self.srcFileName):
            fileType = '视频(*.' + os.path.splitext(self.srcFileName)[1] + ')'
        else:
            if isPicture(self.srcFileName):
                fileType = PICTURE_DST_FILE_TYPE
            else:
                self.process_show.setText('请先选择正确的源文件/路径╮(╯▽╰)╭')
                return
        dstFileName, _ = QFileDialog.getSaveFileName(self,
                                                     "选取目标文件的存储位置",
                                                     defaultPath,
                                                     fileType)
        self.dst_file_name_show.setText(dstFileName)

    def operateSelect(self):
        if(self.convertThread.is_alive()):
            self.videoConverter.cancel()
            self.imageConverter.cancel()
        if self.operate_button.text() == '开始':
            self.operate_button.setText('取消')
            self.convertImage()
        else:
            self.process_show.setText('正在取消中...')
            self.operate_button.setText('开始')

    def finishTask(self):
        self.operate_button.setText('开始')

    def convertImage(self):
        print(self.srcFileName, self.dstFileName, self.blockSize, self.isColored)
        blockShape = (self.blockSize * 2, self.blockSize)
        if isVideo(self.srcFileName):
            self.convertThread = Thread(target=self.videoConverter.fromVideoToAsciiVideo,
                                        args=(self.srcFileName, self.dstFileName, blockShape, self.isColored))
        else:
            if isPicture(self.srcFileName):
                if isPicture(self.dstFileName):
                    self.convertThread = Thread(target = self.imageConverter.fromPictureToPicture,
                                                args=(self.srcFileName, self.dstFileName, blockShape, self.isColored))
                else:
                    if isText(self.dstFileName):
                        self.imageConverter.fromPictureToText(self.srcFileName, self.dstFileName, blockShape, self.isColored)
                        self.progress_show.setValue(100)
                    else:
                        self.process_show.setText('错误的目标文件格式/路径╮(╯▽╰)╭')
                        self.finishTask()
                        return
            else:
                self.process_show.setText('错误的源文件/路径╮(╯▽╰)╭')
                self.finishTask()
                return
        self.convertThread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())