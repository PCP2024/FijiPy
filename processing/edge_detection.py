import numpy as np
import cv2
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

############################################
def detect_edges(data: dict,image):
    """
    Detect edges in an image using the Canny edge detection algorithm.

    Args:
        image_path (str, optional): Path to the image file.
        image (ndarray, optional): Input image.

    Returns:
        ndarray: Image with detected edges.
    """
    if isinstance(image, str):
        image = cv2.imread(image)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(grayscale_image, data['canny_lower_threshold'], data['canny_upper_threshold'])

    return edges

############################################
