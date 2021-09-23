# -*- coding: utf-8 -*-
# @Time : 2021/9/23 14:39
# @Author : liuboliang
# @File : QLabelBuddy
'''
Qlabel与伙伴控制
mainlayout.addWidget(控件对象，rowIndex,columeIndex,row,colume)
'''
from PyQt5.QtWidgets import *
import sys


class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控制')
        #热键
        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        pwdLabel = QLabel('&Password', self)
        pwdLineEdit = QLineEdit(self)
        # 设置伙伴控件
        pwdLabel.setBuddy(pwdLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)
        mainLayout.addWidget(nameLabel,0,0)
        mainLayout.addWidget(nameLineEdit,0,1,1,2)

        mainLayout.addWidget(pwdLabel,1,0)
        mainLayout.addWidget(pwdLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())