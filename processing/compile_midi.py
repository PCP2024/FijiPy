import subprocess
from midi2audio import FluidSynth
import pygame


# def compile_midi_to_audio(input_midi, output_audio, soundfont):
#     # Command to convert MIDI to audio using fluidsynth
#     cmd = f"fluidsynth -F {output_audio} {soundfont} {input_midi}"
    
#     # Execute the command
#     subprocess.run(cmd, shell=True)
# import logging
# def compile_midi_to_audio2(input_midi, output_audio, soundfont):
#     try:
#         logging.debug("Input MIDI file: %s", input_midi)
#         logging.debug("Output audio file: %s", output_audio)
#         logging.debug("Soundfont file: %s", soundfont)
#         # Use the full path to the fluidsynth executable
#         fluidsynth_path = 'C:\\Users\\bianc\\fluidsynth\\bin\\fluidsynth.exe'  # Replace with the actual path
#         subprocess.call([fluidsynth_path, '-ni', soundfont, input_midi, '-F', output_audio])
#     except FileNotFoundError as e:
#         logging.error("File not found: %s", e.filename)

def play_music(midi_filename):
  '''Stream music_file in a blocking manner'''
  clock = pygame.time.Clock()
  pygame.mixer.music.load(midi_filename)
  pygame.mixer.music.play()
  while pygame.mixer.music.get_busy():
    clock.tick(30) # check if playback has finished
    
midi_filename = 'image_score.mid'

# mixer config
freq = 44100  # audio CD quality
bitsize = -16   # unsigned 16 bit
channels = 1  # 1 is mono, 2 is stereo
buffer = 1024   # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(0.8)

# listen for interruptions
try:
  # use the midi file you just saved
  play_music(midi_filename)
except KeyboardInterrupt:
  # if user hits Ctrl/C then exit
  # (works only in console mode)
  pygame.mixer.music.fadeout(1000)
  pygame.mixer.music.stop()
  raise SystemExit

