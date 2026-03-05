import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QStackedWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout,
    QLabel, QLineEdit, QDateEdit, QSpinBox,
    QPushButton, QDialog, QMessageBox, QScrollArea,
    QFrame, QSizePolicy
)
from PySide6.QtCore import Qt, Signal, QDate
from PySide6.QtGui import QFont


class RoomCard(QWidget):
    """
    Room information card — Custom Widget Class
    """

    # Signal: emits (room_name, price, max_guests) when user clicks Select
    room_selected = Signal(str, int, int)

    def __init__(self, room_name: str, price: int, description: str, emoji: str = "🏨", max_guests: int = 2):
        super().__init__()
        self._is_selected = False
        self._room_name = room_name
        self._price = price
        self._max_guests = max_guests

        self._build_ui(emoji, room_name, price, description, max_guests)
        self.deselect()  # Set default style

    def _build_ui(self, emoji: str, room_name: str, price: int, description: str, max_guests: int):
        self.setFixedSize(170, 210)
        self.setCursor(Qt.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 14, 14, 14)
        layout.setSpacing(6)

        # Emoji icon
        emoji_lbl = QLabel(emoji)
        emoji_lbl.setAlignment(Qt.AlignCenter)
        emoji_lbl.setFont(QFont("Segoe UI Emoji", 28))

        # Room name
        name_lbl = QLabel(room_name)
        name_lbl.setAlignment(Qt.AlignCenter)
        name_lbl.setFont(QFont("Segoe UI", 11, QFont.Bold))
        name_lbl.setStyleSheet("color: #1e1b4b;")

        # Price
        price_lbl = QLabel(f"${price} / night")
        price_lbl.setAlignment(Qt.AlignCenter)
        price_lbl.setFont(QFont("Segoe UI", 10))
        price_lbl.setStyleSheet("color: #6366f1; font-weight: bold;")

        # Description
        desc_lbl = QLabel(description)
        desc_lbl.setAlignment(Qt.AlignCenter)
        desc_lbl.setFont(QFont("Segoe UI", 8))
        desc_lbl.setStyleSheet("color: #6b7280;")
        desc_lbl.setWordWrap(True)

        # Max guests badge
        capacity_lbl = QLabel(f"👥 Max {max_guests} guest(s)")
        capacity_lbl.setAlignment(Qt.AlignCenter)
        capacity_lbl.setFont(QFont("Segoe UI", 8))
        capacity_lbl.setStyleSheet("color: #6366f1; font-style: italic;")

        # Select button
        self.select_btn = QPushButton("Select Room")
        self.select_btn.setFixedHeight(30)
        self.select_btn.setCursor(Qt.PointingHandCursor)
        self.select_btn.clicked.connect(self._on_select_clicked)

        layout.addWidget(emoji_lbl)
        layout.addWidget(name_lbl)
        layout.addWidget(price_lbl)
        layout.addWidget(desc_lbl)
        layout.addWidget(capacity_lbl)
        layout.addStretch()
        layout.addWidget(self.select_btn)

    def _on_select_clicked(self):
        """When button is clicked, emit signal to notify parent"""
        self.room_selected.emit(self._room_name, self._price, self._max_guests)

    def select(self):
        """Change to selected state (green border)"""
        self._is_selected = True
        self.setStyleSheet("""
            RoomCard {
                background-color: #f0fdf4;
                border: 2px solid #22c55e;
                border-radius: 12px;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
                font-weight: bold;
            }
        """)
        self.select_btn.setText("✓ Selected")

    def deselect(self):
        """Change back to normal state"""
        self._is_selected = False
        self.setStyleSheet("""
            RoomCard {
                background-color: #ffffff;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
            }
            RoomCard:hover {
                border: 2px solid #6366f1;
                background-color: #f5f3ff;
            }
        """)
        self.select_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 6px;
                padding: 5px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)
        self.select_btn.setText("Select Room")

    def is_selected(self):
        return self._is_selected


