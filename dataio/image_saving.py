import cv2
import numpy as np


def save_image(output_image_path: str, image: np.ndarray) -> None:
    """
    Imports an image

    Parameters
    ----------
    output_image_path : str
        Path to save the image         
    
    image : numpy.ndarray
        Array of size (NxMxC), (NxM) is the size of the image and C 3 for RGB 
        and 1 for black and white

    Returns
    -------
    None
        
    """
    
    cv2.imwrite(output_image_path, image)
