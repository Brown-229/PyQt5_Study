# -*- coding: utf-8 -*-
# @Time : 2021/9/18 14:26
# @Author : liuboliang
# @File : ScreenGeometry
'''
屏幕坐标系
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QHBoxLayout, QWidget, QPushButton

def onClick_Button():
    print("1")
    print("widget.x() = %d"%widget.x())    #窗口横坐标250
    print("widget.y() = %d" % widget.y())   #窗口纵坐标200
    print("widget.width() = %d" % widget.width())  #300 工作区宽度
    print("widget.height() = %d" % widget.height()) #240  工作区高度

    print("2")
    print("widget.geometry().x() = %d" % widget.geometry().x())  #250  工作区横坐标
    print("widget.geometry().y() = %d" % widget.geometry().y())  #231  工作区纵坐标
    print("widget.geometry().width() = %d" % widget.geometry().width()) #300 工作区宽度
    print("widget.geometry().height() = %d" % widget.geometry().height())  #240  工作区高度

    print("3")
    print("widget.frameGeometry().x() = %d" % widget.frameGeometry().x()) #窗口横坐标250
    print("widget.frameGeometry().y() = %d" % widget.frameGeometry().y()) #窗口纵坐标200
    print("widget.frameGeometry().width() = %d" % widget.frameGeometry().width()) #302窗口宽度
    print("widget.frameGeometry().height() = %d" % widget.frameGeometry().height())  #272窗口高度

app = QApplication(sys.argv)

widget = QWidget()
btn = QPushButton(widget)
btn.setText("按钮")
#绑定信号与槽
btn.clicked.connect(onClick_Button)
#按钮位置
btn.move(24,52)
#设置窗口尺寸
widget.resize(300,240)   #设置工作区尺寸
#移动窗口
widget.move(250,200)
widget.setWindowTitle("屏幕坐标系")
widget.show()
sys.exit(app.exec_())


