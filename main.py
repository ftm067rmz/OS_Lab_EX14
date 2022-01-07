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

        self.ui.message.setText('use only calculator numbers')

        self.num1 = 0
        self.num2 = 0
        self.temp = 0
        self.result = 0
        self.txt = ''
        self.select = ''
        
        self.ui.one.clicked.connect(self.one)
        self.ui.two.clicked.connect(self.two)
        self.ui.three.clicked.connect(self.three)
        self.ui.four.clicked.connect(self.four)
        self.ui.five.clicked.connect(self.five)
        self.ui.six.clicked.connect(self.six)
        self.ui.seven.clicked.connect(self.seven)
        self.ui.eight.clicked.connect(self.eight)
        self.ui.nine.clicked.connect(self.nine)
        self.ui.zero.clicked.connect(self.zero)

        self.ui.sum.clicked.connect(self.add)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.mul.clicked.connect(self.mul)
        self.ui.div.clicked.connect(self.div)
        self.ui.sin.clicked.connect(self.sin)
        self.ui.cos.clicked.connect(self.cos)
        self.ui.tan.clicked.connect(self.tan)
        self.ui.log.clicked.connect(self.log)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.mod.clicked.connect(self.mod)
        self.ui.momayez.clicked.connect(self.momayez)
        self.ui.manfimosbat.clicked.connect(self.manfimosbat)
        self.ui.clear.clicked.connect(self.clear)
        self.ui.equal.clicked.connect(self.equal)

    def one(self):
        self.txt += '1'
        self.ui.entry.setText(self.txt)
        self.temp = int(self.txt)

    def two(self):
        self.txt += '2'
        self.ui.entry.setText(self.txt)
        self.temp = int(self.txt)

    def three(self):
        self.txt += '3'
        self.ui.entry.setText(self.txt)
        self.temp = int(self.txt)

    def four(self):
        self.txt += '4'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)

    def five(self):
        self.txt += '5'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)

    def six(self):
        self.txt += '6'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)

    def seven(self):
        self.txt += '7'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)

    def eight(self):
        self.txt += '8'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)
    
    def nine(self):
        self.txt += '9'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)

    def zero(self):
        self.txt += '0'
        self.ui.entry.setText(self.txt)
        self.temp += int(self.txt)



    def add(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'add'
        
        
    def sub(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'sub'

    def mul(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'mul'
    
    def div(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'div'

    def sin(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'sin'

    def cos(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'cos'

    def tan(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'tan'

    def sqrt(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'sqrt'
    
    def log(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'log'

    def mod(self):
        self.num1 = self.temp
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)
        self.select = 'mod'

    def momayez(self):
        if '.' not in self.txt:
            self.txt += '.'
        self.ui.entry.setText(self.txt)
        self.temp = int(self.txt)

    def manfimosbat(self):
        self.txt = '-' + self.txt
        self.ui.entry.setText(self.txt)
        self.temp = int(self.txt)

    def clear(self):
        self.temp = 0
        self.txt = ''
        self.ui.entry.setText(self.txt)

    def chek(self):
        if self.select == 'add':
            self.num2 = self.temp
            self.result = self.num1 + self.num2
        elif self.select == 'sub':
            self.num2 = self.temp
            self.result = self.num1 - self.num2
        elif self.select == 'mul':
            self.num2 = self.temp
            self.result = self.num1 * self.num2
        elif self.select == 'div':
            self.num2 = self.temp
            if self.num2 == 0:
                self.result = 'Cannot divid by zero'
            else:
                self.result = self.num1 / self.num2
        elif self.select == 'sin':
            self.result = math.sinh(self.num1)
        elif self.select == 'cos':
            self.result = math.cosh(self.num1)
        elif self.select == 'tan':
            self.result = math.tanh(self.num1)
        elif self.select == 'sqrt':
            self.result = math.sqrt(self.num1)
        elif self.select == 'log':
            self.result = math.log(self.num1)
        elif self.select == 'mod':
            self.num2 = self.temp
            self.result = self.num1 % self.num2
        else:
            self.result = 'Please select a correct option'


    def equal(self):
        self.chek()
        self.ui.entry.setText(str(self.result))

if __name__ == "__main__": 
    app = QApplication()
    calculat_main = Calculator()
   
    app.exec()