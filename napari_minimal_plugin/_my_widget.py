from qtpy.QtWidgets import QWidget, QGridLayout, QPushButton


class MyWidget(QWidget):
    def __init__(self, napari_viewer):
        super().__init__()

        # initialize layout
        layout = QGridLayout()

        # add a button
        btn = QPushButton('Click me!', self)
        def trigger():
            print("napari has", len(napari_viewer.layers), "layers")
        btn.clicked.connect(trigger)
        layout.addWidget(btn)

        # activate layout
        self.setLayout(layout)
