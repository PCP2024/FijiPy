import unittest
from unittest.mock import patch, MagicMock, call
import numpy as np
from processing.image_to_midi import create_midi_from_arrays

class TestCreateMIDIFromArrays(unittest.TestCase):

    def test_create_midi_from_arrays(self):
    # Mock MIDIFile and its methods
        with patch("processing.image_to_midi.MIDIFile") as mock_midi_file:
           # Prepare test data
            edge_map = np.array([[1, 0, 1], [0, 1, 0]])
            saliency_map = np.array([[64, 127, 32], [0, 96, 100]])
            time_signature = (4, 4)
            tempo = 150
            output_file = "test_output.mid"

            # Call the function
            create_midi_from_arrays(edge_map, saliency_map, time_signature, tempo, output_file)

            # Assertions
            mock_midi_file.assert_called_once_with(1, file_format=1)
            mock_midi_file_instance = mock_midi_file.return_value
            mock_midi_file_instance.addTrackName.assert_called_once_with(0, 0, "Track 0")
            mock_midi_file_instance.addTempo.assert_called_once_with(0, 0, tempo)
            mock_midi_file_instance.addTimeSignature.assert_called_once_with(0, 0, time_signature[0], time_signature[1], 24)
            mock_midi_file_instance.addProgramChange.assert_called_once_with(0, 0, 0, 0)

            # Check the calls to addNote
            expected_calls = [
                call(0, 0, 0, 0, 1, volume=64),  # First note
                call(0, 0, 1, 1, 1, volume=96),  # Third note
                call(0, 0, 0, 2, 1, volume=32),  # Second note
            ]
            mock_midi_file_instance.addNote.assert_has_calls(expected_calls, any_order=False)

if __name__ == "__main__":
    unittest.main()