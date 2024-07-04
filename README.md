# image2song

This library converts an image into a song.
For an example of how to use it, run run_main.py

## General pipeline
- image preprocessing (compress, crop, denoise)
- convert the image to a binary file
- obtain saliency map
- obtain midi file
- compile midi

## Contents
- processing: .py files for the pipeline
- dataio: .py files to load images
- demodata: demo image, and results after each processing step 
- tests: tests for each function
- configuration: contains files with arguments for each function. If default arguments are not used, this file gets updated


## Usage
### Option 1: in your python environment    
```console
pip install -r requirements.txt # install all packages
python run_main.py input_path convertion_type output_path --optional=xxx 
```

e.g.
```console
pip install -r requirements.txt # install all packages
python run_main.py ./demodata/demo_Image.jpg crop demo_test.jpg
```

### Option 2: Docker
```console
docker build -t fijipy:latest . # Create a docker image from Docker file. (Do this at the top directory.)
docker run fijipy:latest  input_path convertion_type output_path --optional=xxx 
docker cp Container:"/app/output_path" "Destination in your local"
```
e.g. 
```console
docker build -t fijipy:latest . 
docker run --name test_fijipy fijipy:latest ./demodata/demo_Image.jpg crop demo_test.jpg
docker cp test_fijipy:"/app/demo_test.jpg" "./demo_test.jpg"
```


```console
docker restart test_fijipy # start your container 
docker cp image.jpg test_fijipy:"/app/demodata/image.jpg" # copy your image.jpg to demodata in your container. 
docker exec test_fijipy python run_main.py ./demodata/image.jpg image_2_midi demo_test.jpg # convert image to midi ()
```
Once you done, you may want to delete the container. 
