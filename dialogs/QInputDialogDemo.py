# -*- coding: utf-8 -*-
# @Time : 2021/9/26 13:45
# @Author : liuboliang
# @File : QInputDialogDemo
'''
输入对话框 QinputDialog

QInputDialog.getItem----显示输入列表
QInputDialog.getText----普通文本
QInputDialog.getInt----整数
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QInputDialog案例')
        #创建表单布局
        layout = QFormLayout()
        self.button1 = QPushButton('获取列表中的选项')
        self.button1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(self.button1,self.lineEdit1)

        self.button2 = QPushButton('获取字符串')
        self.button2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(self.button2, self.lineEdit2)

        self.button3 = QPushButton('获取整数')
        self.button3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(self.button3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = ('C','C++','Ruby','Python','Java')
        item,ok = QInputDialog.getItem(self,'请选择编程语言','语言列表',items)
        if ok and item:
            self.lineEdit1.setText(item)

    def getText(self):
        text,ok = QInputDialog.getText(self,'文本输入框','输入姓名')
        if ok and text:
            self.lineEdit2.setText(text)

    def getInt(self):
        num,ok = QInputDialog.getInt(self,'整数输入框','输入数字')
        if ok and num:
            self.lineEdit3.setText(str(num))









if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QInputDialogDemo()
    main.show()
    sys.exit(app.exec_())