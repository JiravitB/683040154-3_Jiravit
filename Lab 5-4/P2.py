"""
68040154-3
Jiravit Boonyaritchaikit
P2
"""

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QFormLayout,
                               QHBoxLayout, QLabel, QComboBox, QLineEdit, QPushButton,
                               QFrame, QSpinBox, QColorDialog, QFileDialog, QToolBar, QStyle,
                                QSlider, QProgressBar, QMessageBox)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QAction, QIcon, QPixmap

import random
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

        self.create_menu()

        self.create_toolbar()

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
        gen_btr.clicked.connect(self.gen)

        form_layout.addWidget(gen_btr)

    
        
        self.main_layout.addLayout(form_layout)

        self.update_stat()
#============================MAKE CARD==============================

    def card(self):
        self.bg.setFixedWidth(220)
        self.bg.setStyleSheet("""
            QWidget {
                background-color: #1e1b2e;
                border-radius: 16px;
            }
        """)

#============================NAME==============================
        self.card_name = QLabel("— Character Name —")
        self.card_name.setAlignment(Qt.AlignCenter)
        self.card_name.setStyleSheet("""
            color: #c084fc;
            font-size: 15px;
            font-weight: bold;
            letter-spacing: 1px;
            background: transparent;
        """)

#============================RACE & CLASS==============================
        self.card_sub = QLabel("Race  •  Class")
        self.card_sub.setAlignment(Qt.AlignCenter)
        self.card_sub.setStyleSheet("""
            color: #a0a0c0;
            font-size: 11px;
            background: transparent;
        """)

#============================LINE==============================
        divider = QFrame()
        divider.setFrameShape(QFrame.Shape.HLine)
        divider.setStyleSheet("color: #3a3555; background-color: #3a3555;")
        divider.setFixedHeight(1)

        self.card_layout.addWidget(self.card_name)
        self.card_layout.addWidget(self.card_sub)
        self.card_layout.addSpacing(6)
        self.card_layout.addWidget(divider)
        self.card_layout.addSpacing(10)

#============================STAT==============================
        self.stat_bars = {}
        self.stat_val_labels = {}

        for stat in ["STR", "DEX", "INT", "VIT"]:
            row = QHBoxLayout()
            row.setSpacing(8)

#============================STAT LABEL==============================
            name_lbl = QLabel(stat)
            name_lbl.setFixedWidth(28)
            name_lbl.setStyleSheet("""
                color: #c0b8e0;
                font-size: 11px;
                font-weight: bold;
                background: transparent;
            """)

#============================STAT BAR==============================
            bar = QProgressBar()
            bar.setRange(0, 20)
            bar.setValue(5)
            bar.setTextVisible(False)
            bar.setFixedHeight(8)
            bar.setStyleSheet("""
                QProgressBar {
                    background-color: #2e2a45;
                    border-radius: 4px;
                    border: none;
                }
                QProgressBar::chunk {
                    background-color: #7c3aed;
                    border-radius: 4px;
                }
            """)

#============================STAT VALUE==============================
            val_lbl = QLabel("—")
            val_lbl.setFixedWidth(22)
            val_lbl.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            val_lbl.setStyleSheet("""
                color: #a0a0c0;
                font-size: 11px;
                background: transparent;
            """)

            row.addWidget(name_lbl)
            row.addWidget(bar)
            row.addWidget(val_lbl)

            self.card_layout.addLayout(row)
            self.stat_bars[stat] = bar
            self.stat_val_labels[stat] = val_lbl

        self.card_layout.addStretch()
        self.main_layout.addWidget(self.bg)

#================================================================
#=========================== METHOD =============================
#================================================================

#===================UPDATE STAT SLIDER===========================
    def update_stat(self):
        self.str_tex.setText(str(self.str.value()))
        self.dex_tex.setText(str(self.dex.value()))
        self.int_tex.setText(str(self.int.value()))
        self.vit_tex.setText(str(self.vit.value()))

        self.values = {
            "STR": self.str.value(),
            "DEX": self.dex.value(),
            "INT": self.int.value(),
            "VIT": self.vit.value(),
        }

        self.total = sum(self.values.values())
        
        self.point_used.setText(f"Points used: {self.total} / {self.max_point}")
        if self.total > self.max_point:
             self.point_used.setStyleSheet("color: #FF3300;")
             self.statusBar().showMessage("Ain't it too OP?", 3000)
        else:
             self.point_used.setStyleSheet("color: #cccccc;")

#============================GEN CARD==============================

    def gen(self):

#============================VALIDATE POINT==============================
        if self.total > self.max_point:
            msg = QMessageBox(self)
            msg.setWindowTitle("Too OP!")
            msg.setText("MY BRO YOU NOT SUNG JIN WOO!!")
            msg.setInformativeText(f"Points used {self.total} exceeds the maximum of {self.max_point}!")
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.exec()
            return

        self.card_name.setText(f"— {self.name.text()} —")
        self.card_sub.setText(f"{self.race.currentText()}  •  {self.clas.currentText()}")
        
        if self.stat_bars:
            for stat, val in self.values.items():
                self.stat_bars[stat].setValue(val)
                self.stat_val_labels[stat].setText(str(val))
        
        self.statusBar().showMessage("Generating your character!", 3000)

