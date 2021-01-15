from napari.types import ImageData

def my_function(image : ImageData) -> 'napari.types.LayerDataTuple':

    # process the image
    result = -image

    # return it + some layer properties
    return result, {'colormap':'turbo'}