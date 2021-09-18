# -*- coding: utf-8 -*-
# @Time : 2021/9/18 16:03
# @Author : liuboliang
# @File : Tooltip
#显示控件提示信息


import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton,QToolTip
from PyQt5.QtGui import QFont
class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #设置字体
        QToolTip.setFont(QFont('SansSerif',12))

        self.setToolTip('今天是<b>星期五</b>')
        #设置窗口尺寸
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮')
        #将信号与槽关联
        self.button1.setToolTip('这是一个按钮，Are you OK?')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()
    sys.exit(app.exec_())
