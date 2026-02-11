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
from PySide6.QtGui import QPixmap
import sys

class login(QWidget):
    def __init__(self):
        super().__init__()
        
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()
        pic_layout = QHBoxLayout()

##Title
        title = QLabel("LOGIN")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        main_layout.addWidget(title)
        

#Email
        main_layout.addWidget(QLabel("Email"))
        self.email = QLineEdit()
        main_layout.addWidget(self.email)

#Password
        main_layout.addWidget(QLabel("Password"))
        self.Pass = QLineEdit()
        main_layout.addWidget(self.Pass)

#checkbox
        self.rem = QCheckBox("Remember me?")
        main_layout.addWidget(self.rem)

#PushNutton
        self.log = QPushButton("LOGIN")
        self.log.setFixedWidth(150)
        button_layout.addWidget(self.log)
        button_layout.setAlignment(Qt.AlignCenter)
        
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

#Forgot
        self.forgot = QLabel("Forgot password?")
        self.forgot.setAlignment(Qt.AlignRight)
        main_layout.addWidget(self.forgot)

#Line
        self.divider = QLabel("————————— OR —————————")
        self.divider.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.divider)

#Pic
        Gmail = QLabel()
        try:
            pixmap = QPixmap("Gmail_pic.PNG")
            Gmail.setPixmap(pixmap.scaled(
                400, 400,  # width, height
                Qt.KeepAspectRatio,  # maintain aspect ratio
                Qt.SmoothTransformation  # smooth scaling
            ))
        except:
            Gmail.setText("Image not found: WP.png")
            Gmail.setAlignment(Qt.AlignCenter)

        Gmail.setAlignment(Qt.AlignCenter)

        pic_layout.addWidget(Gmail)
#Need acc
        self.need = QLabel("Need an account? SIGN UP")
        self.need.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.need)

        




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    window.setWindowTitle("P1: Login")
    window.setCentralWidget(login())
    window.setFixedSize(300, 400)
    window.show()

    sys.exit(app.exec())