class ConfirmDialog(QDialog):
    """
    Booking confirmation popup — Custom Dialog Class
    """

    def __init__(self, guest_name: str, room_name: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Booking Confirmed")
        self.setFixedSize(360, 220)
        self.setModal(True)
        self._build_ui(guest_name, room_name)

    def _build_ui(self, guest_name: str, room_name: str):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(12)

        # Checkmark icon
        icon_lbl = QLabel("✅")
        icon_lbl.setAlignment(Qt.AlignCenter)
        icon_lbl.setFont(QFont("Segoe UI Emoji", 36))

        # Success title
        title_lbl = QLabel("Booking Successful!")
        title_lbl.setAlignment(Qt.AlignCenter)
        title_lbl.setFont(QFont("Segoe UI", 15, QFont.Bold))
        title_lbl.setStyleSheet("color: #16a34a;")

        # Message
        msg_lbl = QLabel(f"Dear {guest_name},\n{room_name} is ready to welcome you! 🎉")
        msg_lbl.setAlignment(Qt.AlignCenter)
        msg_lbl.setFont(QFont("Segoe UI", 10))
        msg_lbl.setStyleSheet("color: #374151;")
        msg_lbl.setWordWrap(True)

        # OK button
        ok_btn = QPushButton("OK")
        ok_btn.setFixedHeight(40)
        ok_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        ok_btn.setCursor(Qt.PointingHandCursor)
        ok_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover { background-color: #16a34a; }
        """)
        ok_btn.clicked.connect(self.accept)

        layout.addWidget(icon_lbl)
        layout.addWidget(title_lbl)
        layout.addWidget(msg_lbl)
        layout.addWidget(ok_btn)


# ─────────────────────────────────────────────
#  Page 1: Booking Page
# ─────────────────────────────────────────────
class BookingPage(QWidget):
    """
    Page 1 — Guest information form and room selection
    """

    def __init__(self):
        super().__init__()
        self.selected_room = None
        self.selected_price = 0
        self.cards = []
        self._build_ui()

    def _build_ui(self):
        scroll = QScrollArea(self)
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        container = QWidget()
        main_layout = QVBoxLayout(container)
        main_layout.setContentsMargins(30, 24, 30, 24)
        main_layout.setSpacing(20)

        # Title
        title = QLabel("🏨 Book Your Stay at CozyStay")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")

        subtitle = QLabel("Fill in your details and choose your room")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")

        main_layout.addWidget(title)
        main_layout.addWidget(subtitle)

        # ── Section 1: Guest Info Form ──
        form_title = QLabel("📋 Guest Information")
        form_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        form_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(form_title)

        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 10px;
            }
        """)

        # Create input widgets
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("e.g. John Smith")

        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("e.g. 081-234-5678")

        today = QDate.currentDate()
        tomorrow = today.addDays(1)

        self.checkin_input = QDateEdit()
        self.checkin_input.setDate(today)
        self.checkin_input.setDisplayFormat("dd/MM/yyyy")
        self.checkin_input.setCalendarPopup(True)
        self.checkin_input.setMinimumDate(today)

        self.checkout_input = QDateEdit()
        self.checkout_input.setDate(tomorrow)
        self.checkout_input.setDisplayFormat("dd/MM/yyyy")
        self.checkout_input.setCalendarPopup(True)
        self.checkout_input.setMinimumDate(tomorrow)

        self.guests_input = QSpinBox()
        self.guests_input.setMinimum(1)
        self.guests_input.setMaximum(10)
        self.guests_input.setValue(1)
        self.guests_input.setSuffix(" guest(s)")

        # Style inputs
        input_style = """
            QLineEdit, QDateEdit, QSpinBox {
                border: 1px solid #d1d5db;
                border-radius: 6px;
                padding: 6px 10px;
                font-size: 13px;
                background: white;
            }
            QLineEdit:focus, QDateEdit:focus, QSpinBox:focus {
                border: 1px solid #6366f1;
            }
        """
        for w in [self.name_input, self.phone_input,
                  self.checkin_input, self.checkout_input, self.guests_input]:
            w.setStyleSheet(input_style)
            w.setMinimumWidth(200)

        # Build form layout inside frame
        form_layout = QFormLayout(form_frame)
        form_layout.setContentsMargins(24, 20, 24, 20)
        form_layout.setSpacing(14)
        form_layout.setHorizontalSpacing(20)

        label_style = "font-size: 13px; color: #374151; font-weight: bold;"
        for text, widget in [
            ("Full Name :",       self.name_input),
            ("Phone Number :",    self.phone_input),
            ("Check-in Date :",   self.checkin_input),
            ("Check-out Date :",  self.checkout_input),
            ("Guests :",          self.guests_input),
        ]:
            lbl = QLabel(text)
            lbl.setStyleSheet(label_style)
            form_layout.addRow(lbl, widget)

        main_layout.addWidget(form_frame)

        # ── Section 2: Room Selection ──
        room_title = QLabel("🛏 Select a Room")
        room_title.setFont(QFont("Segoe UI", 12, QFont.Bold))
        room_title.setStyleSheet("color: #374151; margin-top: 8px;")
        main_layout.addWidget(room_title)

        rooms_data = [
            ("Standard Room", 50,  "Single bed, Free Wi-Fi",             "🛏",  2),
            ("Deluxe Room",   120, "Double bed, Ocean view, Wi-Fi",      "🌊",  4),
            ("Suite Room",    250, "Living room, Jacuzzi, Premium view", "👑",  10),
            ("Family Room",   160, "2 Bedrooms, Perfect for families",   "👨‍👩‍👧‍👦", 6),
        ]

        cards_layout = QHBoxLayout()
        cards_layout.setSpacing(14)
        cards_layout.setContentsMargins(0, 0, 0, 0)

        for room_name, price, desc, emoji, max_guests in rooms_data:
            card = RoomCard(room_name, price, desc, emoji, max_guests)
            card.room_selected.connect(self._on_room_selected)
            self.cards.append(card)
            cards_layout.addWidget(card)

        cards_layout.addStretch()
        main_layout.addLayout(cards_layout)

        # ── Buttons ──
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.clear_btn = QPushButton("🗑  Clear Info")
        self.clear_btn.setFixedHeight(42)
        self.clear_btn.setFont(QFont("Segoe UI", 11))
        self.clear_btn.setCursor(Qt.PointingHandCursor)
        self.clear_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 20px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)
        self.clear_btn.clicked.connect(self.clear_form)

        self.next_btn = QPushButton("Next  →")
        self.next_btn.setFixedHeight(42)
        self.next_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.next_btn.setCursor(Qt.PointingHandCursor)
        self.next_btn.setStyleSheet("""
            QPushButton {
                background-color: #6366f1;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #4f46e5; }
        """)

        btn_layout.addWidget(self.clear_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.next_btn)

        main_layout.addLayout(btn_layout)
        main_layout.addStretch()

        scroll.setWidget(container)

        page_layout = QVBoxLayout(self)
        page_layout.setContentsMargins(0, 0, 0, 0)
        page_layout.addWidget(scroll)

    def _on_room_selected(self, room_name: str, price: int, max_guests: int):
        """Receive signal from RoomCard, update state, deselect other cards"""
        self.selected_room = room_name
        self.selected_price = price

        # Clamp current guest value if it exceeds new room capacity
        self.guests_input.setMaximum(max_guests)
        if self.guests_input.value() > max_guests:
            self.guests_input.setValue(max_guests)

        for card in self.cards:
            if card._room_name == room_name:
                card.select()
            else:
                card.deselect()

    def clear_form(self):
        """Clear all form fields and deselect all room cards"""
        self.name_input.clear()
        self.phone_input.clear()

        today = QDate.currentDate()
        self.checkin_input.setDate(today)
        self.checkout_input.setDate(today.addDays(1))
        self.guests_input.setValue(1)

        self.selected_room = None
        self.selected_price = 0
        self.guests_input.setMaximum(10)
        self.guests_input.setValue(1)
        for card in self.cards:
            card.deselect()

    def get_booking_data(self):
        """Collect form data — returns None if validation fails"""
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()
        checkin = self.checkin_input.date()
        checkout = self.checkout_input.date()

        if not name:
            QMessageBox.warning(self, "Missing Information", "Please enter your full name.")
            return None
        if not phone:
            QMessageBox.warning(self, "Missing Information", "Please enter your phone number.")
            return None
        import re
        if not re.fullmatch(r'\d+', phone):
            msg = QMessageBox(self)
            msg.setWindowTitle("Invalid Phone Number")
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Please enter numbers only.")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.phone_input.setFocus()
            self.phone_input.selectAll()
            return None
        if checkin >= checkout:
            QMessageBox.warning(self, "Invalid Dates",
                                "Check-out date must be after check-in date.")
            return None
        if not self.selected_room:
            QMessageBox.warning(self, "No Room Selected",
                                "Please select a room before proceeding.")
            return None

        nights = checkin.daysTo(checkout)
        total = nights * self.selected_price

        data_dict = {
            "room":     self.selected_room,
            "price":    self.selected_price,
            "name":     name,
            "phone":    phone,
            "checkin":  checkin.toString("dd/MM/yyyy"),
            "checkout": checkout.toString("dd/MM/yyyy"),
            "nights":   nights,
            "guests":   self.guests_input.value(),
            "total":    total,
        }

        return data_dict


