from typing import Union
import numpy as np
import cv2
import json

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)


############################################
def detect_edges(data: dict, image: Union[str, np.ndarray]) -> np.ndarray:
    """Detect edges in an image using the Canny edge detection algorithm.

    Parameters
    ----------
    data: dict :
        Extra arguments to `cv2.Canny`: Possible arguments include
        'canny_lower_threshold', and 'canny_upper_threshold'.
        Please refer to the `cv2.Canny` documentation for more information.
    image: Union[str : Image file path.
                 np.ndarray] : Image array.
        

    Returns
    -------
    np.ndarray
        Image with detected edges.

    """
    if isinstance(image, str):
        image = cv2.imread(image)
    #print("Shape of image into edge detection: ", image.shape)
    # Convert the image to grayscale if it is not already
    if len(image.shape) > 2:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(image, data['canny_lower_threshold'], data['canny_upper_threshold'])
    #print("Shape of edge map: ", edges.shape)
    return edges

############################################
