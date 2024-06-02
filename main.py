import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

from gui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Widget and Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)


app = QApplication(sys.argv)
window = MainWindow()
window.showMaximized()
sys.exit(app.exec())
