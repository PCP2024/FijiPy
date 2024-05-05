import unittest
from dataio import image_loader


class TestLoadImage(unittest.TestCase):
    """ Test ImageLoader functionality """

    def setUp(self):
        """ Set up test variables as object attributes """
        self.load_image = image_loader.load_image
        self.demo_data_path = "../../demodata/demo_Image.jpg"
        self.wrong_demo_data_path = "../../demodata/demoImage.jpg"
        self.path_to_wrong_file_type = "../../dataio/image_loader.py"
        self.wrong_path_datatype = 123.321

    def tearDown(self):
        """ Tear down test variable object attributes """
        delattr(self, "load_image")
        delattr(self, "demo_data_path")
        delattr(self, "wrong_demo_data_path")
        delattr(self, "path_to_wrong_file_type")
        delattr(self, "wrong_path_datatype")

    def test_load_image_with_wrong_path(self):
        """ Test load_image with a path that does not exist """
        #self.assertRaises(FileNotFoundError, self.load_image, self.wrong_demo_data_path)
        self.assertIsNone(self.load_image(self.wrong_demo_data_path))

    def test_load_image_with_wrong_file_type(self):
        """ Test load_image with a path to a file of the wrong type """
        #self.assertRaises(TypeError, self.load_image, self.wrong_demo_data_path)
        self.assertIsNone(self.load_image(self.path_to_wrong_file_type))
        print(self.load_image(self.path_to_wrong_file_type))

    def test_load_image_with_wrong_path_datatype(self):
        """ Test load_image with a non-string (float) input to file path """
        self.assertRaises(TypeError, self.load_image, self.wrong_path_datatype)

    def test_load_image_with_iterable_path(self):
        """ Test load_image with the correct demodata path in an iterable (list) object """
        self.assertRaises(TypeError, self.load_image, [self.demo_data_path])

    def test_load_image_with_demo_data_shape(self):
        """ Test that load_image with the correct demodata path returns the correct output shape """
        self.assertEqual(self.load_image(self.demo_data_path).shape, (570, 995, 3))

