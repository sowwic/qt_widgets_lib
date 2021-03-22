from PySide2 import QtWidgets


class TimeRangeWidget(QtWidgets.QGroupBox):
    def __init__(self, parent=None, title="Time", mode=0, start_time=0, end_time=120, max_time=9999, min_time=-9999):
        super(TimeRangeWidget, self).__init__(title, parent)

        # Widgets
        self.timeslider_radio = QtWidgets.QRadioButton("Time slider")
        self.startend_radio = QtWidgets.QRadioButton("Start/end")
        self.timeslider_radio.setChecked(mode)
        self.startend_radio.setChecked(not mode)

        self.start_label = QtWidgets.QLabel("Start:")
        self.start_time = QtWidgets.QSpinBox()
        self.start_time.setMinimumWidth(50)
        self.start_time.setMinimum(min_time)
        self.start_time.setMaximum(max_time)
        self.start_time.setValue(start_time)
        self.start_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.end_label = QtWidgets.QLabel("End:")
        self.end_time = QtWidgets.QSpinBox()
        self.end_time.setMinimumWidth(50)
        self.end_time.setMinimum(min_time)
        self.end_time.setMaximum(max_time)
        self.end_time.setValue(end_time)
        self.end_time.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)

        # Layouts
        self.radio_layout = QtWidgets.QHBoxLayout()
        self.radio_layout.addWidget(QtWidgets.QLabel("Range:"))
        self.radio_layout.addWidget(self.timeslider_radio)
        self.radio_layout.addWidget(self.startend_radio)
        self.radio_layout.addStretch()
        self.time_range_layout = QtWidgets.QHBoxLayout()
        self.time_range_layout.addWidget(self.start_label)
        self.time_range_layout.addWidget(self.start_time)
        self.time_range_layout.addWidget(self.end_label)
        self.time_range_layout.addWidget(self.end_time)
        self.time_range_layout.addStretch()
        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addLayout(self.radio_layout)
        self.main_layout.addLayout(self.time_range_layout)
        self.setLayout(self.main_layout)

        # Connections
        self.startend_radio.toggled.connect(self.set_spinboxes_enabled)
