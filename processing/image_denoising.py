import numpy as np
import cv2
import json

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

############################################
def median_filter(image, kernel_size):
    """
    Apply median filtering to the input image.

    Args:
        image (ndarray): Input image.
        kernel_size (int): Size of the median filter kernel.

    Returns:
        ndarray: Denoised image.
    """
    denoised_image = cv2.medianBlur(image, kernel_size)
    return denoised_image

def gaussian_filter(image, kernel_size, sigma):
    """
    Apply Gaussian filtering to the input image.

    Args:
        image (ndarray): Input image.
        sigma (float): Standard deviation of the Gaussian kernel.

    Returns:
        ndarray: Denoised image.
    """
    # Store the original shape of the image
    original_shape = image.shape

    # Convert the image to grayscale for filtering
    if len(image.shape) == 3:
        grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        grayscale_image = image

    # Apply Gaussian filter
    denoised_grayscale_image = cv2.GaussianBlur(grayscale_image, kernel_size, sigma)

    # Convert the denoised grayscale image back to the original color format
    if len(original_shape) == 3:
        denoised_image = cv2.cvtColor(denoised_grayscale_image, cv2.COLOR_GRAY2BGR)
    else:
        denoised_image = denoised_grayscale_image

    return denoised_image

############################################
def denoise_image(image, algorithm='median'):
    """
    Denoise an image using the specified algorithm.

    Args:
        image (ndarray): Name of image loaded with the loader module.
        algorithm (str): Denoising algorithm to use.
        algorithm specific parameters are passed through the config file (e.g.: kernel_sie,sigma)

    Returns:
        ndarray: Denoised image.
    """

    # Apply the selected denoising algorithm
    if algorithm == 'median':
        denoised_image = median_filter(image, data['kernel_size'])
    elif algorithm == 'gaussian':
        denoised_image = gaussian_filter(image, data['kernel_size'], data['sigma'])

    return denoised_image