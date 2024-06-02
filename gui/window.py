from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout, QScrollArea, QVBoxLayout, QWidget


class Window(QWidget):
    def __init__(self, title, main_window, parent=None):
        super().__init__(parent)

        self.main_window = main_window

        self.setWindowTitle(title)

        self.main_layout = QVBoxLayout(self)
        self.setLayout(self.main_layout)

        self.scrollArea = QScrollArea()
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.scrollAreaContents = QWidget()
        self.scrollArea.setWidget(self.scrollAreaContents)
        self.scrollArea.setWidgetResizable(True)

        self._layout = la = QGridLayout(self.scrollAreaContents)
        self.scrollAreaContents.setLayout(la)

        self.main_layout.addWidget(self.scrollArea)
