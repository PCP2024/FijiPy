#from dataio import image_loader
import numpy as np
from skimage.transform import resize

def preprocess_compress_image(image):
    """
    THIS FUNCTION MUST BE CALLED AT THE BEGINNING OF THE img2song PROCESSING PIPELINE.
    Ensures image axis 0 maps perfectly to pitch axis of MIDI file.
    Compress the input image to have axis 0 length <= 128.

    Args:
        image (ndarray): Input image.

    Returns:
        ndarray: Compressed image.
    """
    # Check if axis 0 length is less than or equal to 128
    if image.shape[0] <= 128:
        return image  # No need to compress, return original image

    # Calculate the compression factor
    compression_factor = 128 / image.shape[0]

    # Resize the image to have axis 0 length = 128 while preserving aspect ratio
    compressed_image = resize(image, (128, int(image.shape[1]*compression_factor)),
                              anti_aliasing=True)

    return compressed_image

# Test the function >>>> OK
# implement full test
#import cv2
#image = cv2.imread("demodata/demo_Image.jpg")
#compressed_image = preprocess_compress_image(image)

#print(f"Original image shape: {image.shape}")
#print(f"Compressed image shape: {compressed_image.shape}")