# -*- coding: utf-8 -*-
# @Time : 2021/9/24 16:37
# @Author : liuboliang
# @File : QComboBoxDemo
'''
下拉列表控件  QComboBox
1、如何将列表项添加到QComboBox控件中
2、如何获取选项中的列表项
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QComboBoxDemo(QWidget):
    def __init__(self):
        super(QComboBoxDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('下拉列表控件演示')
        self.resize(300,100)
        #垂直分布
        layout = QVBoxLayout()
        self.label = QLabel('请选择编程语言')

        self.cb = QComboBox()
        self.cb.addItem('Python')
        self.cb.addItem('C++')
        self.cb.addItems(['Java','C#','Ruby'])

        self.cb.currentIndexChanged.connect(self.selectionChange)

        layout.addWidget(self.label)
        layout.addWidget(self.cb)

        self.setLayout(layout)


    def selectionChange(self,i):
        #获得当前选择的文本
        self.label.setText(self.cb.currentText())
        #调整控件尺寸
        self.label.adjustSize()

        for count in range(self.cb.count()):
            print('item' + str(count) + '=' + self.cb.itemText(count))
        print('current index',i,'selection changed',self.cb.currentText())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QComboBoxDemo()
    main.show()
    sys.exit(app.exec_())