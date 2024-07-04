import unittest
import cv2
import json
import numpy as np
from processing.dilation import dilate_image

class DilationTestCase(unittest.TestCase):
    def setUp(self):
        self.image_path = "demodata/demo_Image.jpg"
        self.image = cv2.imread(self.image_path)
        # Load test data from JSON file
        with open("data_file.json", "r") as read_file:
            self.data = json.load(read_file)

    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "image_path")
        delattr(self, "image")
        delattr(self, "data")

    def test_dilate_image_with_image_path(self):
        # Test case 1: Check if the dilated image is generated correctly
        dilated_image = dilate_image(data=self.data, image=self.image_path)
        self.assertIsInstance(dilated_image, np.ndarray)
        self.assertEqual(dilated_image.shape, self.image.shape)

    def test_dilate_image_with_loaded_image(self):
        # Test case 1: Check if the dilated image is generated correctly
        dilated_image = dilate_image(data=self.data, image=self.image)
        self.assertIsInstance(dilated_image, np.ndarray)
        self.assertEqual(dilated_image.shape, self.image.shape)

        # Ghadi: this isn't part of what the function does, so it doesn't need to be here. if this is to be implemented, you might need to tear down this temporary saved file
        # Test case 2: Check if the dilated image is saved correctly
        #output_path = 'demodata/demo_Image_dilated.jpg'
        #cv2.imwrite(output_path, dilated_image)
        #saved_image = cv2.imread(output_path)
        #self.assertIsNotNone(saved_image)
        #self.assertEqual(saved_image.shape, dilated_image.shape)

if __name__ == '__main__':
    unittest.main()