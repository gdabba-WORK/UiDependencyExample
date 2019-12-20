# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ddl_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget


# filename.ui에 대한 클래스 생성법 case2
# 1. uic.loadUi()를 사용하지 않고, PyUIC5(external tool)로 해당 ui에 대한 .py 파일(클래스)을 생성
# 2. QWidget or QMainWindow를 상속하고, 클래스의 __init__()에서 기존에 생성 된 함수들(setupUi(), retranslateUi())로 자신(self)을 초기화한다.
# 3. 클래스 자신이 ui 컨트롤 클래스이다.
# case1의 장점 및 단점과 반대되는 장단점을 가진다.
class DDLUi(QWidget):
    # custom signal 선언. 시그널에서 인자를 전달하려면 pyqtSignal(<parameter1 type>, <parameter2 type>, ...) 형태로 생성
    mySignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    # closeEvent()을 오버라이딩하여 내부에서 custom signal(mySignal)을 발생
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.mySignal.emit()
        super().closeEvent(a0)

    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(532, 295)
        self.splitter = QtWidgets.QSplitter(widget)
        self.splitter.setGeometry(QtCore.QRect(50, 30, 401, 101))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_create = QtWidgets.QPushButton(self.splitter)
        self.btn_create.setObjectName("btn_create")
        self.btn_backup = QtWidgets.QPushButton(self.splitter)
        self.btn_backup.setObjectName("btn_backup")
        self.btn_restore = QtWidgets.QPushButton(self.splitter)
        self.btn_restore.setObjectName("btn_restore")
        self.btn_close = QtWidgets.QPushButton(widget)
        self.btn_close.setGeometry(QtCore.QRect(200, 190, 80, 23))
        self.btn_close.setObjectName("btn_close")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "DDL Application"))
        self.btn_create.setText(_translate("widget", "Create"))
        self.btn_backup.setText(_translate("widget", "Backup"))
        self.btn_restore.setText(_translate("widget", "Restore"))
        self.btn_close.setText(_translate("widget", "close"))