# ─────────────────────────────────────────────
#  PAGE 2: ReviewPage
# ─────────────────────────────────────────────
class ReviewPage(QWidget):
    """
    Page 2 — Review booking details before submitting
    """

    def __init__(self):
        super().__init__()
        self.current_data = {}
        self._build_ui()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(16)

        title = QLabel("📋 Booking Summary")
        title.setFont(QFont("Segoe UI", 18, QFont.Bold))
        title.setStyleSheet("color: #1e1b4b;")

        subtitle = QLabel("Please review your details before confirming")
        subtitle.setFont(QFont("Segoe UI", 10))
        subtitle.setStyleSheet("color: #6b7280;")

        layout.addWidget(title)
        layout.addWidget(subtitle)

        self.info_frame = QFrame()
        self.info_frame.setStyleSheet("""
            QFrame {
                background-color: #f9fafb;
                border-radius: 12px;
            }
        """)

        self.info_layout = QGridLayout(self.info_frame)
        self.info_layout.setContentsMargins(28, 22, 28, 22)
        self.info_layout.setSpacing(12)
        self.info_layout.setColumnStretch(1, 1)

        key_style = "font-weight: bold; color: #374151; font-size: 13px;"
        val_style = "color: #1f2937; font-size: 13px;"

        display_rows = [
            ("🛏  Room",            "room"),
            ("💰  Price / Night",   "price"),
            ("👤  Guest Name",      "name"),
            ("📞  Phone",           "phone"),
            ("📅  Check-in",        "checkin"),
            ("📅  Check-out",       "checkout"),
            ("🌙  Nights",          "nights"),
            ("👥  Guests",          "guests"),
        ]

        self._value_labels = {}

        for row, (label_text, key) in enumerate(display_rows):
            key_lbl = QLabel(label_text)
            key_lbl.setStyleSheet(key_style)

            val_lbl = QLabel("—")
            val_lbl.setStyleSheet(val_style)

            self.info_layout.addWidget(key_lbl, row, 0)
            self.info_layout.addWidget(val_lbl, row, 1)
            self._value_labels[key] = val_lbl

        layout.addWidget(self.info_frame)

        # Horizontal line
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setStyleSheet("color: #e5e7eb;")
        layout.addWidget(line)

        # Total amount label
        total_layout = QHBoxLayout()
        total_layout.addStretch()
        total_icon = QLabel("💳")
        total_icon.setFont(QFont("Segoe UI Emoji", 14))
        self.total_lbl = QLabel("Total Amount:  $—")
        self.total_lbl.setFont(QFont("Segoe UI", 15, QFont.Bold))
        self.total_lbl.setStyleSheet("color: #1e1b4b;")
        total_layout.addWidget(total_icon)
        total_layout.addWidget(self.total_lbl)
        layout.addLayout(total_layout)

        layout.addStretch()

        # Buttons
        btn_layout = QHBoxLayout()
        btn_layout.setSpacing(12)

        self.back_btn = QPushButton("←  Back")
        self.back_btn.setFixedHeight(44)
        self.back_btn.setFont(QFont("Segoe UI", 11))
        self.back_btn.setCursor(Qt.PointingHandCursor)
        self.back_btn.setStyleSheet("""
            QPushButton {
                background-color: #f3f4f6;
                color: #374151;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                padding: 0 22px;
            }
            QPushButton:hover { background-color: #e5e7eb; }
        """)

        self.submit_btn = QPushButton("✅  Confirm Booking")
        self.submit_btn.setFixedHeight(44)
        self.submit_btn.setFont(QFont("Segoe UI", 11, QFont.Bold))
        self.submit_btn.setCursor(Qt.PointingHandCursor)
        self.submit_btn.setStyleSheet("""
            QPushButton {
                background-color: #22c55e;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 0 28px;
            }
            QPushButton:hover { background-color: #16a34a; }
        """)

        btn_layout.addWidget(self.back_btn)
        btn_layout.addStretch()
        btn_layout.addWidget(self.submit_btn)
        layout.addLayout(btn_layout)

    def load_data(self, data: dict):
        """Receive data dict from BookingPage and populate the review layout"""
        self.current_data = data

        self._value_labels["room"].setText(data.get("room", "—"))
        self._value_labels["price"].setText(f"${data.get('price', 0)}")
        self._value_labels["name"].setText(data.get("name", "—"))
        self._value_labels["phone"].setText(data.get("phone", "—"))
        self._value_labels["checkin"].setText(data.get("checkin", "—"))
        self._value_labels["checkout"].setText(data.get("checkout", "—"))
        self._value_labels["nights"].setText(f"{data.get('nights', 0)} night(s)")
        self._value_labels["guests"].setText(f"{data.get('guests', 0)} guest(s)")

        total = data.get("total", 0)
        self.total_lbl.setText(f"Total Amount:  ${total}")


