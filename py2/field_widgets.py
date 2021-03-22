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
    def __init__(self,
                 label_text,
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


class SliderFieldWidget(QtWidgets.QWidget):
    def __init__(self,
                 data_type="int",
                 label_text="label",
                 min_value=0.0,
                 max_value=1.0,
                 default_value=1.0,
                 step=1.0,
                 slider_multiplier=1.0,
                 parent=None):
        super(SliderFieldWidget, self).__init__(parent)
        # Properties
        self.data_type = data_type
        self.setMinimumSize(100, 40)

        # Build components
        self.create_widgets()
        self.create_layouts()
        self.create_connections()

        # Set values
        self.slide_multiplier = slider_multiplier
        self.label_text = label_text
        self.min_value = min_value
        self.max_value = max_value
        self.step = step

        if data_type == "float":
            default_value = float(default_value)
        elif data_type == "int":
            default_value = int(default_value)
        self.spin_box.setValue(default_value)

    @property
    def label_text(self):
        return self._label_text

    @label_text.setter
    def label_text(self, text):
        self._label_text = str(text)
        self.label.setText(str(text))

    @property
    def min_value(self):
        return self._min_value

    @min_value.setter
    def min_value(self, value):
        self._min_value = value
        self.spin_box.setMinimum(value)
        self.slider.setMinimum(value * self.slide_multiplier)

    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, value):
        self._max_value = value
        self.spin_box.setMaximum(value)
        self.slider.setMaximum(value * self.slide_multiplier)

    @property
    def step(self):
        return self._step

    @step.setter
    def step(self, value):
        self._step = value
        self.spin_box.setSingleStep(value)

    @property
    def value(self):
        return self.get_value()

    def set_value(self, value):
        self.spin_box.setValue(value)

    def get_value(self):
        return self.spin_box.value()

    def create_widgets(self):
        if self.data_type == "float":
            self.spin_box = QtWidgets.QDoubleSpinBox()
        elif self.data_type == "int":
            self.spin_box = QtWidgets.QSpinBox()
        self.spin_box.setMinimumWidth(40)
        self.label = QtWidgets.QLabel()
        self.spin_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Horizontal)

    def create_layouts(self):
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.addWidget(self.label, 0, 0)
        self.main_layout.addWidget(self.spin_box, 0, 1)
        self.main_layout.addWidget(self.slider, 0, 2)
        self.main_layout.setColumnMinimumWidth(0, 90)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_layout)

    def create_connections(self):
        self.spin_box.valueChanged.connect(self._update_slider_value)
        self.slider.valueChanged.connect(self._update_field_value)

    @QtCore.Slot()
    def _update_field_value(self, value):
        self.spin_box.setValue(value / self.slide_multiplier)

    @QtCore.Slot()
    def _update_slider_value(self, value):
        self.slider.setValue(value * self.slide_multiplier)
