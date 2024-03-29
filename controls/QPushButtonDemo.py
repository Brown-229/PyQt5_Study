# -*- coding: utf-8 -*-
# @Time : 2021/9/24 14:14
# @Author : liuboliang
# @File : QPushButtonDemo
'''
按钮控件(QPushButton)
父类QAbstractButton
子类
QPushButton
AToolButton工具条按钮
QRadioButton单选按钮
QCheckBox多选
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QPushButton Demo')
        #垂直布局
        layout = QVBoxLayout()

        self.button1 = QPushButton('第1个按钮')
        self.button1.setText('First Button')
        #设置开关
        self.button1.setCheckable(True)
        self.button1.toggle()
        #传参，使用lambda
        # 多个信号可以绑定到一个槽上
        self.button1.clicked.connect(self.buttonState)
        self.button1.clicked.connect(lambda :self.whichButton(self.button1))

        layout.addWidget(self.button1)
        #在文本前面显示图像
        self.button2 = QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/python.png')))
        self.button2.clicked.connect(lambda :self.whichButton(self.button2))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('不可用的按钮')
        self.button3.setEnabled(True)
        layout.addWidget(self.button3)
       #默认按钮
        self.button4 = QPushButton('&MyButton')
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda :self.whichButton(self.button4))
        layout.addWidget(self.button4)

        self.setLayout(layout)
        self.resize(300,280)

    def whichButton(self,btn):
        print('被单击的按钮是<' + btn.text() + '>')

    def buttonState(self):
        if self.button1.isChecked():
            print('按钮1已经被选中')
        else:
            print('按钮1未被选中')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QPushButtonDemo()
    main.show()
    sys.exit(app.exec_())