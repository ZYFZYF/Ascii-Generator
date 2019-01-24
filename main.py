# coding=utf-8
__author__ = 'ZYF'

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from mainWindow import *
import ImageConverter
from PIL import Image

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.src_picture_selector.clicked.connect(self.selectSrcPicture)
        self.dst_picture_selector.clicked.connect(self.selectDstPicture)
        self.dst_txt_selector.clicked.connect(self.selectDstTxt)
        self.end_button.clicked.connect(self.close)
        self.start_button.clicked.connect(self.convertImage)
        for i in range(1, 60):
            self.block_size_selector.addItem('%dpx'%(i))
        self.block_size_selector.setCurrentIndex(4)

    def getDefaultPath(self, path):
        if path == '':
            return 'C:/'
        else:
            return path

    def selectSrcPicture(self):
        defaultPath = self.getDefaultPath(self.src_picture_path_show.text())
        srcPictureFileName, _ = QFileDialog.getOpenFileName(self,
                                                          "选取要转换的图片",
                                                          defaultPath,
                                                          "图片(*.jpg;*.png)")
        print(srcPictureFileName)
        if srcPictureFileName:
            self.src_picture_path_show.setText(srcPictureFileName)
            srcPicture = srcPictureFileName.split('.')[0]
            self.dst_picture_path_show.setText(srcPicture + '_ascii.jpg')
            self.dst_txt_path_show.setText(srcPicture + '_ascii.txt')

    def selectDstPicture(self):
        defaultPath = self.getDefaultPath(self.dst_picture_path_show.text())
        dstPictureFilaName, _ = QFileDialog.getSaveFileName(self,
                                                          "选取要保存的路径",
                                                          defaultPath,
                                                          "图片(*.jpg;*.png)")
        if dstPictureFilaName:
            self.dst_picture_path_show.setText(dstPictureFilaName)

    def selectDstTxt(self):
        defaultPath = self.getDefaultPath(self.dst_txt_path_show.text())
        dstTxtFilaName, _ = QFileDialog.getSaveFileName(self,
                                                      "选取要保存的路径",
                                                      defaultPath,
                                                      "文本文件(*.txt)")
        if dstTxtFilaName:
            self.dst_txt_path_show.setText(dstTxtFilaName)

    def convertImage(self):
        if self.picture_selected.isChecked():
            src = self.src_picture_path_show.text()
            dst = self.dst_picture_path_show.text()
            srcImage = Image.open(src)
            blockSize = self.block_size_selector.currentIndex() + 1
            blockSizeComp = (blockSize * 2, blockSize)
            ImageConverter.fromImageToAsciiImage(srcImage, blockSizeComp).save(dst)
        else:
            src = self.src_picture_path_show.text()
            dst = self.dst_txt_path_show.text()
            srcImage = Image.open(src)
            file = open(dst, 'w')
            blockSize = self.block_size_selector.currentIndex() + 1
            blockSizeComp = (blockSize * 2, blockSize)
            file.write(ImageConverter.fromImageToAsciiArray(srcImage,blockSizeComp))
            file.close()
        reply = QMessageBox.information(self, '标题', '转换成功！请自行查看←_←', QMessageBox.Yes)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())