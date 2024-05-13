import numpy as np
import cv2
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

############################################
def detect_edges(image_path=None, image=None):
    """
    Detect edges in an image using the Canny edge detection algorithm.

    Args:
        image_path (str, optional): Path to the image file.
        image (ndarray, optional): Input image.

    Returns:
        ndarray: Image with detected edges.
    """
    if image_path is not None:
        # Load the image
        image = cv2.imread(image_path)

    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(grayscale_image, data['canny_lower_threshold'], data['canny_upper_threshold'])

    return edges

############################################
# test the function above
image_path = 'demodata\demo_Image.jpg'
edges = detect_edges(image_path=image_path)
cv2.imwrite('demodata\demo_Image_edges.jpg', edges)