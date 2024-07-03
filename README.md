# image2song

This library converts an image into a song.
For an example of how to use it, run run_main.py

General pipeline:
- image preprocessing (compress, crop, denoise)
- convert the image to a binary file
- obtain saliency map
- obtain midi file
- compile midi

Contents:
- processing: .py files for the pipeline
- dataio: .py files to load images
- demodata: demo image, and results after each processing step 
- tests: tests for each function
- configuration: contains files with arguments for each function. If default arguments are not used, this file gets updated

Usage: 

docker build -t fijipy:latest . # Create a docker image from Docker file. (Do this at the top directory.)
docker run fijipy:latest  input_path convertion_type output_path --optional=xxx 
docker cp Container:"/app/output_path" "Destination in your local"

e.g. 
docker run  --name test_fijipy fijipy:latest ./demodata/demo_Image.jpg crop demo_test.jpg
docker cp test_fijipy:"/app/output_path" "./demo_test.jpg"

Once you done, you may want to delete the container. 
