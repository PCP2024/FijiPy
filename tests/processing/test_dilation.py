import unittest
import cv2
import json
import numpy as np
from processing.dilation import dilate_image

class DilationTestCase(unittest.TestCase):
    def setUp(self):
        # Load test data from JSON file
        with open("data_file.json", "r") as read_file:
            self.data = json.load(read_file)

    def test_dilate_image(self):
        # Test case 1: Check if the dilated image is generated correctly
        image_path = 'demodata/demo_Image.jpg'
        image = cv2.imread(image_path)
        dilated_image = dilate_image(image)
        self.assertIsInstance(dilated_image, np.ndarray)
        self.assertEqual(dilated_image.shape, image.shape)

        # Test case 2: Check if the dilated image is saved correctly
        output_path = 'demodata/demo_Image_dilated.jpg'
        cv2.imwrite(output_path, dilated_image)
        saved_image = cv2.imread(output_path)
        self.assertIsNotNone(saved_image)
        self.assertEqual(saved_image.shape, dilated_image.shape)

if __name__ == '__main__':
    unittest.main()