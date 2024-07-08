import unittest
from processing import image_denoising
import cv2
import numpy as np

class FijiPyTestImageDenoising(unittest.TestCase):
    """ Test the image denoising functionality. """
    def setUp(self):
        self.image = np.random.randint(0, 255, (100, 100, 3)).astype(np.uint8)
        self.data = {'sigma': 1.0, 'kernel_size': (3, 3), 'kernel_size_median': 3, 'denoising_algorithm': 'median'}

    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "image")
        delattr(self, "data")

    def test_import_modules(self):
        """ Test that required modules can be imported. """
        modules = [
            (image_denoising, "image_denoising"),
            (cv2, "cv2"),
            (np, "numpy")
        ]
        for module, module_name in modules:
            with self.subTest(module=module_name):
                self.assertIsNotNone(module)

    def test_median_filter(self):
        """ Test the median_filter function. """

        denoised_image = image_denoising.median_filter(image=self.image, kernel_size=self.data['kernel_size_median'])
        self.assertEqual(denoised_image.shape, self.image.shape)

    def test_gaussian_filter(self):
        """ Test the gaussian_filter function. """
        denoised_image = image_denoising.gaussian_filter(self.image, self.data['kernel_size'], self.data['sigma'])
        self.assertEqual(denoised_image.shape, self.image.shape)

    # Ghadi: you need a mocker of the methods used inside "image_denoising.denoise_image"
    def test_denoise_image(self):
        """ Test the denoise_image function. """
        denoised_image = image_denoising.denoise_image(data=self.data, image=self.image)
        self.assertEqual(denoised_image.shape, self.image.shape)
