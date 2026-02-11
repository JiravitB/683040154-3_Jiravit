"""
Jiravit Boonyaritchaikit
683040154-3
P1
"""

from PySide6.QtWidgets import (QApplication, QMainWindow,
                             QVBoxLayout, QWidget, QHBoxLayout,
                             QGridLayout, QFormLayout, QLineEdit,
                             QSpinBox, QPushButton, QLabel, QDateEdit, QButtonGroup,
                             QRadioButton, QComboBox, QTextEdit, QCheckBox)

from PySide6.QtCore import QDate, Qt
import sys

class login(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()

        title = QLabel("LOGIN")
        main_layout.addWidget(title)

        

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("P1: Login")
    window.setCentralWidget(login())
    window.setFixedSize(400, 600)
    window.show()

    sys.exit(app.exec())