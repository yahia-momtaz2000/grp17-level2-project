# install package PyQt5-Qt5
# import QtGui module from PyQt5 package
from PyQt5 import QtGui

# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox
import sys


class FirstWindow(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()
        # initializers for the window
        self.setWindowTitle('This is My First Window')
        self.setGeometry(100, 100, 800, 500)  # X    Y    Width      Height

        # create Name Label
        self.label_name = QLabel('Name', self)
        self.label_name.move(20, 80)  # x y from window frame

        # create Name LineEdit
        self.line_edit_name = QLineEdit(self)
        self.line_edit_name.move(60, 80)  # X Y
        self.line_edit_name.resize(250, 30)  # W H

        # create push button
        self.button_name = QPushButton('Read the field', self)
        self.button_name.move(70, 120)  # X Y
        self.button_name.resize(210, 30)  # W H
        self.button_name.clicked.connect(self.read_name_func)


        # ----------------------------------------
        # Create Food Label
        self.label_food = QLabel('Choose Food', self)
        self.label_food.move(380, 80)  # X Y

        # Create Combobox
        self.combo_food = QComboBox(self)
        self.combo_food.move(480, 80)  # X Y
        self.combo_food.resize(200, 30)  # W H
        # add items to combo_food
        self.combo_food.addItem('Koshary', 10)
        self.combo_food.addItem('Chicken', 20)
        self.combo_food.addItem('Rice', 30)
        self.combo_food.addItem('Fruit', 40)

        # Create Food button
        self.food_button = QPushButton('Read Chosen Food', self)
        self.food_button.move(500, 120) #  X Y
        self.food_button.resize(160, 30) # W H
        self.food_button.clicked.connect(self.read_food_func)

        self.show()  # Show the window

    def read_name_func(self):
        v_name = self.line_edit_name.text() # read [ get ]
        print('ًWelcome '+v_name)
        QMessageBox.question(self, 'opening ...', 'Welcome '+v_name, QMessageBox.Ok, QMessageBox.Ok)

    def read_food_func(self):
        v_food = self.combo_food.currentText()
        QMessageBox.question(self, 'opening ...', 'You Chose ' + v_food, QMessageBox.Ok, QMessageBox.Ok)


# main program
app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
first_window_object = FirstWindow()
sys.exit(app_object.exec())  # exit screen only when user take action

