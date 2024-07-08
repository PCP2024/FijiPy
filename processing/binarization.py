from typing import Union
import numpy as np
import cv2
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from configuration.config_utils import THRESHOLD_TYPE_MAP

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)


############################################
def binarize_image(data: dict, image: Union[str, np.ndarray]) -> np.ndarray:
    """Binarize an image using a thresholding method from cv2.
    thresholding hyperparameters can be adjusted in the data json file.
    hyperparameters include
    threshold_value: range 0-255. value at which the thresholding is applied. values higher than threshold value are set to max_value, values lower than threshold value are set to 0.
    max_value: range 0-255. value to set the pixel to if the pixel value is higher than the threshold value.
    threshold_type: thresholding type/algortihm. choose from ["THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV", "THRESH_MASK", "THRESH_OTSU", "THRESH_TRIANGLE", "THRESH_BINARY_OTSU"]

    Parameters
    ----------
    data: dict :
        Extra arguments to `cv2.threshold`: Possible arguments include
        'threshold_value', 'max_value', and 'threshold_type'.
        Please refer to the `cv2.threshold` documentation for more information.
    image: Union[str : Image file path.

                 np.ndarray] : Image array.

    Returns
    -------
    np.ndarray
        Binarized image.

    """
    if isinstance(image, str):
        image = cv2.imread(image)
    #print("Shape of image into binarization: ", image.shape)
    # Convert the image to grayscale if it is not already
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load hyperparameters from data json file
    threshold_value = data['threshold_value']
    max_value = data['max_value']
    threshold_type_str = data['threshold_type']
    threshold_type = THRESHOLD_TYPE_MAP[threshold_type_str]
    
    # Apply Otsu thresholding
    _, binary_image = cv2.threshold(image, threshold_value, max_value, threshold_type)
    #print("Shape of binarized image: ", binary_image.shape)
    return binary_image

############################################
