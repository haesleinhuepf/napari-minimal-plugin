from qtpy.QtWidgets import QWidget, QGridLayout, QPushButton


class MyWidget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()

        # initialize layout
        self.layout = QGridLayout()

        # text
        btn = QPushButton('Click me!', self)

        def trigger():
            print("Hello world!\nnapari has ", len(napari_viewer.layers), " layers")

        # action
        btn.clicked.connect(trigger)

        self.layout.addWidget(btn)

        # activate layout
        self.setLayout(self.layout)