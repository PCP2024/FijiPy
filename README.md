# image2song

## 1. Description
This library converts an image into a MIDI file by exploiting some of its characteristics to generate notes (edges), their pitch (position along the y axis of the image) and their velocity (saliency of corresponding pixel).

The library is intended to work via a custom-written Command Line Interface.
Individual functions performing transformations on the input image can be either run independently or stacked depending on the type of specified conversion mode.

## 2. Functionality
### 2.1 What's available
- image cropping
- image denoising
- image dilation
- image binarization
- generation of an edge map from image
- generation of per channel, and per image saliency maps
- generation of MIDI score from edge and saliency maps
- full image to MIDI score conversion

### 2.2 Full image to MIDI pipeline
- necessary image preprocessing (resize to fit piano roll space)
- convert the image to a binary file
- obtain edge map from binarized image
- obtain saliency map
- obtain midi file from edge and saliency maps

## 3. Contents
- processing: .py files for the pipeline
- dataio: .py files to load images
- demodata: demo image, and results after each processing step 
- tests: tests for each function
- configuration: contains files with arguments for each function. If default arguments are not used, this file gets updated


## 4. Installation & Basic Usage
The library comes with a `requirements.txt` file that can be used to install all necessary dependencies in a new environment in order to avoid conflicts.

The primary interface with the library happens via `run_main.py`:
```bash
python run_main.py --help # visualize required and optional arguments
```

To process an image in one of the available ways, the base command structure is:
```bash
python run_main.py input_path conversion_type output_path
```
where:
- `input_path` designates the path to input image
- `conversion_type` designates one of the available processing functions or stacks thereof
- `output_path` designates the desired output path of either an image or a `.mid` file

Available conversion modes include:
- `binarization` -> binarize image
- `edge_detection` -> geenrate an edge map from image
- `denoising` -> use either median or Gaussian filtering to denoise image
- `dilation` -> dilate an image using a structuring element of the specified size
- `crop` -> crop an image to a desired size
- `saliency` -> from image, generate one saliency map per RGB channel, and a final saliency map averaged over the three channels
- `preprocess_compress` -> ensure the input image has a diemnsion of max 128 pixels on the y axis in roder to match the max piano roll length
- `image_2_midi` -> generate a MIDI score from image
- `all` -> apply all available processing functions to image

To gather further information about how each voncersion mdoe works, one can consult the docstring of each processing function in the folder `./processing`.

### 4.1 Installation & usage examples
#### Option 1: in your python environment    
```bash
pip install -r requirements.txt # install all packages
python run_main.py input_path convertion_type output_path --optional=xxx 
```

e.g.
```bash
pip install -r requirements.txt # install all packages
python run_main.py ./demodata/demo_Image.jpg crop demo_test.jpg
```

#### Option 2: Docker
```bash
docker build -t fijipy:latest . # Create a docker image from Docker file. (Do this at the top directory.)
docker run fijipy:latest  input_path convertion_type output_path --optional=xxx 
docker cp Container:"/app/output_path" "Destination in your local"
```
e.g. 
```bash
docker build -t fijipy:latest . 
docker run --name test_fijipy fijipy:latest ./demodata/demo_Image.jpg image_2_midi demo_test.mid
docker cp test_fijipy:"/app/demo_test.mid" "./demo_test.mid"
```


```bash
docker restart test_fijipy # start your container 
docker cp image.jpg test_fijipy:"/app/demodata/image.jpg" # copy your image.jpg to demodata in your container. 
docker exec test_fijipy python run_main.py ./demodata/image.jpg crop demo_test.jpg # crop image
```
Once you done, you may want to delete the container. 

## 5. Configuration
This tool provides a wide range of configurable options, which can be specified either directly via command-line arguments or through a configuration file. Below is an explanation of how to use these options effectively.

### 5.1 Using a Configuration File
You can specify a configuration file using the `--config` argument. This file should be in JSON format and contain key-value pairs for the various parameters. **By default, the tool looks for a file named `data_file.json`.**

Example Configuration File (`config.json`):
```json
{
    "denoising_algorithm": "median",
    "kernel_size_gaussian": [5, 5],
    "kernel_size_median": 3,
    "sigma": 1.0,
    "canny_lower_threshold": 100.0,
    "canny_upper_threshold": 120.0,
    "threshold_type": "THRESH_BINARY_OTSU",
    "max_value": 255.0,
    "threshold_value": 50.0,
    "structuring_element_type": "MORPH_RECT",
    "structuring_element_size": [3, 3],
    "dilation_iterations": 2,
    "crop_width": 100,
    "crop_height": 100,
    "crop_x": 0,
    "crop_y": 0,
    "patch_size": 5,
    "time_signature": [4, 4],
    "tempo": 120
}
```

Using the Configuration File:
```bash
python run_main.py --config config.json input_image.jpg output.mid
```

### 5.2 Command-Line Arguments
In addition to (or instead of) using a configuration file, you can specify parameters directly via command-line arguments. The following is a list of all available arguments:

- `--config`: Path to the configuration file. Default is data_file.json.
- `--version`: Show version information. Default is False.
Denoising:
- `--denoising_algorithm`: Denoising algorithm. Default is from config file.
- `--kernel_size_gaussian`: Kernel size of Gaussian filter. Default is from config file.
- `--kernel_size_median`: Kernel size of median filter (int). Default is from config file.
- `--sigma`: Sigma value. Default is from config file.
Edge Detection:
- `--canny_lower_threshold`: Canny lower threshold. Default is from config file.
- `--canny_upper_threshold`: Canny upper threshold. Default is from config file.
Binarisation:
- `--threshold_type`: Threshold type. Default is from config file.
- `--max_value`: Max value for thresholding. Default is from config file.
- `--threshold_value`: Threshold value. Default is from config file.
Dilation:
- `--structuring_element_type`: Structuring element type. Default is from config file.
- `--structuring_element_size`: Structuring element size. Default is from config file.
- `--dilation_iterations`: Number of dilation iterations. Default is from config file.
Image Cropping:
- `--crop_width`: Width of the crop region. Default is from config file.
- `--crop_height`: Height of the crop region. Default is from config file.
- `--crop_x`: X-coordinate of the top-left corner of the crop region. Default is from config file.
- `--crop_y`: Y-coordinate of the top-left corner of the crop region. Default is from config file.
Saliency Detection:
- `--patch_size`: Patch size for saliency detection. Default is from config file.
MIDI Conversion:
- `--time_signature`: Time signature for MIDI. Default is from config file.
- `--tempo`: Tempo for MIDI. Default is from config file.
- `--save_config`: Location and name to save an updated version of the used config file. Default is None.
- `--save_intermediate`: Save intermediate images in the output path if using the option convert 'all'. Default is False.

Example Command-Line Usage:
```bash
python run_main.py --denoising_algorithm gaussian --kernel_size_gaussian [7,7] --sigma 1.5 input_image.jpg output.mid
```

### 5.3 Combined Usage
You can combine the configuration file and command-line arguments. Command-line arguments will override the corresponding values in the configuration file.

Example Combined Usage
```bash
python run_main.py --config config.json --sigma 2.0 input_image.jpg output.mid
```
In this example, all parameters will be loaded from `config.json` except for sigma, which will be set to 2.0.

## 6. License
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

## 7. Authors and Acknowledgments
The project was realized in the context of BCCN's CNN MSc's PCP 2024 course by (in no particular order): Ammar Ibrahim, Bernardo Andrade Ortega, Bianca Ariani, Ghadi El Hasbani, Yohta Kawashima.
