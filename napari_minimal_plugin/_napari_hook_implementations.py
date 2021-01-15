# Implementation of napari hooks according to
# https://napari.org/docs/dev/plugins/for_plugin_developers.html#plugins-hook-spec

from napari_plugin_engine import napari_hook_implementation
from ._my_widget import MyWidget
from ._my_function import my_function

@napari_hook_implementation
def napari_experimental_provide_dock_widget():
    return MyWidget

@napari_hook_implementation
def napari_experimental_provide_function_widget():
    return my_function
