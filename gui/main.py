from PySide6.QtGui import QAction, Qt
from PySide6.QtWidgets import *


class Label(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)


class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)


class SelectionButton(Button):
    def __init__(self, text, parent=None, window=None, show_kwargs=None, change_text_of=False):
        """
        :param text:
        :param parent:
        :param window:
        :param change_text_of: None for none, False for self. This object will have its text changed
                                to whatever the selection window returns
        """

        super().__init__(text, parent)

        self.window_to_show = window
        if not show_kwargs:
            show_kwargs = {}
        self.show_kwargs = show_kwargs

        if change_text_of is False:
            change_text_of = self

        self.change_text_of = change_text_of
        self.default = text
        self.clicked.connect(self.onClick)

    def onClick(self):
        if self.window_to_show:
            print(self.show_kwargs)
            self.window_to_show.show(**self.show_kwargs)
            self.window_to_show.closeEvent = self.window_closed

    def window_closed(self, event):
        if self.window_to_show and self.change_text_of is not None:
            v = self.window_to_show.selection

            if self.change_text_of is False:
                self.setText(v)

            else:
                self.change_text_of.setText(v)


class LineEdit(QLineEdit):
    def __init__(self, parent=None, readonly=False, value=None):
        super().__init__(parent=parent)

        self.setReadOnly(readonly)

        if value:
            self.default = value
            self.setText(value)


class ComboBox(QComboBox):
    def __init__(self, items, parent=None):
        super().__init__(parent=parent)

        self.addItems(items)


class CheckBox(QCheckBox):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)


class RadioButton(QRadioButton):
    def __init__(self, text, parent=None):
        super().__init__(text=text, parent=parent)


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


class Slider(QSlider):
    def __init__(self, parent=None, orientation=None, interval=None, position=None):
        super().__init__(parent=parent)

        if orientation:
            self.setOrientation(orientation)

        if interval:
            self.setTickInterval(interval)

        if position:
            self.setSliderPosition(position)


class DoubleSpinBox(QDoubleSpinBox):
    def __init__(self, parent=None, _max=None, _min=None, step=None, value=None, readonly=False, buttons=True):
        super().__init__(parent=parent)

        if _max:
            self.setMaximum(_max)

        if _min:
            self.setMinimum(_min)

        if step:
            self.setSingleStep(step)

        if value:
            self.default = value
            self.setValue(value)

        self.showButtons = buttons
        self.setReadOnly(readonly)

    def setReadOnly(self, r):
        if r:
            self.setStyleSheet(
                "QSpinBox::up-button { width: 0; height: 0; }"
                "QSpinBox::down-button { width: 0; height: 0; }"
            )

        elif self.showButtons:
            self.setStyleSheet("")

        super().setReadOnly(r)


class SpinBox(QSpinBox):
    def __init__(self, parent=None, _max=None, _min=None, step=None, value=None, readonly=False, buttons=True):
        super().__init__(parent=parent)

        if _max:
            self.setMaximum(_max)

        if _min:
            self.setMinimum(_min)

        if step:
            self.setSingleStep(step)

        if value:
            self.default = value
            self.setValue(value)

        self.showButtons = buttons
        self.setReadOnly(readonly)

    def setReadOnly(self, r):
        if r:
            self.setStyleSheet(
                "QSpinBox::up-button { width: 0; height: 0; }"
                "QSpinBox::down-button { width: 0; height: 0; }"
            )

        elif self.showButtons:
            self.setStyleSheet("")

        super().setReadOnly(r)


class ProgressBar(QProgressBar):
    def __init__(self, parent=None, orientation=None, _max=None, _min=None):
        super().__init__(parent=parent)

        if orientation:
            self.setOrientation(orientation)

        if _max:
            self.setMaximum(_max)

        if _min:
            self.setMinimum(_min)


class Table(QTableWidget):
    def  __init__(self, rows, columns, parent=None, readonly=False):
        super().__init__(parent=parent)

        self.setRowCount(rows)
        self.setColumnCount(columns)

        if readonly:
            self.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)


class Toolbar(QToolBar):
    def __init__(self, title, parent=None, orientation=None, floatable=None):
        super().__init__(parent=parent)

        if parent:
            parent.addToolBar(self)

        if orientation:
            self.setOrientation(orientation)

        if floatable:
            self.setFloatable(floatable)

        self.setWindowTitle(title)


class Action(QAction):
    def __init__(self, text=None, parent=None, icon=None, tooltip=None, command=None):
        super().__init__(parent=parent)

        if text:
            self.setText(text)

        if icon:
            self.setIcon(icon)

        if command:
            self.triggered.connect(command)

        if tooltip:
            self.setToolTip(tooltip)


class GroupBox(QGroupBox):
    def __init__(self, title, parent=None):
        super().__init__()

        self.setTitle(title)


class ListWidget(QListWidget):
    def __init__(self, items=None, parent=None):
        super().__init__(parent)

        if items and len(items) > 0:
            for item in items:
                QListWidgetItem(item, self)
