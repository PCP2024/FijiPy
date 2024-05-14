from midiutil import MIDIFile
import numpy as np

def create_midi_from_arrays(edge_map, saliency_map, time_signature=(4, 4), tempo=120, output_file="image_score.mid"):
    # Mask saliency array to assign a velocity to each note
    # saliency must take values between 0 and 127 !!!!
    # must be the same shape as edge_map
    masked_saliency_map = np.where(edge_map == 1, saliency_map, 0)

    # Create a MIDIFile object with one track
    midi_file = MIDIFile(1, file_format=1)

    # Add track name and tempo
    midi_file.addTrackName(0, 0, "Track 0")
    midi_file.addTempo(0, 0, tempo) # user specified

    # Add time signature
    midi_file.addTimeSignature(0, 0, *time_signature)

    # Set instrument (optional)
    midi_file.addProgramChange(0, 0, 0, 0)  # Use instrument 0 (piano)

    # Iterate through the numpy array and add MIDI events
    time = 0
    duration = 1  # Duration of each note (in beats) <<<< do we want this to be dynamic? random?
    for i, row in enumerate(edge_map):
        for j, value in enumerate(row):
            if value == 1:
                pitch = i
                velocity = masked_saliency_map[i, j]
                midi_file.addNote(0, 0, pitch, time, duration, velocity=velocity)
            time += duration

    # Write the MIDI events to a file
    with open(output_file, "wb") as f:
        midi_file.writeFile(f)