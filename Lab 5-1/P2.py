from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QLabel, QDateEdit, QButtonGroup,
                             QRadioButton, QComboBox, QTextEdit, QCheckBox)

from PySide6.QtCore import QDate, Qt
import sys

class StudentRegistrationForm (QWidget):
    def __init__(self):
        super().__init__()

        #self.setWindowTitle("Student Registration")
        #self.setFixedSize(400, 600)

        main_layout = QVBoxLayout()
        botton_layout = QHBoxLayout()

        ########################### Line box ##############################

        title = QLabel("Student Registration Form")
        title.setStyleSheet("font-size: 18px; font-weight: bold;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)
    
        main_layout.addWidget(QLabel("Full name:"))
        self.name_input = QLineEdit()
        main_layout.addWidget(self.name_input)

        main_layout.addWidget(QLabel("Email:"))
        self.email_input = QLineEdit()
        main_layout.addWidget(self.email_input)

        main_layout.addWidget(QLabel("Phone:"))
        self.phone_input = QLineEdit()
        main_layout.addWidget(self.phone_input)

        ################################ Date edit ######################################
        
        main_layout.addWidget(QLabel("Date of Birth (dd/MM/yyyy):   "))
        self.date_edit = QDateEdit()
        self.date_edit.setCalendarPopup(True)  # Shows calendar dropdown
        self.date_edit.setDisplayFormat("dd/MM/yyyy")  # Format like "2/19/00"
        self.date_edit.setDate(QDate(2000, 1, 1))  # Set default date 
        self.date_edit.setFixedWidth(200)
        main_layout.addWidget(self.date_edit)

        ############################# Radio box #########################################

        main_layout.addWidget(QLabel("Gender:"))
        gender_layout = QHBoxLayout()

        self.gender_group = QButtonGroup()
        
        self.male_radio = QRadioButton("Male")
        self.female_radio = QRadioButton("Female")
        self.non_radio = QRadioButton("Non-binary")
        self.perfer_radio = QRadioButton("Perfer not to say")

        self.gender_group.addButton(self.male_radio)
        self.gender_group.addButton(self.female_radio)
        self.gender_group.addButton(self.non_radio)
        self.gender_group.addButton(self.perfer_radio)

        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)
        gender_layout.addWidget(self.non_radio)
        gender_layout.addWidget(self.perfer_radio)

        main_layout.addLayout(gender_layout)

        ############################# Combo box #########################################

        main_layout.addWidget(QLabel("Program:"))
        self.program = QComboBox()
        self.program.setPlaceholderText("Select your program")
        self.program.addItems([
            "Computer Engineering",
            "Digital Media Engineering",
            "Environmental Engineering",
            "Electical Engineering",
            "Semiconductor Engineering",
            "Mechanical Engineering",
            "Industrial Engineering",
            "Logistic Engineering",
            "Power Engineering",
            "Electronic Engineering",
            "Telecommunication Engineering",
            "Agricultural Engineering",
            "Civil Engineering",
            "ARIS"
        ])

        main_layout.addWidget(self.program)

        ############################# Text edit #########################################
        
        main_layout.addWidget(QLabel("Tell us a little bit about yourself:"))
        self.about = QTextEdit()
        self.about.setMaximumHeight(100)
        main_layout.addWidget(self.about)

        ############################# Check box #########################################

        self.terms = QCheckBox("I accept the terms and conditions.")
        main_layout.addWidget(self.terms)

        ############################# Push Button #########################################

        self.submit_button = QPushButton("Submit Registration")
        self.submit_button.setFixedWidth(150)

        botton_layout.addWidget(self.submit_button)
        botton_layout.setAlignment(Qt.AlignCenter)

        main_layout.addLayout(botton_layout)


        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("P2: Student Registration")
    window.setCentralWidget(StudentRegistrationForm())
    window.setFixedSize(400, 600)
    window.show()

    sys.exit(app.exec())