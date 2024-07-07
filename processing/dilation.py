from configuration.config_utils import STRUCTURING_ELEMENT_TYPE_MAP
import cv2
import json
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

############################################
def dilate_image(data: dict,image):
    """
    Dilate an image using a structuring element of the specified size.

    Args:
        image (ndarray or str): Input image as ndarray or image path.
        kernel_size (tuple, optional): Size of the structuring element.
        iterations (int, optional): Number of times to apply the dilation.

    Returns:
        ndarray: Dilated image.
    """
    if isinstance(image, str):
        image = cv2.imread(image)
    
    kernel_size = data['structuring_element_size']
    iterations = data['dilation_iterations']

    structuring_element_type = data['structuring_element_type']
    structuring_element = cv2.getStructuringElement(STRUCTURING_ELEMENT_TYPE_MAP[structuring_element_type], kernel_size)
    dilated_image = cv2.dilate(image, structuring_element, iterations=iterations)
    return dilated_image

############################################

