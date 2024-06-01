# import QtGui module from PyQt5 package
from PyQt5 import uic

# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

class CalculatorWin(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()

        # Load ui File
        uic.loadUi('calculator_win_02.ui', self)

        # ---------------------------------------------------------------
        # Define Widgets
        self.label_screen = self.findChild(QLabel, 'label_screen')
        self.button_1 = self.findChild(QPushButton, 'button_1')
        self.button_2 = self.findChild(QPushButton, 'button_2')
        self.button_3 = self.findChild(QPushButton, 'button_3')
        self.button_4 = self.findChild(QPushButton, 'button_4')
        self.button_5 = self.findChild(QPushButton, 'button_5')
        self.button_6 = self.findChild(QPushButton, 'button_6')
        self.button_7 = self.findChild(QPushButton, 'button_7')
        self.button_8 = self.findChild(QPushButton, 'button_8')
        self.button_9 = self.findChild(QPushButton, 'button_9')
        self.button_0 = self.findChild(QPushButton, 'button_0')
        self.button_plus = self.findChild(QPushButton, 'button_plus')
        self.button_minus = self.findChild(QPushButton, 'button_minus')
        self.button_multiply = self.findChild(QPushButton, 'button_multiply')
        self.button_divide = self.findChild(QPushButton, 'button_divide')
        self.button_eq = self.findChild(QPushButton, 'button_eq')
        self.button_dot = self.findChild(QPushButton, 'button_dot')
        self.button_backspace = self.findChild(QPushButton, 'button_backspace')
        self.button_reset = self.findChild(QPushButton, 'button_reset')
        self.button_square = self.findChild(QPushButton, 'button_square')
        self.button_chg_sign = self.findChild(QPushButton, 'button_chg_sign')

        # Define Operations
        self.button_1.clicked.connect(lambda: self.button_chosen('1'))
        self.button_2.clicked.connect(lambda: self.button_chosen('2'))
        self.button_3.clicked.connect(lambda: self.button_chosen('3'))
        self.button_4.clicked.connect(lambda: self.button_chosen('4'))
        self.button_5.clicked.connect(lambda: self.button_chosen('5'))
        self.button_6.clicked.connect(lambda: self.button_chosen('6'))
        self.button_7.clicked.connect(lambda: self.button_chosen('7'))
        self.button_8.clicked.connect(lambda: self.button_chosen('8'))
        self.button_9.clicked.connect(lambda: self.button_chosen('9'))
        self.button_0.clicked.connect(lambda: self.button_chosen('0'))
        self.button_plus.clicked.connect(lambda: self.button_chosen('+'))
        self.button_minus.clicked.connect(lambda: self.button_chosen('-'))
        self.button_multiply.clicked.connect(lambda: self.button_chosen('*'))
        self.button_divide.clicked.connect(lambda: self.button_chosen('/'))
        self.button_reset.clicked.connect(lambda: self.button_chosen('C'))

        self.button_eq.clicked.connect(lambda: self.equal_solution())


        # Show window
        self.show()
    # ---------------------------------------------------
    def button_chosen(self, key_value):
        if key_value == 'C':
            self.label_screen.setText('0')
            return

        current_screen = self.label_screen.text()
        if current_screen == '0':
            self.label_screen.setText(f'{key_value}')
        else:
            self.label_screen.setText( f'{current_screen}{key_value}'  )

    def equal_solution(self):
        current_screen = self.label_screen.text()
        result = eval(current_screen)
        self.label_screen.setText( str(result) ) # casting : convert to string

    def square_result(self):
        pass

    def change_sign(self):
        pass

    def backspace(self):
        pass

    def press_dot(self):
        pass

# main program
app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
calculator_window_object = CalculatorWin()
sys.exit(app_object.exec())  # exit screen only when user take action