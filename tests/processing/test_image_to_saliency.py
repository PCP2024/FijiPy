import unittest
import numpy as np
from processing.image_to_saliency import generate_per_channel_saliency

class TestGeneratePerChannelSaliency(unittest.TestCase):
    def test_generate_per_channel_saliency(self):
        # Create a sample image
        image = np.random.rand(100, 100, 3)

        # Call the function
        saliency_maps = generate_per_channel_saliency(data={'patch_size': 15}, image=image)

        # Check the shape of the output
        self.assertEqual(saliency_maps.shape, (86, 86, 3))

        # Check that the saliency values are between 0 and 1
        self.assertTrue(np.all(saliency_maps >= 0))
        self.assertTrue(np.all(saliency_maps <= 1))

if __name__ == '__main__':
    unittest.main()