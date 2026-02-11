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
        button_layout = QHBoxLayout()

        title = QLabel("LOGIN")
        main_layout.addWidget(title)

        main_layout.addWidget(QLabel("Email"))
        self.email = QLineEdit()
        main_layout.addWidget(self.email)

        main_layout.addWidget(QLabel("Password"))
        self.Pass = QLineEdit()
        main_layout.addWidget(self.Pass)

        self.rem = QCheckBox("Remember me?")
        main_layout.addWidget(self.rem)

        self.log = QPushButton("LOGIN")
        self.log.setFixedWidth(150)
        button_layout.addWidget(self.log)
        button_layout.setAlignment(Qt.AlignCenter)
        
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        self.forgot = QLabel("Forgot password?")
        self.forgot.setAlignment(Qt.AlignRight)
        main_layout.addWidget(self.forgot)



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("P1: Login")
    window.setCentralWidget(login())
    window.setFixedSize(400, 500)
    window.show()

    sys.exit(app.exec())