import argparse
import json
from configuration import write_config
from processing import (binarization, 
                        edge_detection, image_denoising, 
                        dilation, image_cropping,
                        image_to_saliency, preprocess_compress,
                        image_to_midi)
from dataio import image_saving, image_loader
import cv2
import os

def main(): 
    # create parser object    
    parser = argparse.ArgumentParser(
        description='Convert image to song.', \
        epilog='By PCP 2024 FijiPy')
    
    
    # arguments
    parser.add_argument('input_image_path', \
                        type=str, \
                        help='Path to the input image.')
    parser.add_argument('convert', \
                        type=str, \
                        help='Type of conversion .')
    parser.add_argument('output_path', \
                        type=str, \
                        help='Path to the output file (either image or audio).')
    
    # to-do 1
    parser.add_argument('--config', type=str, help='Path to the configuration file.', default='data_file.json')
    args, unknown = parser.parse_known_args()
    if args.config is not None:
        config_file = args.config
        with open(config_file, "r") as read_file:
            config_data = json.load(read_file)
    else:
        config_file = 'data_file.json'
        with open(config_file, "r") as read_file:
            config_data = json.load(read_file)
    
    
    
    # optional arguments
    parser.add_argument('--version', \
                        type=str, \
                        help='Show version.', \
                        default='False')
    # denoising
    parser.add_argument('--denoising_algorithm', \
                        type=str, \
                        help='For denoising. Denoising algorithm. default: median', \
                        default=config_data['denoising_algorithm'])
    parser.add_argument('--kernel_size_gaussian', \
                        type=list, \
                        help='For denoising. Kernel size of Gaussian filter. default: [5,5]', \
                        default=config_data['kernel_size_gaussian'])
    parser.add_argument('--kernel_size_median', \
                        type=int, \
                        help='For denoising. Kernel size of median filter (int). default: 3', \
                        default=config_data['kernel_size_median'])
    parser.add_argument('--sigma', \
                        type=float, \
                        help='For denoising. Sigma. default: 1', \
                        default=config_data['sigma'])    
    # edge detection 
    parser.add_argument('--canny_lower_threshold', \
                        type=float, \
                        help='For edge detection. Canny lower threshold. default: 100', \
                        default=config_data['canny_lower_threshold'])
    parser.add_argument('--canny_upper_threshold', \
                        type=float, \
                        help='For edge detection. Canny upper threshold. default: 120', \
                        default=config_data['canny_upper_threshold'])    
    # binarisation 
    parser.add_argument('--threshold_type', \
                        type=str, \
                        help='For binarisation. Threshold type. default: THRESH_BINARY_OTSU', \
                        default=config_data['threshold_type'])
    parser.add_argument('--max_value', \
                        type=float, \
                        help='For binarisation. max value. default: 255', \
                        default=config_data['max_value'])
    parser.add_argument('--threshold_value', \
                        type=float, \
                        help='For binarisation. Threshold value. default: 50', \
                        default=config_data['threshold_value'])  
    # dialation 
    parser.add_argument('--structuring_element_type', \
                        type=str, \
                        help='For dilation. Structuring element type. default: MORPH_RECT', \
                        default=config_data['structuring_element_type'])
    parser.add_argument('--structuring_element_size', \
                        type=list, \
                        help='For dilation. Structuring element size. default: [3,3]', \
                        default=config_data['structuring_element_size'])
    parser.add_argument('--dilation_iterations', \
                        type=int, \
                        help='For dilation. Number of iterations. default: 2', \
                        default=config_data['dilation_iterations'])
    # image crop
    parser.add_argument('--crop_width', \
                        type=int, \
                        help='For cropping. Width of the crop region. default: 100', \
                        default=config_data['crop_width'])
    parser.add_argument('--crop_height', \
                        type=int, \
                        help='For cropping. Height of the crop region. default: 100', \
                        default=config_data['crop_height'])
    parser.add_argument('--crop_x', \
                        type=int, \
                        help='For cropping. X-coordinate of the top-left corner of the crop region. default: 0', \
                        default=config_data['crop_x'])
    parser.add_argument('--crop_y', \
                        type=int, \
                        help='For cropping. Y-coordinate of the top-left corner of the crop region. default: 0', \
                        default=config_data['crop_y'])
    # image 2 saliency
    parser.add_argument('--patch_size', \
                        type=int, \
                        help='For saliency. Patch size. default: 5', \
                        default=config_data['patch_size'])
    # preprocess compress
    
    # >> at present no additional arguments are needed for this function

    # image to midi
    parser.add_argument('--time_signature', \
                        type=list, \
                        help='For midi. Time signature. default: [4,4]', \
                        default=config_data['time_signature'])
    parser.add_argument('--tempo', \
                        type=int, \
                        help='For midi. Tempo. default: 120', \
                        default=config_data['tempo'])
    # save config
    parser.add_argument('--save_config', \
                        type=str, \
                        help='location and name to save an updated version of the used config file. default: None', \
                        default=None)
    # save intermediate images
    parser.add_argument('--save_intermediate', \
                        type=bool, \
                        help="save intermediate images in output path if you use the option convert 'all'. default: False", \
                        default=False)

    args = parser.parse_args()

    if args.version == 'True': 
        with open('VERSION', 'r') as f:
            print('version: ' + f.read())

    if args.save_config is not None:
        config_file = args.save_config
        json.dump(config_data, open(config_file, 'w'), indent=4)
    # overwrite the user-specified value in the configuration file.
    for key, value in vars(args).items():
        # if the key is in the configuration file, update the value.
        if key in config_data: 
            write_config.update_json_file(config_file, \
                                        key, \
                                        value)

    with open(config_file, "r") as read_file:
            config_data = json.load(read_file)


    if args.convert == 'binarization':
        print('--binarizing image---')
        proc_img = binarization.binarize_image(config_data, args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'edge_detection':
        print('--detecting edge---')
        proc_img = edge_detection.detect_edges(config_data, args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'denoising':
        print('--denoising image---')
        proc_img = image_denoising.denoise_image(config_data, args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'dilation':
        print('--dialating image---')
        proc_img = dilation.dilate_image(config_data, args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'crop':
        print('--cropping image---')
        proc_img = image_cropping.crop_image(config_data, args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'saliency':
        print('--generating saliency map---')
        print('Three channel saliency maps will additionally be saved in the same directory\n of the merged saliency map as "saliency map ch*.jpg" ')
        proc_img, ch1, ch2, ch3 = image_to_saliency.generate_per_channel_saliency(config_data, args.input_image_path,)
        cv2.imwrite('saliency map ch1.jpg', ch1)
        cv2.imwrite('saliency map ch2.jpg', ch2)
        cv2.imwrite('saliency map ch3.jpg', ch3)
        proc_img = image_to_saliency.merge_saliency_maps(proc_img)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'preprocess_compress':
        print('--compressing image---')
        proc_img = preprocess_compress.preprocess_compress_image(args.input_image_path,)
        image_saving.save_image(args.output_path,proc_img)
    elif args.convert == 'image_2_midi':
        image = cv2.imread(args.input_image_path)
        proc_img = preprocess_compress.preprocess_compress_image(image,)

        print('--converting image to midi---')
        binarized_img = binarization.binarize_image(config_data, proc_img)
        print('1/5 steps completed')
        edge_map = edge_detection.detect_edges(config_data, binarized_img)
        print('2/5 steps completed')
        saliency_map, _, _, _ = image_to_saliency.generate_per_channel_saliency(config_data, proc_img)
        print('3/5 steps completed')
        saliency_map = image_to_saliency.merge_saliency_maps(saliency_map)
        print('4/5 steps completed')
        image_to_midi.create_midi_from_arrays(config_data, edge_map, saliency_map, args.output_path)
        print('5/5 steps completed: MIDI file successfully generated.')


    elif args.convert == 'all': # run all functions
        print('--full processing---')
        image = cv2.imread(args.input_image_path)
        proc_img = preprocess_compress.preprocess_compress_image(image,)

        print('--converting image to midi---')
        binarized_img = binarization.binarize_image(config_data, proc_img)
        print('1/5 steps completed')
        edge_map = edge_detection.detect_edges(config_data, binarized_img)
        print('2/5 steps completed')
        saliency_map, _, _, _ = image_to_saliency.generate_per_channel_saliency(config_data, proc_img)
        print('3/5 steps completed')
        saliency_map = image_to_saliency.merge_saliency_maps(saliency_map)
        print('4/5 steps completed')
        image_to_midi.create_midi_from_arrays(config_data, edge_map, saliency_map, args.output_path)
        print('5/5 steps completed: MIDI file successfully generated.')
        if args.save_intermediate == True:
            base_path = os.path.dirname(args.output_path)  # Get the directory part of output_path
            print('Intermediate images will be saved in the same directory as the output file: ', base_path)

            image_saving.save_image(base_path + '/compressed_img.jpg',proc_img)
            image_saving.save_image(base_path + '/binarized_img.jpg',binarized_img)
            image_saving.save_image(base_path +'/edge_map.jpg',edge_map)
            image_saving.save_image(base_path +'/saliency_map.jpg',saliency_map)
    else:
        print('Invalid conversion type.')

if __name__ == '__main__':
    main()
