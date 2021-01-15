from napari.types import ImageData, LayerDataTuple

def my_function(image : ImageData) -> LayerDataTuple:

    # process the image
    result = -image

    # return it + some layer properties
    return result, {'colormap':'turbo'}