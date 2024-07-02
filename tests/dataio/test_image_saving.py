import unittest
from dataio import image_saving
from dataio import image_loader
import numpy as np
import os

class TestSaveImage(unittest.TestCase):
    """ Test ImageLoader functionality """

    def setUp(self):
        """ Set up test variables as object attributes """
        self.save_image = image_saving.save_image
        self.demo_data_path = "demodata/demo_Image.jpg"        
        self.image = image_loader.load_image(self.demo_data_path)
        self.output_image_path = "demodata/demo_Image_copy.jpg" 
        self.save_image(self.output_image_path, self.image)
        self.saved_image = image_loader.load_image(self.output_image_path)      

    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "save_image")
        delattr(self, "demo_data_path")
        delattr(self, "image")
        delattr(self, "output_image_path")

    def test_save_image_exist(self):
        """ Test whehter the saved image exists or not"""
        self.assertTrue(os.path.isfile(self.output_image_path))

    # Ghadi: this test fails, but it is not needed as this isn't relevant to the function
    def test_saved_image_is_the_same(self):
        """ Test whether the saved image is the same as the original image"""
        print(self.image)
        print(self.saved_image)
        print(self.image - self.saved_image)
        print(np.array_equal(self.image, self.saved_image))
        self.assertTrue(np.array_equal(self.image, self.saved_image))
        
if __name__ == '__main__':
    unittest.main()