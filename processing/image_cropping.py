#from dataio.image_loader import image_loader
import cv2
import json
import os

with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

################################################
def image_cropping(image, crop_width, crop_height, crop_x=0, crop_y=0):
        """
        Crop image into a desired size.

        Args:
            image (ndarray): Input image.
            crop_width (int): Width of the crop region.
            crop_height (int): Height of the crop region.
            crop_x (int, optional): X-coordinate of the top-left corner of the crop region. Defaults to 0.
            crop_y (int, optional): Y-coordinate of the top-left corner of the crop region. Defaults to 0.
            
        Returns:
            ndarray: Cropped image.
        """
        if image.shape[0] < crop_height or image.shape[1] < crop_width:
            raise ValueError("The crop region is larger than the image.")
        if image.shape[0] < crop_height + crop_y or image.shape[1] < crop_width + crop_x:
            raise ValueError("The crop region is out of the image.")
                
        # Crop the image
        cropped_image = image[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]
        return cropped_image

############################################
# test the function above
data_dir = '..' + os.sep + 'demodata'  + os.sep
image_path = data_dir + 'demo_Image.jpg'
image = cv2.imread(image_path) # Load the image
#image = image_loader(image_path) # Load the image
crop_width = 100
crop_height = 100
crop_x=100
crop_y=100
cropped_image = image_cropping(image, crop_width, crop_height, crop_x, crop_y)
image_cropped_path = data_dir + 'demo_Image_cropped.jpg'
cv2.imwrite(image_cropped_path, cropped_image)
