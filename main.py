import sys
import os
import csv

from PyQt6.QtWidgets import (QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QApplication)
from PyQt6.QtCore import Qt

# Constants
filepath = 'Data\Total DNC 1.9.24.csv'
contacted_file_path = 'Data\Contacted.csv'

class MainWindow(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.initUI()

    def initUI(self):

        # Default Values
        self.prospect = "Prospect #"
        self.firstname = "First Name"
        self.lastname = "Last Name"
        self.address = "Address"
        self.city = "City"
        self.state = "State"
        self.zipcode = "Zipcode"
        self.phone = "Phone"
        self.productid = "Product"

        # Static labels
        prosp = QLabel(self.prospect)
        fname = QLabel(self.firstname)
        lname = QLabel(self.lastname)
        address = QLabel(self.address)
        city = QLabel(self.city)
        state = QLabel(self.state)
        zipcode = QLabel(self.zipcode)
        product = QLabel(self.zipcode)
        phone = QLabel(self.phone)

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

    def update_ui(self, entry):
        self.prospect = entry['custnumber']
        self.firstname = entry['firstname']
        self.lastname = entry['lastname']
        self.address = entry['Address1']
        self.city = entry['City']
        self.state = entry['State']
        self.zipcode = entry['Zip']
        self.phone = entry['Phone']
        self.productid = entry['productid']

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def mark_contacted(data, entry_id):
    for entry in data:
        if entry['id'] == entry_id:
            entry['contacted'] = True
            break

def write_csv(file_path, data):
    fieldnames = data[0].keys()
    with open(file_path, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def create_contacted_csv(data, contacted_file_path):
    contacted_data = [entry for entry in data if entry.get('contacted')]
    write_csv(contacted_file_path), contacted_data

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    
    # Get csv
    data = read_csv(filepath)
    for entry in data:
        window.update_ui(entry)
    
    # Input LP login credentials

    # Load next contact
    # Navigate to LP profile for contact
    # Generate new call and tag
    
    # After clicking get next, save previous result as contacted and fetch

    
    
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
