import argparse
import preprocessing 

def main(): 
    parser = argparse.ArgumentParser(description='Convert image to song.')
    parser.add_argument('input_image_path', type=str, help='Path to the input image.')
    parser.add_argument('convert', type=str, help='Type of conversion .')
    parser.add_argument('output_path', type=str, help='Path to the output file (either image or audio).')
    parser.add_argument('--config', type=str, help='Path to the configuration file.', default='data_file.json')
    parser.add_argument('--kernel_size', type=int, help='Size of the kernel for dilation.', default=3)
    parser.add_argument('--binarisation_threshold', type=int, help='Threshold for binarisation.', default=128)
                         
    args = parser.parse_args()
    print('--converting image to song---')

    # update configuration file? 

    # run fuctions?
    if args.convert == 'binarization':

if __name__ == '__main__':
    main()