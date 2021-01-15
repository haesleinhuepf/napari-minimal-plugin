import napari
import numpy as np

# create Qt GUI context
with napari.gui_qt():
    # start napari
    viewer = napari.Viewer()

    viewer.add_image(np.random.random((512,512)))
