"""
68040154-3
Jiravit Boonyaritchaikit
P2
"""

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
                               QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton,
                               QFrame, QSpinBox, QColorDialog, QFileDialog, QToolBar, QStyle, QSlider, QProgressBar)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction, QIcon, QPixmap

import sys, os, pyperclip

default_color = "#210035"

class game(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("P2: RPG Character Builder")
        self.setGeometry(100, 100, 400, 500)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        self.main_layout = QHBoxLayout(central_widget)
        self.create_form()
        self.bg = QWidget()
        self.card_layout = QVBoxLayout(self.bg)
        self.card()

        # self.create_menu()

        # # toolbar
        # self.create_toolbar()

        # status bar
        self.statusBar().showMessage("Ready - create your character")

        self.perma = QLabel("Created by Jerry♥")
        self.statusBar().addPermanentWidget(self.perma)

    def create_form(self):
        form_layout = QFormLayout()

#============================ATTRIBUTE=========================================

        self.name = QLineEdit()
        self.name.setPlaceholderText("Enter Character name...")

        self.race = QComboBox()
        self.race.addItems(["Human", "Elf", "Dwarf", "Orc", "Undead"])
        self.race.setPlaceholderText("Choose your race")
        self.race.setCurrentIndex(-1)

        self.clas = QComboBox()
        self.clas.addItems(["Warrior", "Mage", "Rogue", "Paladin", "Ranger"])
        self.clas.setPlaceholderText("Choose your class")
        self.clas.setCurrentIndex(-1)

        self.gender = QComboBox()
        self.gender.addItems(["Male", "Female", "Other"])
        self.gender.setPlaceholderText("Choose your gender")
        self.gender.setCurrentIndex(-1)

        form_layout.addRow("Character:", self.name)
        form_layout.addRow("Race:", self.race)
        form_layout.addRow("Class:", self.clas)
        form_layout.addRow("Gender:", self.gender)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        form_layout.addWidget(line)

#============================STAT=========================================

        form_layout.addWidget(QLabel("Stat Allocation"))

        self.max_point = 40

#============================SET SLIDER====================================

        self.str = QSlider(Qt.Horizontal)
        self.str.setMinimum(0)
        self.str.setMaximum(20)
        self.str.setValue(5)
        self.str_tex = QLabel("5")

        self.dex = QSlider(Qt.Horizontal)
        self.dex.setMinimum(0)
        self.dex.setMaximum(20)
        self.dex.setValue(5)
        self.dex_tex = QLabel("5")

        self.int = QSlider(Qt.Horizontal)
        self.int.setMinimum(0)
        self.int.setMaximum(20)
        self.int.setValue(5)
        self.int_tex = QLabel("5")

        self.vit = QSlider(Qt.Horizontal)
        self.vit.setMinimum(0)
        self.vit.setMaximum(20)
        self.vit.setValue(5)
        self.vit_tex = QLabel("5")

#============================CONNECT=========================================

        self.str.valueChanged.connect(self.update_stat)
        self.dex.valueChanged.connect(self.update_stat)
        self.int.valueChanged.connect(self.update_stat)
        self.vit.valueChanged.connect(self.update_stat)

#============================TURN 2 WIDGET TO 1 LAYOUT========================

        str_layout = QHBoxLayout()
        str_layout.addWidget(self.str)
        str_layout.addWidget(self.str_tex)

        dex_layout = QHBoxLayout()
        dex_layout.addWidget(self.dex)
        dex_layout.addWidget(self.dex_tex)

        int_layout = QHBoxLayout()
        int_layout.addWidget(self.int)
        int_layout.addWidget(self.int_tex)

        vit_layout = QHBoxLayout()
        vit_layout.addWidget(self.vit)
        vit_layout.addWidget(self.vit_tex)


#============================ADD LAYOUT TO ROW==============================

        form_layout.addRow("💪 STR:", str_layout)
        form_layout.addRow("🏃‍♂️ DEX:", dex_layout)
        form_layout.addRow("🧠 INT:", int_layout)
        form_layout.addRow("❤️ VIT:", vit_layout)

#============================POINTS USED==============================

        self.point_used = QLabel("Points used: 20 / 40")
        form_layout.addWidget(self.point_used)

#============================BUTTON==============================
        gen_btr = QPushButton("Generate Character Sheet")

        form_layout.addWidget(gen_btr)

    
        
        self.main_layout.addLayout(form_layout)

        self.update_stat()

    def card(self):
        self.bg.setStyleSheet(f"background-color: {default_color}; border-radius: 250px;")

        self.name = QLabel("- Character Name -")

        att_layout = QHBoxLayout()
        race_dis = QLabel("Race")
        class_dis = QLabel("Class")
        
        att_layout.addWidget(race_dis)
        att_layout.addWidget(class_dis)

        line = QFrame()
        line.setFrameShape(QFrame.Shape.HLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)


        

        self.card_layout.addWidget(self.name)
        self.card_layout.addLayout(att_layout)
        self.card_layout.addWidget(line)

        self.stat_bar = {}

        for stat in ["STR", "DEX", "INT", "VIT"]:
            stat_label = QLabel(stat)

            bar = QProgressBar()
            bar.setRange(0, 20)
            bar.setValue(5)
            bar.setTextVisible(False)
            bar.setStyleSheet("""
            QProgressBar {
                background-color: #cccccc;
                border-radius: 5px;}
            QProgressBar::chuck {
                background-color: #3b82f6;
                border-radius: 5px;
                              }
                              """)
            
            self.card_layout.addWidget(stat_label)
            self.card_layout.addWidget(bar)

            self.stat_bar[stat] = bar

        self.main_layout.addWidget(self.bg)

    def update_stat(self):
        self.str_tex.setText(str(self.str.value()))
        self.dex_tex.setText(str(self.dex.value()))
        self.int_tex.setText(str(self.int.value()))
        self.vit_tex.setText(str(self.vit.value()))

        total = (self.str.value()
                 + self.dex.value()
                 + self.int.value()
                 + self.vit.value())
        
        self.point_used.setText(f"Points used: {total} / {self.max_point}")
        # if total > self.max_point:
        #     self.point_used.setStyleSheet(QColor("#FF3300"))
        # else:
        #     self.point_used.setStyleSheet(QColor("#000000"))



def main():
    app = QApplication(sys.argv)
    window = game()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()