# -*- coding: utf-8 -*-
# @Time : 2021/9/10 16:02
# @Author : liuboliang
# @File : run_demo1
'''
表单布局
'''
import sys
from basic import demo_Form_layout
from PyQt5.QtWidgets import QApplication,QMainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWin = QMainWindow()
    ui = demo_Form_layout.Ui_MainWindow()
    ui.setupUi(MainWin)
    MainWin.show()
    sys.exit(app.exec_())
