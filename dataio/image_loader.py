# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:56:04 2024

@author: Bernardo Andrade Ortega
"""

import cv2

def load_image(imagename):
        """
   Imports an image 

    Parameters
    ----------
    imagename : str
        Name/path of the image

    Returns
    -------
    image : numpy.ndarray
        Array of size (NxMxC), (NxM) is the size of the image and C 3 for RGB 
        and 1 for black and white
        
    """
    
    return cv2.imread(imagename)}