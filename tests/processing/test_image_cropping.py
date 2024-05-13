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
        width = 100
        height = 100
        x = 50
        y = 50

        # Call the image_cropping function
        cropped_image = image_cropping(image, width, height, x, y)

        # Assert the cropped image dimensions
        self.assertEqual(cropped_image.shape, (height, width, 3))

    def test_crop_content(self):
        "Test the content of cropped image."
        # Create a dummy image
        image = np.zeros((200, 200, 3), dtype=np.uint8)
        width = 100
        height = 100
        x = 50
        y = 50

        # Call the image_cropping function
        cropped_image = image_cropping(image, width, height, x, y)

        # Assert the cropped image content
        self.assertTrue(np.array_equal(cropped_image, image[y:y+height, x:x+width]))

if __name__ == '__main__':
    unittest.main()