class MainWindow(QMainWindow):
    """
    Main window — uses QStackedWidget to manage 2 pages
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("CozyStay — Hotel Booking System")
        self.setMinimumSize(820, 680)
        self.resize(900, 720)

        # QStackedWidget as central widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # Create pages
        self.booking_page = BookingPage()
        self.review_page = ReviewPage()

        # Add to stack: index 0 = booking, index 1 = review
        self.stack.addWidget(self.booking_page)   # index 0
        self.stack.addWidget(self.review_page)    # index 1

        # Connect navigation
        self.booking_page.next_btn.clicked.connect(self._go_to_review)
        self.review_page.back_btn.clicked.connect(self._go_to_booking)
        self.review_page.submit_btn.clicked.connect(self._on_submit)

        # Start on page 0
        self.stack.setCurrentIndex(0)

        self.setStyleSheet("""
            QMainWindow { background-color: #f0f0ff; }
            QScrollArea  { background-color: transparent; }
            QWidget      { font-family: 'Segoe UI', 'Tahoma', sans-serif; }
        """)

    def _go_to_review(self):
        """Validate form, then switch to Review page"""
        data = self.booking_page.get_booking_data()

        if data is None:
            return

        self.review_page.load_data(data)
        self.stack.setCurrentIndex(1)

    def _go_to_booking(self):
        """Go back to Booking page, form data remains intact"""
        self.stack.setCurrentIndex(0)

    def _on_submit(self):
        """Show ConfirmDialog, then reset the entire app"""
        name = self.review_page.current_data.get("name", "Guest")
        room = self.review_page.current_data.get("room", "Room")

        dialog = ConfirmDialog(name, room, parent=self)
        dialog.exec()

        # Clear booking page and return to it
        self.booking_page.clear_form()
        self.stack.setCurrentIndex(0)


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.styleHints().setColorScheme(Qt.ColorScheme.Light)


    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()