# -*- coding: utf-8 -*-
# @Time : 2021/9/10 16:02
# @Author : liuboliang
# @File : run_demo1
'''
修改TAB顺序
'''
import sys
from basic import demo_TAB
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = QMainWindow()
    ui = demo_TAB.Ui_MainWindow()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())
