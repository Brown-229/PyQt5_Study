# -*- coding: utf-8 -*-
# @Time : 2021/9/23 16:14
# @Author : liuboliang
# @File : QLineEditValidator

'''
现在QLineEdit控件的输入（校验器）
如限制只能输入整数、浮点数或满足一定条件的字符串
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys

class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("校验器")
        #创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubuleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow("整数类型",intLineEdit)
        formLayout.addRow("浮点类型",doubuleLineEdit)
        formLayout.addRow("数字和字母",validatorLineEdit)

        intLineEdit.setPlaceholderText("整型")
        doubuleLineEdit.setPlaceholderText("浮点型")
        validatorLineEdit.setPlaceholderText("数字和字母")

        #整数校验器[1,99]
        intValidator = QIntValidator(self)
        intValidator.setRange(1,99)
        #浮点校验器[-360,360],精度是小数点后2位
        doubuleValidator = QDoubleValidator(self)
        doubuleValidator.setRange(-360,360)
        doubuleValidator.setNotation(QDoubleValidator.StandardNotation)
        #设置小数点后2位精度
        doubuleValidator.setDecimals(2)

        #字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')   #创建正则表达式
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置绑定校验器
        intLineEdit.setValidator(intValidator)
        doubuleLineEdit.setValidator(doubuleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())
