# -*- coding: utf-8 -*-
# @Time : 2021/9/17 15:27
# @Author : liuboliang
# @File : CenterForm

'''
让显示的窗口居中，使用QDesktopWidget
'''

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QDesktopWidget
from PyQt5.QtGui import QIcon


class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm,self).__init__()

        #设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        #设置窗口尺寸
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)
    def center(self):
        #获取屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2
        self.move(newLeft,newTop)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = CenterForm()
    main.show()
    sys.exit(app.exec_())