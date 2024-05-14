import unittest
from processing import image_cropping
import cv2
import numpy as np

class FijiPyTestImageCropping(unittest.TestCase):
    """ Test the image cropping functionality. """
    def test_crop_size(self):
        "Test the size of cropped image."
        # Create a dummy image
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        crop_width = 100
        crop_height = 100
        crop_x = 50
        crop_y = 50

        # Call the image_cropping function
        cropped_image = image_cropping(image, crop_width, crop_height, crop_x, crop_y)

        # Assert the cropped image dimensions
        self.assertEqual(cropped_image.shape, (crop_height, crop_width, 3))

    def test_crop_content(self):
        "Test the content of cropped image."
        # Create a dummy image
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        crop_width = 100
        crop_height = 100
        crop_x = 50
        crop_y = 50

        # Call the image_cropping function
        cropped_image = image_cropping(image, crop_width, crop_height, crop_x, crop_y)

        # Assert the cropped image content
        self.assertTrue(np.array_equal(cropped_image, image[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]))

if __name__ == '__main__':
    unittest.main()