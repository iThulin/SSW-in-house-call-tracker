import sys
import csv

from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QGridLayout, QApplication)
from PyQt6.QtCore import Qt

# Constants
filepath = 'Data\Total DNC 1.9.24.csv'
contacted_file_path = 'Data\Contacted.csv'

class MainWindow(QWidget):

    def __init__(self, data, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.current_account_index = 0
        self.account_list = data
        self.contacted = []

        self.initUI()

    def initUI(self):

        # Static labels
        prosp = QLabel("Prospect #:")
        fname = QLabel("First name:")
        lname = QLabel("Last name:")
        address = QLabel("Address:")
        city = QLabel("City:")
        state = QLabel("State:")
        zipcode = QLabel("Zip code:")
        product = QLabel("Product:")
        phone = QLabel("Phone:")

        # Dynamic labels
        self.prospect_info = QLabel(self.account_list[self.current_account_index]['custnumber'])
        self.firstname_info = QLabel(self.account_list[self.current_account_index]['firstname'])
        self.lastname_info = QLabel(self.account_list[self.current_account_index]['lastname'])
        self.address_info = QLabel(self.account_list[self.current_account_index]['Address1'])
        self.city_info = QLabel(self.account_list[self.current_account_index]['City'])
        self.state_info = QLabel(self.account_list[self.current_account_index]['State'])
        self.zipcode_info = QLabel(self.account_list[self.current_account_index]['Zip'])
        self.phone_info = QLabel(self.account_list[self.current_account_index]['Phone'])
        self.productid_info = QLabel(self.account_list[self.current_account_index]['productid'])

        # Buttons
        next_button = QPushButton("Next Account")
        next_button.setCheckable(True)
        next_button.clicked.connect(self.next_button_clicked)

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
        grid.addWidget(next_button, 10, 0)

        # Build Column 2
        grid.addWidget(self.prospect_info, 1, 1)
        grid.addWidget(self.firstname_info, 2, 1)
        grid.addWidget(self.lastname_info, 3, 1)
        grid.addWidget(self.address_info, 4, 1)
        grid.addWidget(self.city_info, 5, 1)
        grid.addWidget(self.state_info, 6, 1)
        grid.addWidget(self.zipcode_info, 7, 1)
        grid.addWidget(self.productid_info, 8, 1)
        grid.addWidget(self.phone_info, 9, 1)
        

        # Adjust grid layout parameters
        grid.setColumnMinimumWidth(1, prosp.sizeHint().width())
        grid.setColumnStretch(2, 1)
        self.setLayout(grid)

        # Adjust window parameters
        self.resize(200, 250)
        self.setWindowTitle("SSW Call Tracking")
        self.show()            

    def switch_account(self):
        # increment index to switch to next account

        # Update the tags on all label elements
        self.prospect_info.setText(self.account_list[self.current_account_index]['custnumber'])
        self.firstname_info.setText(self.account_list[self.current_account_index]['firstname'])
        self.lastname_info.setText(self.account_list[self.current_account_index]['lastname'])
        self.address_info.setText(self.account_list[self.current_account_index]['Address1'])
        self.city_info.setText(self.account_list[self.current_account_index]['City'])
        self.state_info.setText(self.account_list[self.current_account_index]['State'])
        self.zipcode_info.setText(self.account_list[self.current_account_index]['Zip'])
        self.phone_info.setText(self.account_list[self.current_account_index]['Phone'])
        self.productid_info.setText(self.account_list[self.current_account_index]['productid'])

    def mark_contact(self):
        self.account_list[self.current_account_index]['contacted'] = True
        self.contacted = self.account_list[self.current_account_index]
        self.account_list.pop(self.current_account_index)
    
    def next_button_clicked(self):
        self.mark_contact()
        self.save_data()
        self.save_contacted()
        self.switch_account()

    def save_data(self):
        existing_raw_data = []
        try:
            with open(filepath, 'r') as old_raw_file:
                reader = csv.DictReader(old_raw_file)
                existing_raw_data = list(reader)
        except FileNotFoundError:
            pass

        existing_raw_data = self.account_list

        with open(filepath, 'w', newline='') as new_raw_file:
            fieldnames = existing_raw_data[0].keys() if existing_raw_data else self.data.keys()
            writer = csv.DictWriter(new_raw_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(existing_raw_data)

    def save_contacted(self):
        existing_contacted_data = []
        try:
            with open(contacted_file_path, 'r') as old_contacted_file:
                reader = csv.DictReader(old_contacted_file)
                existing_contacted_data = list(reader)
        except FileNotFoundError:
            pass

        existing_contacted_data.append(self.contacted)

        with open(contacted_file_path, 'w', newline='') as new_contacted_file:
            fieldnames = existing_contacted_data[0].keys() if existing_contacted_data else self.data.keys()
            writer = csv.DictWriter(new_contacted_file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(existing_contacted_data)

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def main():
    app = QApplication(sys.argv)
    data = read_csv(filepath)
    window = MainWindow(data)
    window.show()

    sys.exit(app.exec())

if __name__ == '__main__':
    main()
