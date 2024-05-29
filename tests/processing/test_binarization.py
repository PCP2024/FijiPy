import unittest
import cv2
import numpy as np
from processing.binarization import binarize_image

class BinarizationTestCase(unittest.TestCase):
    def setUp(self):
        self.image_path = 'demodata/demo_Image.jpg'
        self.image = cv2.imread(self.image_path)
    def test_binarize_image_with_image_path(self):
        binary_image = binarize_image(image_path=self.image_path)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape,  self.image.shape[:2])

    def test_binarize_image_with_image_object(self):
        binary_image = binarize_image(image=self.image)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape, self.image.shape[:2])

    def test_binarize_image_with_custom_threshold_type(self):
        binary_image = binarize_image(image_path=self.image_path, threshold_type="THRESH_BINARY_INV")
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape, self.image.shape[:2])

    def test_binarize_image_with_invalid_threshold_type(self):
        with self.assertRaises(ValueError):
            binarize_image(image_path=self.image_path, threshold_type="INVALID_THRESHOLD_TYPE")

if __name__ == '__main__':
    unittest.main()