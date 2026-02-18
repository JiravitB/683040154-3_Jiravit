"""
Jiravit Boonyaritchaikit
683040154-3
P1
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                               QVBoxLayout, QHBoxLayout, QGridLayout, QWidget, QLabel, QLineEdit,
                               QPushButton, QComboBox, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
kg = "kilograms"
lb = "pounds"
cm = "centimeters"
m = "meters"
ft = "feet"
adult = "Adults 20+"
child = "Children and Teenagers (5-19)"

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("P1: BMI Calculator")
        self.setGeometry(100, 100, 350, 550)

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main vertical layout
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setSpacing(10)
        self.main_layout.setContentsMargins(10, 10, 10, 10)

        # Header Label (Red background)
        self.header_label = QLabel("Adult and Child BMI Calculator")
        self.header_label.setAlignment(Qt.AlignCenter)
        self.header_label.setFont(QFont("Arial", 12, QFont.Bold))
        self.header_label.setStyleSheet("background-color: #A52A2A; color: white; padding: 5px;")
        self.header_label.setFixedHeight(40)
        self.main_layout.addWidget(self.header_label)

        # Create an input section object
        self.input_section = InputSection()
        self.main_layout.addWidget(self.input_section)
        
        # create an output section object
        self.output_section = OutputSection()
        self.main_layout.addWidget(self.output_section)

        # Connect signals: We pass the output_section instance to the input_section methods
        self.input_section.btn_submit.clicked.connect(lambda: self.input_section.submit_reg(self.output_section))
        self.input_section.btn_clear.clicked.connect(lambda: self.input_section.clear_form(self.output_section))


class OutputSection(QWidget):
    def __init__(self):
        super().__init__()

        #Main layout for output
        self.outer_layout = QVBoxLayout()
        self.outer_layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(self.outer_layout)

        #Colored Background
        self.result_container = QWidget()
        self.result_container.setStyleSheet("background-color: #FAF0E6;")  # Linen color

        #Layout inside the colored container
        self.container_layout = QVBoxLayout()
        self.container_layout.setContentsMargins(20, 20, 20, 20)
        self.result_container.setLayout(self.container_layout)

        #"Your BMI" Label
        self.lbl_title = QLabel("Your BMI")
        self.lbl_title.setStyleSheet("color: #000000;")
        self.lbl_title.setFont(QFont("Arial", 10, QFont.Bold))
        self.lbl_title.setAlignment(Qt.AlignCenter)
        self.container_layout.addWidget(self.lbl_title)

        #The BMI Value Number
        self.bmi_text = QLabel("0.00")
        self.bmi_text.setAlignment(Qt.AlignCenter)
        self.bmi_text.setStyleSheet("color: #6666FF;")
        self.bmi_text.setFont(QFont("Arial", 28, QFont.Bold))
        self.container_layout.addWidget(self.bmi_text)

        #Adult Table
        self.adult_table_widget = self.create_adult_table()
        self.container_layout.addWidget(self.adult_table_widget)
        self.adult_table_widget.hide()

        #Child Links
        self.child_link_widget = self.create_child_links()
        self.container_layout.addWidget(self.child_link_widget)
        self.child_link_widget.hide()

        # Add stretch to push content up if empty, or space it out
        self.container_layout.addStretch()

        # Add the colored container to the outer layout
        self.outer_layout.addWidget(self.result_container)

    def create_adult_table(self):
        container = QWidget()
        table_layout = QGridLayout(container)
        table_layout.setSpacing(10)

        # Headers
        l1 = QLabel("BMI")
        l1.setFont(QFont("Arial", 10, QFont.Bold))
        l1.setStyleSheet("color: #000000;")
        table_layout.addWidget(l1, 0, 0, Qt.AlignCenter)
        
        l2 = QLabel("Condition")
        l2.setFont(QFont("Arial", 10, QFont.Bold))
        l2.setStyleSheet("color: #000000;")
        table_layout.addWidget(l2, 0, 1, Qt.AlignLeft)

        data = [
            ("< 18.5", "Thin"),
            ("18.5 - 25.0", "Normal"),
            ("25.1 - 30.0", "Overweight"),
            ("> 30.0", "Obese")
        ]

        for i, (range_val, cond_val) in enumerate(data, start=1):
            # Create labels and set color to black
            l_range = QLabel(range_val)
            l_range.setStyleSheet("color: #000000;") 
            table_layout.addWidget(l_range, i, 0, Qt.AlignCenter)

            l_cond = QLabel(cond_val)
            l_cond.setStyleSheet("color: #000000;")
            table_layout.addWidget(l_cond, i, 1, Qt.AlignLeft)

        return container

    def create_child_links(self):
        container = QWidget()
        layout = QVBoxLayout(container)
        
        info = QLabel("For child's BMI interpretation, please click one of the following links.")
        info.setStyleSheet("color: #000000;")
        info.setWordWrap(True)
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)

        link_box = QHBoxLayout()
        
        boy_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-boys-z-5-19years.pdf?sfvrsn=4007e921_4">BMI graph for BOYS</a>')
        girl_link = QLabel('<a href="https://cdn.who.int/media/docs/default-source/child-growth/growth-reference-5-19-years/bmi-for-age-(5-19-years)/cht-bmifa-girls-z-5-19years.pdf?sfvrsn=c708a56b_4">BMI graph for GIRLS</a>')
        boy_link.setOpenExternalLinks(True)
        girl_link.setOpenExternalLinks(True)

        link_box.addWidget(boy_link)
        link_box.addWidget(girl_link)
        link_box.setAlignment(Qt.AlignCenter)
        
        layout.addLayout(link_box)
        return container

    def update_results(self, bmi, age_group):
        self.bmi_text.setText(f"{bmi:.2f}")
        
        if age_group == adult:
            self.adult_table_widget.show()
            self.child_link_widget.hide()
        else:
            self.adult_table_widget.hide()
            self.child_link_widget.show()

    def clear_result(self):
        self.bmi_text.setText("0.00")
        self.adult_table_widget.hide()
        self.child_link_widget.hide()


class InputSection(QWidget):

    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.setLayout(self.layout)

        #Age Group
        self.layout.addWidget(QLabel("BMI age group:"), 0, 0)
        self.combo_age = QComboBox()
        self.combo_age.addItems([adult, child])
        self.layout.addWidget(self.combo_age, 0, 1, 1, 2)

        #Weight
        self.layout.addWidget(QLabel("Weight:"), 1, 0)
        self.txt_weight = QLineEdit()
        self.layout.addWidget(self.txt_weight, 1, 1)
        
        self.combo_weight = QComboBox()
        self.combo_weight.addItems([kg, lb])
        self.layout.addWidget(self.combo_weight, 1, 2)

        #Height
        self.layout.addWidget(QLabel("Height:"), 2, 0)
        self.txt_height = QLineEdit()
        self.layout.addWidget(self.txt_height, 2, 1)

        self.combo_height = QComboBox()
        self.combo_height.addItems([cm, m, ft])
        self.layout.addWidget(self.combo_height, 2, 2)

        #Buttons
        self.btn_clear = QPushButton("clear")
        self.btn_submit = QPushButton("Submit Registration")
        
        # Spacer row to push buttons down slightly
        self.layout.setRowMinimumHeight(3, 10)
        
        self.layout.addWidget(self.btn_clear, 4, 0, 1, 2)
        self.layout.addWidget(self.btn_submit, 4, 2)

    def clear_form(self, output_section):
        # Clear inputs
        self.txt_weight.clear()
        self.txt_height.clear()
        self.combo_age.setCurrentIndex(0)
        self.combo_weight.setCurrentIndex(0)
        self.combo_height.setCurrentIndex(0)

        # Clear output
        output_section.clear_result()

    def submit_reg(self, output_section):
        bmi = self.calculate_BMI()
        if bmi is not None:
            group = self.combo_age.currentText()
            output_section.update_results(bmi, group)

    def calculate_BMI(self):
        try:
            w_str = self.txt_weight.text()
            h_str = self.txt_height.text()
            
            #if not w_str or not h_str:
                #return None
            
            weight = float(w_str)
            height = float(h_str)
            
            w_unit = self.combo_weight.currentText()
            h_unit = self.combo_height.currentText()

            # Normalize to kg
            if w_unit == lb:
                weight = weight * 0.45359237
            if weight <= 0:
                QMessageBox.warning(self, "Input Error", "Weight cannot be negative or zero")
                return None

            # Normalize to meters
            if h_unit == cm:
                height = height / 100.0
            elif h_unit == ft:
                height = height * 0.3048

            if height <= 0:
                QMessageBox.warning(self, "Input Error", "Height cannot be negative or zero")
                return None

            return weight / (height ** 2)

        except ValueError:
            QMessageBox.warning(self, "Input Error", "Please enter valid numbers") # Handle non-numeric input
        #except ZeroDivisionError:
            #QMessageBox.warning(self, "Input Error", "Height cannot be zero")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()