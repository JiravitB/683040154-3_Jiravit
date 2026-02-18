"""
Jiravit Boonyaritchaikit
683040154-3
"""

import sys
from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QLabel, )
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont 

class CalculatorLayout(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        main_layout = QVBoxLayout()

        display_layout = QVBoxLayout()
        calc_type = QLabel("Standard")
        calc_type.setFont(QFont("Arial", 14))

        self.current_display = "0"
        self.display = QLabel(self.current_display)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFont(QFont("Arial",40))

        display_layout.addWidget(calc_type)
        display_layout.addWidget(self.display)

        layout = QGridLayout()
        for i in range(4):
            layout.setColumnStretch(i, 1)

        for i in range(3, 9):
            layout.setRowStretch(i, 1)


        # Basic grid positioning
        layout.addWidget(QPushButton("%"), 3, 0)
        layout.addWidget(QPushButton("CE"), 3, 1)
        
        buttonc = QPushButton("C")
        buttonc.clicked.connect(self.reset_zero)
        layout.addWidget(buttonc, 3, 2)
        
        buttonx = QPushButton("<x")
        buttonx.clicked.connect(self.del_last)
        layout.addWidget(buttonx, 3, 3)

        layout.addWidget(QPushButton("1/x"), 4, 0)
        layout.addWidget(QPushButton("x^2"), 4, 1)
        layout.addWidget(QPushButton("2 sqr x"), 4, 2)
        layout.addWidget(QPushButton("÷"), 4, 3)
        
        button7 = QPushButton("7")
        button7.clicked.connect(lambda: self.append_value("7"))
        layout.addWidget(button7, 5, 0)

        button8 = QPushButton("8")
        button8.clicked.connect(lambda: self.append_value("8"))
        layout.addWidget(button8, 5, 1)  # row 0, col 1

        button9 = QPushButton("9")
        button9.clicked.connect(lambda: self.append_value("9"))
        layout.addWidget(button9, 5, 2)  # row 0, col 2
        layout.addWidget(QPushButton("X"), 5, 3)

        button4 = QPushButton("4")
        button4.clicked.connect(lambda: self.append_value("4"))
        layout.addWidget(button4, 6, 0)

        button5 = QPushButton("5")
        button5.clicked.connect(lambda: self.append_value("5"))
        layout.addWidget(button5, 6, 1)

        button6 = QPushButton("6")
        button6.clicked.connect(lambda: self.append_value("6"))
        layout.addWidget(button6, 6, 2)
        layout.addWidget(QPushButton("-"), 6, 3)

        button1 = QPushButton("1")
        button1.clicked.connect(lambda: self.append_value("1"))
        layout.addWidget(button1, 7, 0)

        button2 = QPushButton("2")
        button2.clicked.connect(lambda: self.append_value("2"))
        layout.addWidget(button2, 7, 1)

        button3 = QPushButton("3")
        button3.clicked.connect(lambda: self.append_value("3"))
        layout.addWidget(button3, 7, 2)
        layout.addWidget(QPushButton("+"), 7, 3)    

        layout.addWidget(QPushButton("+/-"), 8, 0)

        button0 = QPushButton("0")
        button0.clicked.connect(lambda: self.append_value("0"))
        layout.addWidget(button0, 8, 1)
        layout.addWidget(QPushButton("."), 8, 2)
        layout.addWidget(QPushButton("="), 8, 3)
        # Widget spanning multiple cells

        # Spacing and margins
        layout.setSpacing(1)
        layout.setContentsMargins(5, 5, 5, 5)

        # Column/Row stretch
        layout.setColumnStretch(0, 1)  # First column stretches more
        layout.setRowStretch(1, 2)     # Second row stretches more

        main_layout.addLayout(display_layout)
        main_layout.addLayout(layout)

        self.setLayout(main_layout)

    def append_value(self, new_num):
        if self.current_display == "0":
            self.current_display = str(new_num)
        else:
            self.current_display += str(new_num)

        self.display.setText(self.current_display)

    def reset_zero(self):
        self.current_display = "0"
        self.display.setText(self.current_display)

    def del_last(self):
        if self.current_display != "0":
            self.current_display = self.current_display[:-1]
            self.display.setText(self.current_display)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setCentralWidget(CalculatorLayout())
        self.resize(300, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())