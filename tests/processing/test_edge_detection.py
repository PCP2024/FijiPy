import cv2
import numpy as np
import unittest
from processing.edge_detection import detect_edges

class EdgeDetectionTestCase(unittest.TestCase):
    def setUp(self):
        # Load the test image
        self.image_path = 'demodata/demo_Image_dilated.jpg'
        self.image = cv2.imread(self.image_path)

    def test_output_not_none(self):
        # Call the edge detection function
        edges = detect_edges(image=self.image)

        # Assert that the output is not None
        self.assertIsNotNone(edges)

    def test_output_dtype(self):
        # Call the edge detection function
        edges = detect_edges(image=self.image)

        # Assert that the output is a binary image
        self.assertEqual(edges.dtype, np.uint8)
        self.assertEqual(set(np.unique(edges)), {0, 255})

    def test_output_shape(self):
        # Call the edge detection function
        edges = detect_edges(image=self.image)

        # Assert that the output has the same shape as the input image
        self.assertEqual(edges.shape, self.image.shape[:2])

    def test_output_has_edges(self):
        # Call the edge detection function
        edges = detect_edges(image=self.image)

        # Assert that the output image has edges
        self.assertGreater(np.sum(edges), 0)

if __name__ == '__main__':
    unittest.main()