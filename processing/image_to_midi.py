from midiutil import MIDIFile
import numpy as np


def create_midi_from_arrays(data: dict, edge_map: np.ndarray, saliency_map: np.ndarray, output_path: str) -> None:
    """

    Parameters
    ----------
    data: dict :
        Extra arguments to `MIDIFile.addTempo` and `MIDIFile.addTimeSignature`: Possible arguments include
        'tempo' and 'time_signature'.
        Please refer to the respective documentation for more information.
    edge_map: np.ndarray :
        Edge map as resulting from `fijipy.processing.edge_detection.detect_edges`
    saliency_map: np.ndarray :
        Saliency map as resulting from a function in `fijipy.processing.image_to_saliency`
    output_path: str :
        Output path to save MIDI file

    Returns
    -------
    None

    """
    # import hyperparameters from data json file
    time_signature = data['time_signature']
    tempo = data['tempo']
    
    # convert edge_map back to binary
    edge_map = np.where(edge_map > 0, 1, 0)

    # check if edge_map and saliency_map have the same shape
    if edge_map.shape != saliency_map.shape:
        # crop the larger array to match both dimensions of the smaller array
        edge_map = edge_map[:saliency_map.shape[0], :saliency_map.shape[1]]
    
    # Mask saliency array to assign a velocity to each note
    # saliency must take values between 0 and 127 !!!!
    # if range of saliency_map is outside of [0,127] normalize saliency values to be between 0 and 127
    if np.max(saliency_map) > 127:
        saliency_map = (saliency_map / np.max(saliency_map)) * 127
    # must be the same shape as edge_map
    masked_saliency_map = np.where(edge_map == 1, saliency_map, 0)
    masked_saliency_map = np.round(masked_saliency_map).astype(int)
    masked_saliency_map = masked_saliency_map.T
    # Create a MIDIFile object with one track
    midi_file = MIDIFile(1, file_format=1)

    # Add track name and tempo
    midi_file.addTrackName(0, 0, "Track 0")
    midi_file.addTempo(0, 0, tempo) # user specified

    # Add time signature
    midi_file.addTimeSignature(0, 0, time_signature[0], time_signature[1], 24)

    # Set instrument (optional)
    midi_file.addProgramChange(0, 0, 0, 0)  # Use instrument 0 (piano)

    # Transpose the edge_map array
    transposed_edge_map = np.transpose(edge_map)

    # Iterate through the transposed numpy array and add MIDI events
    time = 0
    duration = 1  # Duration of each note (in beats)
    
    for i, row in enumerate(transposed_edge_map):
        for j, value in enumerate(row):

            if value == 1:
                pitch = j  # Use j as pitch since it's iterating through columns
                velocity = masked_saliency_map[i, j]
                midi_file.addNote(0, 0, pitch, time, duration, volume=velocity)
        time += duration

    # Write the MIDI events to a file
    with open(output_path, "wb") as f:
        midi_file.writeFile(f)

############################
# currently works for following call
# probability_edges = 0.05
# probability_saliency = 0.05
# edges = np.random.choice([0, 1], size=(50, 120), p=[1 - probability_edges, probability_edges])
# saliency = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7], size=(50, 120), p=[0.3, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1])

# create_midi_from_arrays(data= {'time_signature': (4, 4), 'tempo': 120}, edge_map=edges, saliency_map=saliency, output_path="output.mid")
