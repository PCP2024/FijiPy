import subprocess

def compile_midi_to_audio(input_midi, output_audio, soundfont):
    # Command to convert MIDI to audio using fluidsynth
    cmd = f"fluidsynth -F {output_audio} {soundfont} {input_midi}"
    
    # Execute the command
    subprocess.run(cmd, shell=True)
