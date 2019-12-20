from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot, QObject
from PyQt5.QtWidgets import QWidget

from ddl_form import DDLUi


# filename.ui에 대한 클래스 생성법 case1
# 1.uic 모듈의 loadUi('filename.ui') 메소드로 self.ui 객체(ui 컨트롤 클래스)를 생성 및 소유한다.
# 장점: 적은 코드라인으로 ui 생성 가능 및 다수의 ui 소유 가능
# 단점: ui의 부모 클래스(QObject, QWidget, QMainWindow 등)로부터 상속받은 메소드를 오버라이딩(재정의) 불가

class MainUi(QObject):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("coffee_main.ui")
        self.ddl = DDLUi()
        self.ui.btn_ddl.clicked.connect(self.switchDDL)
        self.ddl.mySignal.connect(self.mySlot)
        self.ui.show()

    def switchDDL(self):
        self.ui.hide()
        self.ddl.show()

    # @pyqtSlot 데코레이션: 1.클래스 메소드를 데코레이트 하려면 클래스는 Qt 클래스를 상속 및 super().__init__() 필수
    #                     2.단독 메소드(클래스 외부)는 제약조건 없이 바로 사용 가능
    @pyqtSlot()
    def mySlot(self):
        self.ui.show()
        print("mySlot()")
