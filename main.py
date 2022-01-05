import math
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtUiTools import QUiLoader

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load('design.ui')
        self.ui.show()

        self.ui.sum.clicked.connect(self.add)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.log.clicked.connect(self.log)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.percent.clicked.connect(self.percent)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.equal.clicked.connect(self.equal)


    def add(self):
        self.num1 = int(self.ui.entry.text())
        self.ui.entry.setText('')
        self.num2 = int(self.ui.entry.text())
        self.result = self.num1 + self.num2

    def sub(self):
        pass

    def mul(self):
        pass
    
    def div(self):
        pass

    def sin(self):
        pass

    def cos(self):
        pass

    def tan(self):
        pass

    def sqrt(self):
        pass
    
    def log(self):
        pass

    def clear(self):
        pass

    def percent(self):
        pass

    def equal(self):
        # self.num2 = int(self.ui.entry.text())
        # result = self.num1 + self.num2
        self.ui.entry.setText(str(self.result))

if __name__ == "__main__": 
    app = QApplication()
    calculat_main = Calculator()
   
    app.exec()