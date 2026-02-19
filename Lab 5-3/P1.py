from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                               QHBoxLayout, QLabel, QLineEdit, QPushButton,
                               QTableWidget, QTableWidgetItem, QSpinBox, QMessageBox, QComboBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
import sys

class Student(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Student scores and grades")
        self.setGeometry(100, 100, 800, 400)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

#create Layout
        input_layout = QHBoxLayout()
        score_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

#Student ID
        id = QLabel("Students ID: ")
        self.id = QComboBox()
        self.id.setPlaceholderText("Select Student ID")
        self.id.load_id("students.txt")

        input_layout.addWidget(id)
        input_layout.addWidget(self.id)

#Student Name
        name = QLabel("Student Name: ")
        self.name = QLineEdit()
        
        input_layout.addWidget(name)
        input_layout.addWidget(self.name)

#Math
        math = QLabel("Math: ")
        self.math = QSpinBox()
        self.math.setRange(0, 100)
        self.math.setValue(0)

        score_layout.addWidget(math)
        score_layout.addWidget(self.math)

#Science
        sci = QLabel("Science: ")
        self.sci = QSpinBox()
        self.sci.setRange(0, 100)
        self.sci.setValue(0)

        score_layout.addWidget(sci)
        score_layout.addWidget(self.sci)

#English
        eng = QLabel("English: ")
        self.eng = QSpinBox()
        self.eng.setRange(0, 100)
        self.eng.setValue(0)

        score_layout.addWidget(eng)
        score_layout.addWidget(self.eng)

#Add student button
        self.add = QPushButton("Add Student")
        self.add.clicked.connect(self.add_student)

#Add reset button
        self.reset = QPushButton("Reset Input")
        self.reset.clicked.connect(self.reset_input)

#Add clear button
        self.clear = QPushButton("Clear All")
        self.clear.clicked.connect(self.clear_all)

#Add all button to button layout
        button_layout.addWidget(self.add)
        button_layout.addWidget(self.reset)
        button_layout.addWidget(self.clear)

#Make table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels(["Student ID", "Name", "Math", "Science", "English", "Total", "Average", "Grade"])

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setColumnWidth(0,120)
        self.table.setColumnWidth(1,150)
        self.table.setColumnWidth(2,70)
        self.table.setColumnWidth(3,70)
        self.table.setColumnWidth(4,70)
        self.table.setColumnWidth(5,70)
        self.table.setColumnWidth(6,70)

#Add all layout to main layout
        main_layout.addLayout(input_layout)
        main_layout.addLayout(score_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

    def load_id(self, filename):
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
                ids = [line.strip() for line in lines if line.strip()]
        except FileNotFoundError:
            QMessageBox.warning(self, "File Error", f"{filename} not found.")

    def add_student(self):
        stu_id = self.id.currentText()
        stu_name = self.name.text().strip()
        stu_math = self.math.value()
        stu_sci = self.sci.value()
        stu_eng = self.eng.value()

#Validate ID
        if not stu_id:
            QMessageBox.warning(self, "Input Error", "Please enter ID")
            return

#validate name
        if not stu_name:
            QMessageBox.warning(self, "Input Error", "Please enter name")
            return
        
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

#Make everything to Table Item
        id_item = QTableWidgetItem(stu_id)
        name_item = QTableWidgetItem(stu_name)

        math_item = QTableWidgetItem(str(stu_math))
        if stu_math < 50:
            math_item.setBackground(QColor("#FF3300"))
        else:
            math_item.setBackground(QColor("#00FF84"))

        sci_item = QTableWidgetItem(str(stu_sci))
        if stu_sci < 50:
            sci_item.setBackground(QColor("#FF3300"))
        else:
            sci_item.setBackground(QColor("#00FF84"))

        eng_item = QTableWidgetItem(str(stu_eng))
        if stu_eng < 50:
            eng_item.setBackground(QColor("#FF3300"))
        else:
            eng_item.setBackground(QColor("#00FF84"))

        total = stu_math + stu_sci + stu_eng
        total_item = QTableWidgetItem(str(total))

        avg = total / 3
        avg_item = QTableWidgetItem(str(f"{avg:.2f}"))

        if avg >= 80:
            grade = QTableWidgetItem("A")
            grade.setBackground(QColor("#00FF84"))
        elif avg >= 70:
            grade = QTableWidgetItem("B")
        elif avg >= 60:
            grade = QTableWidgetItem("C")
        elif avg >= 50:
            grade = QTableWidgetItem("D")
        else:
            grade = QTableWidgetItem("F")
            grade.setBackground(QColor("#FF3300"))

#Add all Item to table
        self.table.setItem(row_position, 0, id_item)
        self.table.setItem(row_position, 1, name_item)
        self.table.setItem(row_position, 2, math_item)
        self.table.setItem(row_position, 3, sci_item)
        self.table.setItem(row_position, 4, eng_item)
        self.table.setItem(row_position, 5, total_item)
        self.table.setItem(row_position, 6, avg_item)
        self.table.setItem(row_position, 7, grade)

        self.id.clear()
        self.name.clear()
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)


    def reset_input(self):
        self.id.clear()
        self.name.clear()
        self.math.setValue(0)
        self.sci.setValue(0)
        self.eng.setValue(0)


    def clear_all(self):
        self.table.setRowCount(0)

def main():
    app = QApplication(sys.argv)
    window = Student()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()