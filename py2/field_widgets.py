from PySide2 import QtCore
from PySide2 import QtWidgets


class StringFieldWidget(QtWidgets.QWidget):
    def __init__(self, label_text, button=True, button_text="", parent=None):
        super(StringFieldWidget, self).__init__(parent)
        self.label = QtWidgets.QLabel(label_text)
        self.line_edit = QtWidgets.QLineEdit()
        self.button = None  # type: QtWidgets.QPushButton

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        if button:
            self.button = QtWidgets.QPushButton(button_text)
            self.main_layout.addWidget(self.button)

        self.setLayout(self.main_layout)

    def text(self):
        return self.line_edit.text()


class NumericFieldWidget(QtWidgets.QWidget):
    def __init__(self, label_text,
                 button=False,
                 data_type="int",
                 default_value=0.0,
                 min_value=-1000.0,
                 max_value=1000.0,
                 button_text="",
                 spinbox_symbols=False,
                 parent=None):
        super(NumericFieldWidget, self).__init__(parent)
        self.label = QtWidgets.QLabel(label_text)
        self.button = None
        if data_type == "int":
            self.spin_box = QtWidgets.QSpinBox()
        elif data_type in ["double", "float"]:
            self.spin_box = QtWidgets.QDoubleSpinBox()
        self.spin_box.setValue(default_value)
        self.spin_box.setMinimum(min_value)
        self.spin_box.setMaximum(max_value)

        if not spinbox_symbols:
            self.spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        self.main_layout = QtWidgets.QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.spin_box)
        self.main_layout.setAlignment(QtCore.Qt.AlignLeft)
        if button:
            self.button = QtWidgets.QPushButton(button_text)
            self.main_layout.addWidget(self.button)

        self.setLayout(self.main_layout)

    def value(self):
        return self.spin_box.value()

    def set_value(self, value):
        self.spin_box.setValue(value)
