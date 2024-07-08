import json
import os
from typing import Union
import cv2
import numpy as np

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)


def crop_image(data: dict, image: Union[str, np.ndarray]) -> np.ndarray:
    """Crop image into a desired size.

    Parameters
    ----------
    data: dict :
        Extra arguments of type `int` for cropping procedure: Possible arguments include
        'crop_width', 'crop_height', 'crop_x', and 'crop_y'. The latter two arguments specify the index
        at which the cropped image starts in each dimension. The former two arguments dictate the shape of
        the resulting image.
    image: Union[str : Image file path.

                 np.ndarray] : Image array.

    Returns
    -------
    np.ndarray
        Cropped image.

    """
    # either load the image from the path or use the image array
    if isinstance(image, str):
        image = cv2.imread(image)

    # Load hyperparameters from data json file
    crop_width = data['crop_width']
    crop_height = data['crop_height']
    crop_x = data['crop_x']
    crop_y = data['crop_y']

    if image.shape[0] < crop_height or image.shape[1] < crop_width:
        raise ValueError("The crop region is larger than the image.")
    if image.shape[0] < crop_height + crop_y or image.shape[1] < crop_width + crop_x:
        raise ValueError("The crop region is out of the image.")
            
    # Crop the image
    cropped_image = image[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]
    return cropped_image