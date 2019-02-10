# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(976, 460)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("QMainWindow{background-image:url(images/bg.png)}")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 871, 379))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.src_file_name_show = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.src_file_name_show.setEnabled(True)
        self.src_file_name_show.setStyleSheet("QLineEdit{\n"
"                border:1px solid gray;\n"
"                width:300px;\n"
"                border-radius:10px;\n"
"                padding:2px 4px;\n"
"            }")
        self.src_file_name_show.setReadOnly(True)
        self.src_file_name_show.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.src_file_name_show.setObjectName("src_file_name_show")
        self.horizontalLayout_3.addWidget(self.src_file_name_show)
        self.src_selector = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.src_selector.setStyleSheet("QToolButton{background:white}")
        self.src_selector.setObjectName("src_selector")
        self.horizontalLayout_3.addWidget(self.src_selector)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.block_size_selector = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.block_size_selector.setStyleSheet("QComboBox{background:white}")
        self.block_size_selector.setEditable(False)
        self.block_size_selector.setObjectName("block_size_selector")
        self.horizontalLayout_4.addWidget(self.block_size_selector)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.color_selector = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.color_selector.setStyleSheet("QComboBox{background:white}")
        self.color_selector.setObjectName("color_selector")
        self.horizontalLayout_4.addWidget(self.color_selector)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dst_file_name_show = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.dst_file_name_show.setStyleSheet("QLineEdit{\n"
"                border:1px solid gray;\n"
"                width:300px;\n"
"                border-radius:10px;\n"
"                padding:2px 4px;\n"
"            }")
        self.dst_file_name_show.setObjectName("dst_file_name_show")
        self.horizontalLayout.addWidget(self.dst_file_name_show)
        self.dst_selector = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.dst_selector.setStyleSheet("QToolButton{background:white}")
        self.dst_selector.setObjectName("dst_selector")
        self.horizontalLayout.addWidget(self.dst_selector)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.progress_show = QtWidgets.QProgressBar(self.verticalLayoutWidget)
        self.progress_show.setStyleSheet("QProgressBar{background:white}")
        self.progress_show.setProperty("value", 0)
        self.progress_show.setInvertedAppearance(False)
        self.progress_show.setObjectName("progress_show")
        self.horizontalLayout_2.addWidget(self.progress_show)
        self.operate_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.operate_button.setStyleSheet("QPushButton{background:white}")
        self.operate_button.setObjectName("operate_button")
        self.horizontalLayout_2.addWidget(self.operate_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.process_show = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.process_show.setText("")
        self.process_show.setAlignment(QtCore.Qt.AlignCenter)
        self.process_show.setObjectName("process_show")
        self.verticalLayout.addWidget(self.process_show)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 976, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AsciiConverter"))
        self.label.setText(_translate("MainWindow", " 源文件 "))
        self.src_selector.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "单个字符大小"))
        self.label_4.setText(_translate("MainWindow", "输出颜色"))
        self.label_2.setText(_translate("MainWindow", "目标文件"))
        self.dst_selector.setText(_translate("MainWindow", "..."))
        self.operate_button.setText(_translate("MainWindow", "开始"))
        self.label_5.setText(_translate("MainWindow", "   _作者：一行超人 如有使用上的问题或建议请联系QQ：973446154"))
