from PySide2 import QtWidgets


class ScrollWidget(QtWidgets.QWidget):
    def __init__(self, border=0, **kwargs):
        super(ScrollWidget, self).__init__(**kwargs)

        self.content = QtWidgets.QWidget(self)
        self.scroll_area = QtWidgets.QScrollArea()

        self.scroll_area.setWidget(self.content)
        self.scroll_area.setWidgetResizable(1)

        self.content_layout = QtWidgets.QVBoxLayout()
        self.content.setLayout(self.content_layout)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.layout().addWidget(self.scroll_area)
        self.layout().setContentsMargins(0, 0, 0, 0)

        if not border:
            self.scroll_area.setFrameShape(QtWidgets.QFrame.NoFrame)

    def add_widget(self, widget):
        self.content_layout.addWidget(widget)

    def add_layout(self, layout):
        self.content_layout.addLayout(layout)

    def resizeEvent(self, e):
        self.scroll_area.resizeEvent(e)
