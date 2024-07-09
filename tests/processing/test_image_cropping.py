import unittest
# import processing.image_cropping as image_cropping (this also works)
# import dataio.image_loader as image_loader 
# from processing.image_cropping import crop_image (this also works)
# from dataio.image_loader import load_image
from processing import image_cropping
from dataio import image_loader

import cv2
import os
import numpy as np


class FijiPyTestImageCropping(unittest.TestCase):
    """ Test the image cropping functionality. """

    def setUp(self):
        """ Set up test variables as object attributes """
        self.load_image = image_loader.load_image
        self.demo_data_path = "demodata" + os.sep + "demo_Image.jpg"
        self.image = self.load_image(self.demo_data_path)
        self.crop_image = image_cropping.crop_image 
        self.crop_width = 100
        self.crop_height = 100 
        self.crop_x = 50
        self.crop_y = 50
        self.data = {'crop_width': self.crop_width,  'crop_height': self.crop_height, 'crop_x': self.crop_x, 'crop_y': self.crop_y}
        self.cropped_image = self.crop_image(image=self.image, data=self.data)
        
    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "load_image")
        delattr(self, "demo_data_path")
        delattr(self, "image")
        delattr(self, "crop_image")
        delattr(self, "crop_width")
        delattr(self, "crop_height")
        delattr(self, "crop_x")
        delattr(self, "crop_y")
        delattr(self, "cropped_image")

    def test_crop_size(self):
        "Test the size of cropped image."        
        # Assert the cropped image dimensions
        self.assertEqual(self.cropped_image.shape, (self.crop_height, self.crop_width, 3))

    def test_crop_content(self):
        "Test the content of cropped image."
        desired_image = \
            self.image[self.crop_y:self.crop_y+self.crop_height, self.crop_x:self.crop_x+self.crop_width]
        # Assert the cropped image content
        self.assertTrue(np.array_equal(self.cropped_image, desired_image))

    #def test_crop_out_of_image(self):
        # test the function above
        #data_dir = '.' + os.sep + 'demodata'  + os.sep
        #image_cropped_path = data_dir + 'demo_Image_cropped.jpg'
        #cv2.imwrite(image_cropped_path, self.cropped_image)

if __name__ == '__main__':
    unittest.main()