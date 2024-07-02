import preprocess_compress, binarization, edge_detection, image_to_midi, image_to_saliency, image_to_midi
from dataio import image_loader

# access loaded image
# rewrite to fit with argparse input method <<<<<
##############
image = image_loader.load_image("demodata/demo_Image.jpg") # test case: works
##############

# apply compression if needed
compressed_image = preprocess_compress.preprocess_compress_image(image)

# binarize image
binarized_image = binarization.binarize_image(compressed_image)

# generate an edge map
edge_map = edge_detection.detect_edges(image = binarized_image)

# generate a saliency map
saliency_maps = image_to_saliency.generate_per_channel_saliency(image = binarized_image)
saliency_map = image_to_saliency.merge_saliency_maps(saliency_maps)

# generate a MIDI file
midi_file = image_to_midi.create_midi_from_arrays(edge_map = edge_map, saliency_map = saliency_map)




