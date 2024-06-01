# import QtGui module from PyQt5 package
from PyQt5 import QtGui, uic

# from QtWidgets found in package PyQt5 import classes QApplication - QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox, QComboBox, \
    QRadioButton, QCheckBox, QTextEdit
import sys

class WidgetsWin(QMainWindow):  # inheritance FirstWindow class inherit from QMainWindow class
    def __init__(self):
        super().__init__()

        # Load ui File
        uic.loadUi('widgets_win_01.ui', self)

        # ---------------------------------- Welcome Frame ----------------------
        # Define Widgets
        self.line_edit_username = self.findChild(QLineEdit, 'line_edit_username')
        self.push_button_hi = self.findChild(QPushButton, 'push_button_hi')
        self.push_button_reset = self.findChild(QPushButton, 'push_button_reset')

        # Define Operations
        self.push_button_hi.clicked.connect(self.welcome_user)
        self.push_button_reset.clicked.connect(self.reset_user)


        # ---------------------------------- Nationality Frame ----------------------
        # Define Widgets
        self.radio_button_eg = self.findChild(QRadioButton, 'radio_button_eg')
        self.radio_button_tn = self.findChild(QRadioButton, 'radio_button_tn')
        self.radio_button_irq = self.findChild(QRadioButton, 'radio_button_irq')
        self.push_button_nationality = self.findChild(QPushButton, 'push_button_nationality')
        self.label_nationality = self.findChild(QLabel, 'label_nationality')

        # Define Operation
        self.radio_button_eg.clicked.connect(self.radio_eg_clicked)
        self.radio_button_tn.clicked.connect(self.radio_tn_clicked)
        self.radio_button_irq.clicked.connect(self.radio_irq_clicked)
        self.push_button_nationality.clicked.connect(self.read_nationality)


        # ---------------------------------- Food Frame ----------------------
        # Define Widgets
        self.check_box_koshari = self.findChild(QCheckBox, 'check_box_koshari')
        self.check_box_pizza = self.findChild(QCheckBox, 'check_box_pizza')
        self.check_box_chicken = self.findChild(QCheckBox, 'check_box_chicken')
        self.text_edit_food = self.findChild(QTextEdit, 'text_edit_food')
        self.push_button_food = self.findChild(QPushButton, 'push_button_food')

        # Define Operations
        self.check_box_koshari.clicked.connect(self.koshari_clicked)
        self.check_box_pizza.clicked.connect(self.pizza_clicked)
        self.check_box_chicken.clicked.connect(self.chicken_clicked)
        self.push_button_food.clicked.connect(self.read_chosen_food)

        # ---------------------------------- Products Frame ----------------------
        # Define Widgets
        self.combo_box_products = self.findChild(QComboBox, 'combo_box_products')
        self.label_products = self.findChild(QLabel, 'label_products')
        self.push_button_products = self.findChild(QPushButton, 'push_button_products')

        # define Operations
        self.push_button_products.clicked.connect(self.read_chosen_product)
        self.combo_box_products.activated.connect(self.choose_combo_food)



        # Show window
        self.show()

    # ---------------------------------- Welcome Frame ----------------------
    def welcome_user(self):
        user_name = self.line_edit_username.text()
        QMessageBox.question(self, 'welcome ... ', f'Hi {user_name}', QMessageBox.Ok, QMessageBox.Ok)

    def reset_user(self):
        self.line_edit_username.setText('')

    # ---------------------------------- Nationality Frame ----------------------
    def radio_eg_clicked(self):
        self.label_nationality.setText('Iam Egyptian')

    def radio_tn_clicked(self):
        self.label_nationality.setText('Iam Tunisian')

    def radio_irq_clicked(self):
        self.label_nationality.setText('Iam Iraqian')

    def read_nationality(self):
        if self.radio_button_eg.isChecked():
            QMessageBox.question(self, 'Nationality ... ', f'Iam Egyptian', QMessageBox.Ok, QMessageBox.Ok)
        elif self.radio_button_tn.isChecked():
            QMessageBox.question(self, 'Nationality ... ', f'Iam Tunisian', QMessageBox.Ok, QMessageBox.Ok)
        else:
            QMessageBox.question(self, 'Nationality ... ', f'Iam Iraqian', QMessageBox.Ok, QMessageBox.Ok)

# ---------------------------------- Food Frame ----------------------
    def koshari_clicked(self):
        print('Koshari checkbox Clicked')

    def pizza_clicked(self):
        print('pizza checkbox Clicked')

    def chicken_clicked(self):
        print('chicken checkbox Clicked')

    def read_chosen_food(self):
        if self.check_box_koshari.isChecked():
            self.koshari = 'Koshari'
        else:
            self.koshari = ''

        if self.check_box_pizza.isChecked():
            self.pizza = 'Pizza'
        else:
            self.pizza = ''

        if self.check_box_chicken.isChecked():
            self.chicken = 'Chicken'
        else:
            self.chicken = ''

        self.text_edit_food.setText(f'You Choose {self.koshari} {self.pizza} {self.chicken}')

    # ---------------------------------- Products Frame ----------------------
    def read_chosen_product(self): # button
        v_product_chosen = self.combo_box_products.currentText()
        QMessageBox.question(self, 'products.. ', f'You Choose {v_product_chosen}', QMessageBox.Ok, QMessageBox.Ok)

    def choose_combo_food(self): # combo box
        v_product_chosen = self.combo_box_products.currentText()
        self.label_products.setText(f'You Choose {v_product_chosen}')

# main program
app_object = QApplication(sys.argv) # sys.argv : list of parameters used when open window from terminal [ not often ]
widgets_window_object = WidgetsWin()
sys.exit(app_object.exec())  # exit screen only when user take action