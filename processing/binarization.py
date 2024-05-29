import cv2
import json
from configuration.config_utils import THRESHOLD_TYPE_MAP
# # TODO: Move this to a configuration file and figure out how to load it.
# THRESHOLD_TYPE_MAP = {
#     "THRESH_BINARY": cv2.THRESH_BINARY,
#     "THRESH_BINARY_INV": cv2.THRESH_BINARY_INV,
#     "THRESH_TRUNC": cv2.THRESH_TRUNC,
#     "THRESH_TOZERO": cv2.THRESH_TOZERO,
#     "THRESH_TOZERO_INV": cv2.THRESH_TOZERO_INV,
#     "THRESH_MASK": cv2.THRESH_MASK,
#     "THRESH_OTSU": cv2.THRESH_OTSU,
#     "THRESH_TRIANGLE": cv2.THRESH_TRIANGLE,
#     "THRESH_BINARY_OTSU": cv2.THRESH_BINARY + cv2.THRESH_OTSU  # Otsu's thresholding with binary thresholding
# }


with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

############################################
def binarize_image(image_path=None, image=None, threshold_value=None, max_value=None, threshold_type=None):
    """
    Binarize an image using a thresholding method from cv2.
    thresholding hyperparameters can be adjusted in the data json file.
    hyperparameters include
    threshold_value: range 0-255. value at which the thresholding is applied. values higher than threshold value are set to max_value, values lower than threshold value are set to 0.
    max_value: range 0-255. value to set the pixel to if the pixel value is higher than the threshold value.
    threshold_type: thresholding type/algortihm. choose from ["THRESH_BINARY", "THRESH_BINARY_INV", "THRESH_TRUNC", "THRESH_TOZERO", "THRESH_TOZERO_INV", "THRESH_MASK", "THRESH_OTSU", "THRESH_TRIANGLE", "THRESH_BINARY_OTSU"]

    Args:
        image_path (str, optional): Path to the image file.
        image (ndarray, optional): Image array.
        threshold_value (int, optional): Threshold value.
        max_value (int, optional): Max value.
        threshold_type (int, optional): Threshold type.

    Returns:
        ndarray: Binarized image.
    """
    if image_path is not None:
        # Load the image
        image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Load hyperparameters from data json file if not specified
    if threshold_value is None:
        threshold_value = data['threshold_value']
    if max_value is None:
        max_value = data['max_value']
    if threshold_type is None:
        threshold_type_str = data['threshold_type']
        threshold_type = THRESHOLD_TYPE_MAP[threshold_type_str]
    
    # Apply Otsu thresholding
    _, binary_image = cv2.threshold(grayscale_image, threshold_value, max_value, threshold_type)

    return binary_image

############################################
# test the function above
image_path = 'demodata\demo_Image.jpg'
binary_image = binarize_image(image_path=image_path)
cv2.imwrite('demodata\demo_Image_binary.jpg', binary_image)