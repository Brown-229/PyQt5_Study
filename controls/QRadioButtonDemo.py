# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:39
# @Author : liuboliang
# @File : QRadioButtonDemo
'''
单击按钮控件QRadioButton
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QRadioButton')
        #水平布局
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        #默认第一个按钮处于选中状态
        self.button1.setChecked(True)

        self.button1.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton = self.sender()
        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '>被选中')
        else:
            print('<' + radioButton.text() + '>被取消选中状态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())