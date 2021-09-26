# -*- coding: utf-8 -*-
# @Time : 2021/9/26 14:13
# @Author : liuboliang
# @File : QFontDialog
'''
字体对话框 QFontDialog
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QFontDialog案例')

        layout = QVBoxLayout()
        self.fontButton = QPushButton('选择字体')
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)

        self.fontlabel = QLabel('Hello，测试字体例子')
        layout.addWidget(self.fontlabel)

        self.setLayout(layout)

    def getFont(self):
        font,ok = QFontDialog.getFont()
        if ok:
            self.fontlabel.setFont(font)










if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QFontDialogDemo()
    main.show()
    sys.exit(app.exec_())