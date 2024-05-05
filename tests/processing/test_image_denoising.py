import unittest
from processing import image_denoising
import cv2
import numpy as np

class FijiPyTestImageDenoising(unittest.TestCase):
    """ Test the image denoising functionality. """
    
    def test_import_modules(self):
        """ Test that required modules can be imported. """
        modules = [
            (self.image_denoising_module, "image_denoising"),
            (self.cv2_module, "cv2"),
            (self.numpy_module, "numpy")
        ]
        for module, module_name in modules:
            with self.subTest(module=module_name):
                self.assertIsNotNone(module)

    def test_median_filter(self):
        """ Test the median_filter function. """
        image = np.random.randint(0, 255, (100, 100, 3)).astype(np.uint8)
        kernel_size = 3
        denoised_image = self.image_denoising_module.median_filter(image, kernel_size)
        self.assertEqual(denoised_image.shape, image.shape)

    def test_gaussian_filter(self):
        """ Test the gaussian_filter function. """
        image = np.random.randint(0, 255, (100, 100, 3)).astype(np.uint8)
        sigma = 1.0
        denoised_image = self.image_denoising_module.gaussian_filter(image, sigma)
        self.assertEqual(denoised_image.shape, image.shape)

    def test_denoise_image(self):
        """ Test the denoise_image function. """
        image = np.random.randint(0, 255, (100, 100, 3)).astype(np.uint8)
        denoised_image = self.image_denoising_module.denoise_image(image, algorithm='median', kernel_size=3)
        self.assertEqual(denoised_image.shape, image.shape)
