# -*- coding: utf-8 -*-
# @Time : 2021/9/17 14:17
# @Author : liuboliang
# @File : FirstMainWin

import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()

        #设置主窗口标题
        self.setWindowTitle('第一个主窗口应用')
        #设置窗口尺寸
        self.resize(400,300)
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('./images/Dragon.ico'))
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())