#============================SAVE TO FILE==============================

    def save(self):
        filename, _ = QFileDialog.getSaveFileName(self, " Save Character", "My character.txt", "Text Files (*.txt)")
        if filename:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(
                    f"Name: {self.name.text()}\n"
                    f"Race: {self.race.currentText()}\n"
                    f"Class: {self.clas.currentText()}\n"
                    f"Gender: {self.gender.currentText()}\n"
                    "\n"
                    f"STR: {self.str_tex.text()} / 20\n"
                    f"DEX: {self.dex_tex.text()} / 20\n"
                    f"INT: {self.int_tex.text()} / 20\n"
                    f"VIT: {self.vit_tex.text()} / 20\n"
                )
            self.statusBar().showMessage(f"Saved: {os.path.basename(filename)}", 3000)

#============================RANDOM==============================

    def random(self):
        """ Random method will use braking stick method
        |-------|---------|-----------|----------|
        0      cut1     cut2        cut3        40
           val1     val2       val3        val4
  
        will be something like this
        """

#============================ASSIGN CUT POINTS AND CUT==============================
        points = self.max_point
        cuts = sorted(random.sample(range(1, points), 3))
        vals = [cuts[0], cuts[1] - cuts[0], cuts[2] - cuts[1], points - cuts[2]]

#======================MAKE LIST WITH EACH CAP AT 20==============================
        clamped = [min(v, 20) for v in vals]
        overflow = sum(vals) - sum(clamped)

#============================IF POINTS OVERFLOW GIVE TO OTHER====================
        for i in range(len(clamped)):
            if overflow <= 0:
                break
            room = 20 - clamped[i]
            add = min(room, overflow)
            clamped[i] += add
            overflow -= add

        random.shuffle(clamped)
        
#============================SET VALUE==============================
        self.str.setValue(clamped[0])
        self.dex.setValue(clamped[1])
        self.int.setValue(clamped[2])
        self.vit.setValue(clamped[3])

        self.update_stat()
        self.statusBar().showMessage("LET'S GO GAMBLING!!", 3000)

#============================RESRT ALL FILED==============================

    def reset(self):
        self.name.clear()
        self.race.setCurrentIndex(-1)
        self.clas.setCurrentIndex(-1)
        self.gender.setCurrentIndex(-1)

        self.str.setValue(5)
        self.dex.setValue(5)
        self.int.setValue(5)
        self.vit.setValue(5)
        self.update_stat

        self.card_name.setText("— Character Name —")
        self.card_sub.setText("Race  •  Class")

        if self.stat_bars:
            for stat, val in self.values.items():
                self.stat_bars[stat].setValue(val)
                self.stat_val_labels[stat].setText(str(val))

        self.statusBar().showMessage("Fresh start!! Got a new idea?", 3000)

#============================RESET ALL STAT==============================

    def re_stat(self):
        self.str.setValue(5)
        self.dex.setValue(5)
        self.int.setValue(5)
        self.vit.setValue(5)
        self.update_stat

        if self.stat_bars:
            for stat, val in self.values.items():
                self.stat_bars[stat].setValue(val)
                self.stat_val_labels[stat].setText(str(val))

        self.statusBar().showMessage("Reset all stat!!", 3000)

#============================MENU==============================

    def create_menu(self):
        game_menu = self.menuBar().addMenu("Game")

        new = QAction("New Character", self)
        new.triggered.connect(self.reset)
        game_menu.addAction(new)

        gen = QAction("Generate Sheet", self)
        gen.triggered.connect(self.gen)
        game_menu.addAction(gen)

        save = QAction("Save Sheet", self)
        save.triggered.connect(self.save)
        game_menu.addAction(save)

        exit_ac = QAction("Exit", self)
        exit_ac.triggered.connect(sys.exit)
        game_menu.addAction(exit_ac)


        edit_menu = self.menuBar().addMenu("Edit")

        reset = QAction("Reset Stat", self)
        reset.triggered.connect(self.re_stat)
        edit_menu.addAction(reset)

        random = QAction("Randomize", self)
        random.triggered.connect(self.random)
        edit_menu.addAction(random)
    
#============================TOOLBAR==============================

    def create_toolbar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

        new_t = QAction("📖 New", self)
        new_t.triggered.connect(self.reset)
        toolbar.addAction(new_t)

        gen_t = QAction("✒️ Generate", self)
        gen_t.triggered.connect(self.gen)
        toolbar.addAction(gen_t)

        random_t = QAction("🎲 Random", self)
        random_t.triggered.connect(self.random)
        toolbar.addAction(random_t)

        save_t = QAction("📥 Save", self)
        save_t.triggered.connect(self.save)
        toolbar.addAction(save_t)


def main():
    app = QApplication(sys.argv)
    window = game()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()