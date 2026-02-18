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

        input_layout = QHBoxLayout()
        score_layout = QHBoxLayout()
        button_layout = QHBoxLayout()

        id = QLabel("Students ID: ")
        self.id = QComboBox()
        self.id.setEditable(True)
        self.id.setPlaceholderText("Select Student ID")

        input_layout.addWidget(id)
        input_layout.addWidget(self.id)

        name = QLabel("Student Name: ")
        self.name = QLineEdit()
        
        input_layout.addWidget(name)
        input_layout.addWidget(self.name)

        math = QLabel("Math: ")
        self.math = QSpinBox()
        self.math.setRange(0, 100)
        self.math.setValue(0)

        score_layout.addWidget(math)
        score_layout.addWidget(self.math)

        sci = QLabel("Science: ")
        self.sci = QSpinBox()
        self.sci.setRange(0, 100)
        self.sci.setValue(0)

        score_layout.addWidget(sci)
        score_layout.addWidget(self.sci)

        eng = QLabel("English: ")
        self.eng = QSpinBox()
        self.eng.setRange(0, 100)
        self.eng.setValue(0)

        score_layout.addWidget(eng)
        score_layout.addWidget(self.eng)

        self.add = QPushButton("Add Student")
        self.add.clicked.connect(self.add_student)
        
        self.reset = QPushButton("Reset Input")
        self.reset.clicked.connect(self.reset_input)

        self.clear = QPushButton("Clear All")
        self.clear.clicked.connect(self.clear_all)

        button_layout.addWidget(self.add)
        button_layout.addWidget(self.reset)
        button_layout.addWidget(self.clear)

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

        main_layout.addLayout(input_layout)
        main_layout.addLayout(score_layout)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(self.table)

    def add_student(self):
        stu_id = self.id.text().strip()
        stu_name = self.name.text().strip()
        stu_math = self.math.value()
        stu_sci = self.sci.value()
        stu_eng = self.eng.value()

        row_position = self.table.rowCount()
        self.table.insertRow(row_position)

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

        avg = total // 3
        avg_item = QTableWidgetItem(str(avg))

        if avg < 50:
            grade = QTableWidgetItem("F")
            grade.setBackground(QColor("#FF3300"))
        elif avg >= 50:
            grade = QTableWidgetItem("D")
        elif avg >= 60:
            grade = QTableWidgetItem("C")
        elif avg >= 70:
            grade = QTableWidgetItem("B")
        else:
            grade = QTableWidgetItem("A")
            grade.setBackground(QColor("#00FF84"))

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
        self.math.clear()
        self.sci.clear()
        self.eng.clear()

    def reset_input(self):
        self.id.clear()
        self.name.clear()
        self.math.clear()
        self.sci.clear()
        self.eng.clear()

    def clear_all(self):
        self.table.setRowCount(0)

def main():
    app = QApplication(sys.argv)
    window = Student()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()