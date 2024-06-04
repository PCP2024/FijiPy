import unittest
from unittest.mock import patch
import numpy as np
from processing.image_to_midi import create_midi_from_arrays

class TestCreateMIDIFromArrays(unittest.TestCase):

    def setUp(self):
        self.edge_map = np.array([[1, 0, 1], [0, 1, 0]])
        self.saliency_map = np.array([[64, 127, 32], [0, 96, 100]])
        self.time_signature = (4, 4)
        self.tempo = 120
        self.output_file = "test_output.mid"

    def test_midi_creation(self):
        # Mock the open function to avoid creating an actual file
        with patch("processing.image_to_midi.open") as mock_open:
            create_midi_from_arrays(self.edge_map, self.saliency_map,
                                    self.time_signature, self.tempo, self.output_file)

            # Assert that open was called with the correct arguments
            mock_open.assert_called_once_with(self.output_file, "wb")

            # Assert that MIDIFile.writeFile was called
            self.assertTrue(mock_open.return_value.__enter__.called)
            midi_file = mock_open.return_value.__enter__.return_value
            midi_file.writeFile.assert_called_once()

if __name__ == "__main__":
    unittest.main()