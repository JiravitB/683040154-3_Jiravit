"""
Jiravit Boonyaritchaikit
683040154-3
P3
"""

from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QLabel, QComboBox,
                             QTableWidget, QTableWidgetItem, QHeaderView)

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import sys


class BMICalculator(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Title
        title = QLabel("Adult and Child BMI Calculator")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            background-color: #C85A54;
            color: white;
            font-size: 18px;
            font-weight: bold;
            padding: 12px;
            border-radius: 5px;
        """)
        main_layout.addWidget(title)
        main_layout.addSpacing(10)

        # Calculate BMI for
        calc_layout = QHBoxLayout()
        calc_layout.addWidget(QLabel("Calculate BMI for"))
        self.age_combo = QComboBox()
        self.age_combo.addItems(["Adult Age 20+", "Child Age 2-19"])
        self.age_combo.setFixedWidth(150)
        calc_layout.addWidget(self.age_combo)
        calc_layout.addStretch()
        main_layout.addLayout(calc_layout)

        # Weight
        weight_layout = QHBoxLayout()
        weight_layout.addWidget(QLabel("Weight:"))
        self.weight_input = QLineEdit()
        self.weight_input.setFixedWidth(120)
        weight_layout.addWidget(self.weight_input)
        self.weight_unit = QComboBox()
        self.weight_unit.addItems(["pounds", "kilograms"])
        self.weight_unit.setFixedWidth(120)
        weight_layout.addWidget(self.weight_unit)
        weight_layout.addStretch()
        main_layout.addLayout(weight_layout)

        # Height
        height_layout = QHBoxLayout()
        height_layout.addWidget(QLabel("Height:"))
        self.height_feet = QLineEdit()
        self.height_feet.setFixedWidth(120)
        height_layout.addWidget(self.height_feet)
        self.height_unit = QComboBox()
        self.height_unit.addItems(["feet", "meters"])
        self.height_unit.setFixedWidth(120)
        height_layout.addWidget(self.height_unit)
        height_layout.addStretch()
        main_layout.addLayout(height_layout)

        # Inches
        inches_layout = QHBoxLayout()
        inches_layout.addSpacing(70)
        self.height_inches = QLineEdit()
        self.height_inches.setFixedWidth(120)
        inches_layout.addWidget(self.height_inches)
        inches_layout.addWidget(QLabel("inches"))
        inches_layout.addStretch()
        main_layout.addLayout(inches_layout)

        main_layout.addSpacing(10)

        # Buttons
        button_layout = QHBoxLayout()
        self.clear_btn = QPushButton("Clear")
        self.clear_btn.setFixedSize(80, 35)
        button_layout.addWidget(self.clear_btn)
        button_layout.addStretch()
        self.calc_btn = QPushButton("Calculate")
        self.calc_btn.setFixedSize(100, 35)
        button_layout.addWidget(self.calc_btn)
        main_layout.addLayout(button_layout)

        main_layout.addSpacing(10)

        # Answer section
        answer_container = QWidget()
        answer_container.setStyleSheet("""
            border: 1px solid #DDD;
            border-radius: 5px;
        """)
        answer_layout = QVBoxLayout(answer_container)
        answer_layout.setContentsMargins(15, 15, 15, 15)

        answer_label = QLabel("Answer:")
        answer_layout.addWidget(answer_label)

        self.bmi_result = QLabel("BMI =")
        self.bmi_result.setAlignment(Qt.AlignCenter)
        self.bmi_result.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        answer_layout.addWidget(self.bmi_result)

        # Adult BMI table title
        table_title = QLabel("Adult BMI")
        table_title.setAlignment(Qt.AlignCenter)
        table_title.setStyleSheet("font-weight: bold; margin-top: 10px;")
        answer_layout.addWidget(table_title)

        # BMI Status Table
        self.bmi_table = QTableWidget(4, 2)
        self.bmi_table.setHorizontalHeaderLabels(["BMI", "Status"])
        self.bmi_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.bmi_table.verticalHeader().setVisible(False)
        self.bmi_table.setMaximumHeight(180)
        
        # Row 1 - Underweight
        item_bmi1 = QTableWidgetItem("≤ 18.4")
        item_bmi1.setBackground(QColor("#FFE082"))
        item_bmi1.setTextAlignment(Qt.AlignCenter)
        item_status1 = QTableWidgetItem("Underweight")
        item_status1.setTextAlignment(Qt.AlignCenter)
        self.bmi_table.setItem(0, 0, item_bmi1)
        self.bmi_table.setItem(0, 1, item_status1)

        # Row 2 - Normal
        item_bmi2 = QTableWidgetItem("18.5 - 24.9")
        item_bmi2.setBackground(QColor("#AED581"))
        item_bmi2.setTextAlignment(Qt.AlignCenter)
        item_status2 = QTableWidgetItem("Normal")
        item_status2.setTextAlignment(Qt.AlignCenter)
        self.bmi_table.setItem(1, 0, item_bmi2)
        self.bmi_table.setItem(1, 1, item_status2)

        # Row 3 - Overweight
        item_bmi3 = QTableWidgetItem("25.0 - 39.9")
        item_bmi3.setBackground(QColor("#FFB74D"))
        item_bmi3.setTextAlignment(Qt.AlignCenter)
        item_status3 = QTableWidgetItem("Overweight")
        item_status3.setTextAlignment(Qt.AlignCenter)
        self.bmi_table.setItem(2, 0, item_bmi3)
        self.bmi_table.setItem(2, 1, item_status3)

        # Row 4 - Obese
        item_bmi4 = QTableWidgetItem("≥ 40.0")
        item_bmi4.setBackground(QColor("#E57373"))
        item_bmi4.setTextAlignment(Qt.AlignCenter)
        item_status4 = QTableWidgetItem("Obese")
        item_status4.setTextAlignment(Qt.AlignCenter)
        self.bmi_table.setItem(3, 0, item_bmi4)
        self.bmi_table.setItem(3, 1, item_status4)

        answer_layout.addWidget(self.bmi_table)
        main_layout.addWidget(answer_container)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("P3: BMI Calculator")
    window.setCentralWidget(BMICalculator())
    window.setFixedSize(400, 650)
    window.show()

    sys.exit(app.exec())