from PySide2 import QtWidgets


class ItemsListGroup(QtWidgets.QGroupBox):
    def __init__(self, title="", add_icon="", delete_icon="", parent=None):
        super(ItemsListGroup, self).__init__(title, parent)
        self.add_icon = add_icon
        self.delete_icon = delete_icon

        self.create_widgets()
        self.create_layouts()
        self.create_connections()

    def create_widgets(self):
        self.list = QtWidgets.QListWidget()
        if self.add_icon:
            self.add_button = QtWidgets.QPushButton(self.add_icon, "")
        else:
            self.add_button = QtWidgets.QPushButton("+")
        if self.delete_icon:
            self.delete_button = QtWidgets.QPushButton(self.delete_icon, "")
        else:
            self.delete_button = QtWidgets.QPushButton("-")

    def create_layouts(self):
        self.buttons_layout = QtWidgets.QHBoxLayout()
        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.add_button)
        self.buttons_layout.addWidget(self.delete_button)

        self.main_layout = QtWidgets.QVBoxLayout()
        self.main_layout.addWidget(self.list)
        self.main_layout.addLayout(self.buttons_layout)
        self.setLayout(self.main_layout)

    def create_connections(self):
        pass
