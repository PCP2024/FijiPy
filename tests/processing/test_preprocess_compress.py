import unittest
import numpy as np
from unittest.mock import patch

from processing.preprocess_compress import preprocess_compress_image
from skimage.transform import resize  # For mocking purposes


class TestPreprocessCompressImage(unittest.TestCase):

    def test_compression_with_large_image(self):
        # Create a large image with axis 0 length > 128
        large_image = np.random.rand(256, 128, 3)

        # Call the preprocess_compress_image function
        compressed_image = preprocess_compress_image(large_image)

        # Check if the compressed image has axis 0 length <= 128
        self.assertTrue(compressed_image.shape[0] <= 128)

    def test_no_compression_with_small_image(self):
        # Create a small image with axis 0 length <= 128
        small_image = np.random.rand(64, 128, 3)

        # Call the preprocess_compress_image function
        compressed_image = preprocess_compress_image(small_image)

        # Check if the compressed image is the same as the input image
        self.assertTrue(np.array_equal(compressed_image, small_image))

    def test_aspect_ratio_preservation(self):
        # Create an image with non-square aspect ratio
        non_square_image = np.random.rand(256, 128, 3)

        # Call the preprocess_compress_image function
        compressed_image = preprocess_compress_image(non_square_image)

        # Calculate the expected width after compression
        expected_width = int(non_square_image.shape[1] * (128 / non_square_image.shape[0]))

        # Check if the compressed image has the expected width
        self.assertEqual(compressed_image.shape[1], expected_width)

if __name__ == '__main__':
    unittest.main()