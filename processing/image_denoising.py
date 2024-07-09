import numpy as np
import cv2
import json
import os
import sys
from typing import Union

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)


############################################
def median_filter(image: np.ndarray, kernel_size: int) -> np.ndarray:
    """Apply median filtering to the input image.

    Parameters
    ----------
    image : np.ndarray :
        Input image.
    kernel_size : int :
        Size of the median filter kernel.
        

    Returns
    -------
    np.ndarray
        Denoised image.

    """
    denoised_image = cv2.medianBlur(image, kernel_size)
    return denoised_image


def gaussian_filter(image: np.ndarray, kernel_size: int, sigma: float) -> np.ndarray:
    """Apply Gaussian filtering to the input image.

    Parameters
    ----------
    image : np.ndarray :
        Input image.
    kernel_size : int :
        Size of the Gaussian filter kernel.
    sigma : float
        Standard deviation of the Gaussian kernel.
        

    Returns
    -------
    np.ndarray
        Denoised image.

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
def denoise_image(data: dict, image: Union[str, np.ndarray]) -> np.ndarray:
    """Denoise an image using the specified algorithm.

    Parameters
    ----------
    data: dict :
        Extra arguments for the denoising procedure: Possible arguments include
        'denoising_algorithm' (one of "median" or "gaussian"), 'kernel_size_median',
        'kernel_size_gaussian', and 'sigma'.
        Please refer to the `median_filter` and `gaussian_filter` documentation in
         `fijipy.processing.image_denoising` for more information.
    image: Union[str : Image file path.

                 np.ndarray] : Image array.

    Returns
    -------
    np.ndarray
        Denoised image.

    """
    if isinstance(image, str):
        image = cv2.imread(image)

    # load hyperparameters from data json file
    algorithm = data['denoising_algorithm']

    # Apply the selected denoising algorithm
    if algorithm == 'median':
        kernel_size_median = data['kernel_size_median']
        denoised_image = median_filter(image, kernel_size_median)
    elif algorithm == 'gaussian':
        sigma = data['sigma']
        kernel_size_gaussian = tuple(data['kernel_size_gaussian'])
        denoised_image = gaussian_filter(image, kernel_size_gaussian, sigma)

    return denoised_image