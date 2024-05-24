import argparse
import json
from configuration import write_config
from processing import binarization 
from processing import edge_detection
from processing import image_denoising
from processing import dilation

# to-do: 
# 1. I tried to add --config argument to specify the configuration file, but it did not work. 
# 2. Uncomment lines to run the functions. 

def main(): 
    # call configuration file (data_file.json)
    
    parser = argparse.ArgumentParser(
        description='Convert image to song.', \
        epilog='By PCP 2024 FijiPy')
    
    # to-do 1
    #parser.add_argument('--config', type=str, help='Path to the configuration file.', default='data_file.json')    
    #with open(parser.parse_args().config, "r") as read_file:
    #    config_data = json.load(read_file)

    config_file = 'data_file.json'
    with open(config_file, "r") as read_file:
        config_data = json.load(read_file)
    
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
    
    # optional arguments
    parser.add_argument('--version', \
                        type=str, \
                        help='Show version.', \
                        default='False')
    # denoising
    parser.add_argument('--kernel_size', \
                        type=int, \
                        help='For denoising. Kernel size. default: 3', \
                        default=config_data['kernel_size'])
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

    args = parser.parse_args()

    if args.version == 'True': 
        with open('VERSION', 'r') as f:
            print('version: ' + f.read())

    # overwrite the user-specified value in the configuration file.
    for key, value in vars(args).items():
        # if the key is in the configuration file, update the value.
        if key in config_data: 
            write_config.update_json_file(config_file, \
                                        key, \
                                        value)

    # to-do 2
    # run specified fuction
    if args.convert == 'binarization':
        print('--binarizing image---')
        #binarization.binarize_image(args.config)
    elif args.convert == 'edge_detection':
        print('--detecting edge---')
        #edge_detection.detect_edges(args.config)
    elif args.convert == 'denoising':
        print('--denoising image---')
        #image_denoising.denoise_image(args.config)
    elif args.convert == 'dialation':
        print('--dialating image---')
        #dilation.dialate_image(args.config)
    elif args.convert == 'all': # run all functions
        print('not ready yet')
        #binarization.binarize_image(args.config) 
        #preprocessing.detect_edges(args.config)
        #preprocessing.denoise_image(args.config)
        #preprocessing.dialate_image(args.config)
    else:
        print('Invalid conversion type.')

if __name__ == '__main__':
    main()
