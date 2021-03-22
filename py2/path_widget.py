from PySide2 import QtWidgets
from PySide2 import QtGui


class PathWidget(QtWidgets.QWidget):

    def __init__(self, parent=None, mode="dir", default_path="", label_text="", dialog_label=""):
        super(PathWidget, self).__init__(parent)
        self.mode = mode
        self.default_path = default_path
        self.label_text = label_text
        self.dialog_label = dialog_label

        self._create_widgets()
        self._create_layouts()
        self._create_connections()

    def _create_widgets(self):
        self.label = QtWidgets.QLabel(self.label_text)
        self.line_edit = QtWidgets.QLineEdit(self.default_path)
        self.browse_button = QtWidgets.QPushButton()
        self.browse_button.setIcon(QtGui.QIcon(":fileOpen.png"))

    def _create_layouts(self):
        self.main_layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.addWidget(self.label)
        self.main_layout.addWidget(self.line_edit)
        self.main_layout.addWidget(self.browse_button)

    def _create_connections(self):
        self.browse_button.clicked.connect(self.get_path)

    def get_path(self):
        if self.mode == "dir":
            self._get_existing_dir()
        elif self.mode == "file":
            self._get_existing_file()
        elif self.mode == "save_file":
            self._get_save_file()

    def _get_save_file(self):
        if not self.dialog_label:
            self.dialog_label = "Select save file"
        path = QtWidgets.QFileDialog.getSaveFileName(None, self.dialog_label, self.line_edit.text())
        if path:
            self.line_edit.setText(path)

    def _get_existing_file(self):
        if not self.dialog_label:
            self.dialog_label = "Select existing file"
        path, extra = QtWidgets.QFileDialog.getOpenFileName(None, self.dialog_label, self.line_edit.text())
        if path:
            self.line_edit.setText(path)

    def _get_existing_dir(self):
        if not self.dialog_label:
            self.dialog_label = "Set directory"
        path = QtWidgets.QFileDialog.getExistingDirectory(None, self.dialog_label, self.line_edit.text())
        if path:
            self.line_edit.setText(path)

    def add_widget(self, widget):
        self.main_layout.addWidget(widget)
