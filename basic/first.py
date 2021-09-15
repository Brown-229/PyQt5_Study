# -*- coding: utf-8 -*-
# @Time : 2021/9/10 11:46
# @Author : liuboliang
# @File : first

import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    #创建QApplication类的实例
    app = QApplication(sys.argv)
    #创建一个窗口
    w = QWidget()
    #设置窗口尺寸
    w.resize(400,200)
    #移动窗口(窗口在屏幕的位置)
    w.move(500,300)
    #设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    #显示窗口
    w.show()
    #进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())


''''
使用命令：python -m PyQt5.uic.pyuic demo_Horizontal.ui -o demo1.py将ui文件转换为.py文件
'''