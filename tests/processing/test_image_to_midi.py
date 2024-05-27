import unittest
from unittest.mock import patch
import numpy as np
from midiutil import MIDIFile

from processing.image_to_midi import create_midi_from_arrays

class TestCreateMidiFromArrays(unittest.TestCase):

    @patch('processing.image_to_midi.MIDIFile')
    def test_create_midi_from_arrays(self, mock_midi_file):
        # Mock the MIDIFile object
        mock_midi_file_instance = mock_midi_file.return_value

        # Define input arrays
        edge_map = np.array([[0, 1, 0], [1, 0, 1]])
        saliency_map = np.array([[0, 1, 2], [3, 4, 5]])
        time_signature = (4, 4)
        tempo = 150
        output_file = "test_output.mid"

        # Call the function
        create_midi_from_arrays(edge_map, saliency_map, time_signature, tempo, output_file)

        # Assert that the MIDIFile object was created with the correct arguments
        mock_midi_file.assert_called_once_with(1, file_format=1)

        # Assert that the MIDI events were added correctly
        expected_calls = [
            mock_midi_file_instance.addTrackName.call_args_list[0],
            mock_midi_file_instance.addTempo.call_args_list[0],
            mock_midi_file_instance.addTimeSignature.call_args_list[0],
            mock_midi_file_instance.addProgramChange.call_args_list[0],
            mock_midi_file_instance.addNote.call_args_list[0],
            mock_midi_file_instance.writeFile.call_args_list[0]
        ]
        actual_calls = [
            call for call in mock_midi_file_instance.method_calls if call[0] != 'addTrackName'
        ]
        self.assertEqual(actual_calls, expected_calls)

        # Assert that the output file was written correctly
        mock_midi_file_instance.writeFile.assert_called_once_with(output_file)

if __name__ == '__main__':
    unittest.main()