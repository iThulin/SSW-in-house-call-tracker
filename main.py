import sys
import os

from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QApplication)
from PyQt6.QtCore import Qt

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):

        # Static labels
        prosp = QLabel("Prospect #:")
        fname = QLabel("First Name:")
        lname = QLabel("Last Name:")
        address = QLabel("Address:")
        city = QLabel("City:")
        state = QLabel("State:")
        zipcode = QLabel("Zip Code:")
        product = QLabel("Product:")
        phone = QLabel("Phone #:")

        # Dynamic labels
        prosp_info = QLabel("Prospect")
        fname_info = QLabel("First name")
        lname_info = QLabel("Last name")
        address_info = QLabel("Address")
        city_info = QLabel("City")
        state_info = QLabel("State")
        zipcode_info = QLabel("Zip code")
        product_info = QLabel("Product")
        phone_info = QLabel("Phone")

        # Buttons
        next_button = QPushButton("Get next contact")

        # Init grid
        grid = QGridLayout()
        grid.setSpacing(15)

        # Build Column 1
        grid.addWidget(prosp, 1, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(fname, 2, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(lname, 3, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(address, 4, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(city, 5, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(state, 6, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(zipcode, 7, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(product, 8, 0, alignment=Qt.AlignmentFlag.AlignRight)
        grid.addWidget(phone, 9, 0, alignment=Qt.AlignmentFlag.AlignRight)

        # Build Column 2
        grid.addWidget(prosp_info, 1, 1)
        grid.addWidget(fname_info, 2, 1)
        grid.addWidget(lname_info, 3, 1)
        grid.addWidget(address_info, 4, 1)
        grid.addWidget(city_info, 5, 1)
        grid.addWidget(state_info, 6, 1)
        grid.addWidget(zipcode_info, 7, 1)
        grid.addWidget(product_info, 8, 1)
        grid.addWidget(phone_info, 9, 1)
        grid.addWidget(next_button, 10, 1)

        # Adjust grid layout parameters
        grid.setColumnMinimumWidth(1, prosp.sizeHint().width())
        grid.setColumnStretch(2, 1)
        self.setLayout(grid)

        # Adjust window parameters
        self.resize(400, 300)
        self.setWindowTitle("SSW Call Tracking")
        self.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
