"""
68040154-3
Jiravit Boonyaritchaikit
P1
"""

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
                               QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton,
                               QFrame, QSpinBox, QColorDialog, QFileDialog, QToolBar, QStyle)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction, QIcon, QPixmap

import sys, os, pyperclip


default_color = "#B0E0E6"

class PersonalCard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P1: Personal Info Card")
        self.setGeometry(100, 100, 400, 500)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.addSpacing(15)

        # input section
        self.input_layout = QFormLayout()
        self.input_layout.setVerticalSpacing(12)
        self.create_form()

        self.main_layout.addSpacing(5)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setLineWidth(1)
        line.setStyleSheet("background-color: #cccccc;")

        self.main_layout.addSpacing(10)

        # Output section
        self.bg_widget = QWidget()
        self.output_layout = QVBoxLayout(self.bg_widget)
        self.create_display()

        # menu
        self.create_menu()

        # toolbar
        self.create_toolbar()

        # status bar
        self.statusBar().showMessage("Fill in your details and click generate") 

    def create_form(self):
        form_layout = QFormLayout()

        self.name = QLineEdit()
        self.name.setPlaceholderText("First name and Lastname")
        
        self.age = QSpinBox()
        self.age.setRange(1,120)
        self.age.setValue(25)
        
        self.email = QLineEdit()
        self.email.setPlaceholderText("username@domain.name")
        
        self.position = QComboBox()
        self.position.addItems(["Teaching Staff","Supporting Staff","Student","Visitor"])
        self.position.setPlaceholderText("Choose your position")
        self.position.setCurrentIndex(-1)

        color_row = QWidget()
        color_layout = QHBoxLayout(color_row)
        self.fav_color = QColor(default_color)
        self.color_swatch = QLabel()
        self.color_swatch.setFixedSize(22, 22)
        self.color_swatch.setStyleSheet(f"background-color: {self.fav_color.name()}; border: 1px solid #888;")
        color_layout.addWidget(self.color_swatch)
        color_button = QPushButton("Pick New Color")
        color_button.clicked.connect(self.pick_color)
        color_layout.addWidget(color_button)

        form_layout.addRow("Full name.", self.name)
        form_layout.addRow("Age.", self.age)
        form_layout.addRow("Email.", self.email)
        form_layout.addRow("Position", self.position)
        form_layout.addRow("Favorite color:", QWidget())
        form_layout.itemAt(form_layout.rowCount()-1, QFormLayout.FieldRole).widget().setLayout(color_layout)

        self.main_layout.addLayout(form_layout)

    def pick_color(self):
        color = QColorDialog.getColor(self.fav_color, self, "Pick a Color")
        if color.isValid():
            self.fav_color = color
            self.color_swatch.setStyleSheet(f"background-color: {self.fav_color.name()}; border: 1px solid #888;")

    def create_display(self):
    
        self.bg_widget.setStyleSheet(f"background-color: {self.fav_color.name()}; \
                                     border-radius: 6px;")

        self.name_label = QLabel("Your name here")
        self.name_label.setStyleSheet("font-size: 18pt; font-weight: bold;")
        self.age_label = QLabel("(Age)")
        self.position_label = QLabel("Your position here")
        self.position_label.setStyleSheet("font-size: 14pt;")
        email_icon = QLabel()
        email_icon.setPixmap(QPixmap("mail.png").scaled(18, 18, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.email_label = QLabel("your_username@domain.name")
        email_layout = QHBoxLayout()
        email_layout.addWidget(email_icon)
        email_layout.addWidget(self.email_label)
        email_layout.addStretch()

        self.output_layout.addWidget(self.name_label)
        self.output_layout.addWidget(self.age_label)
        self.output_layout.addStretch()
        self.output_layout.addWidget(self.position_label)
        self.output_layout.addLayout(email_layout)
        self.output_layout.addSpacing(10)
        self.main_layout.addWidget(self.bg_widget)


    def update_display(self):
        self.name_label.setText(self.name.text())
        self.age_label.setText(f"({self.age.value()})")
        self.position_label.setText(self.position.currentText())
        self.email_label.setText(self.email.text())
        self.bg_widget.setStyleSheet(f"background-color:{self.fav_color.name()};border-radius:6px;")
        self.statusBar().showMessage("Card generated and displaying", 3000)


    def clear_form(self):
        self.name.clear()
        self.age.setValue(25)
        self.position.setCurrentIndex(-1)
        self.email.setText("username@domain.name")
        self.bg_widget.setStyleSheet(f"background-color: {default_color}; \
                                     border-radius: 4px;")

    def save_card(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save Card", "my_card.txt", "Text Files (*.txt)")
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(
                    f"Name: {self.name_label.text()}\n"
                    f"Age: {self.age_label.text()}\n"
                    f"Position: {self.position_label.text()}\n"
                    f"Email: {self.email_label.text()}\n"
                )
            self.statusBar().showMessage(f"Saved: {os.path.basename(filename)}", 3000)

    def clear_display(self):
        self.name_label.setText("Your Name")
        self.age_label.setText(f"(Age)")
        self.position_label.setText("Your Position")
        self.email_label.setText("your_username@domain.name")
        self.bg_widget.setStyleSheet(f"background-color: {default_color}; \
                                     border-radius: 4px;")

    def copy_card(self):
        pyperclip.copy(
            f"Name: {self.name_label.text()}\n"
            f"Age: {self.age_label.text()}\n"
            f"Position: {self.position_label.text()}\n"
            f"Email: {self.email_label.text()}"
        )
        self.statusBar().showMessage("Card copied to clipboard", 3000)

    def clear_all(self):
        self.clear_form()
        self.clear_display()

    def create_menu(self):
        file_menu = self.menuBar().addMenu("File")

        gen = QAction("Generate Card", self)
        gen.triggered.connect(self.update_display)
        file_menu.addAction(gen)

        save = QAction("Save Card", self)
        save.triggered.connect(self.save_card)
        file_menu.addAction(save)

        clear_disp = QAction("Clear Display", self)
        clear_disp.triggered.connect(self.clear_display)
        file_menu.addAction(clear_disp)

        exit_ac = QAction("Exit", self)
        exit_ac.triggered.connect(sys.exit)
        file_menu.addAction(exit_ac)

        edit_menu = self.menuBar().addMenu("Edit")

        copy = QAction("Copy Card", self)
        copy.triggered.connect(self.copy_card)
        edit_menu.addAction(copy)

        clear_form = QAction("Clear Form", self)
        clear_form.triggered.connect(self.clear_form)
        edit_menu.addAction(clear_form)

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        gen = QAction(self.style().standardIcon(QStyle.SP_CommandLink), "Generate", self)
        gen.triggered.connect(self.update_display)
        toolbar.addAction(gen)

        save = QAction(self.style().standardIcon(QStyle.SP_DialogSaveButton), "Save", self)
        save.triggered.connect(self.save_card)
        toolbar.addAction(save)

        clear = QAction(self.style().standardIcon(QStyle.SP_DialogDiscardButton), "Clear All", self)
        clear.triggered.connect(self.clear_all)
        toolbar.addAction(clear)

def main():
    app = QApplication(sys.argv)
    window = PersonalCard()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()