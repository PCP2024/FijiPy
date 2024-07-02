import unittest
import cv2
import numpy as np
from processing.binarization import binarize_image

class BinarizationTestCase(unittest.TestCase):
    def setUp(self):
        self.image_path = 'demodata/demo_Image.jpg'
        self.image = cv2.imread(self.image_path)
        self.data = {'threshold_value': np.max(self.image)/2, 'max_value': np.max(self.image),'threshold_type': "THRESH_BINARY_INV"}

    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "image_path")
        delattr(self, "image")
        delattr(self, "data")

    def test_binarize_image_with_image_path(self):
        binary_image = binarize_image(image=self.image_path, data=self.data)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape,  self.image.shape[:2])

    def test_binarize_image_with_image_object(self):
        binary_image = binarize_image(image=self.image, data=self.data)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape, self.image.shape[:2])

    def test_binarize_image_with_custom_threshold_type(self):
        binary_image = binarize_image(image=self.image_path, data=self.data)
        self.assertIsInstance(binary_image, np.ndarray)
        self.assertEqual(binary_image.shape, self.image.shape[:2])

    def test_binarize_image_with_invalid_threshold_type(self):
        self.data['threshold_type'] = "INVALID_THRESHOLD_TYPE"
        with self.assertRaises(KeyError):
            binarize_image(image=self.image_path, data=self.data)

if __name__ == '__main__':
    unittest.main()