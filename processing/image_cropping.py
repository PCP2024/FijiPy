#from dataio.image_loader import image_loader
import cv2
import json
import os

#with open("data_file.json", "r") as read_file:
#    data = json.load(read_file)

################################################
def image_cropping(image, width, height, x=0, y=0):
        """
        Crop image into a desired size.

        Args:
            image (ndarray): Input image.
            width (int): Width of the crop region.
            height (int): Height of the crop region.
            x (int, optional): X-coordinate of the top-left corner of the crop region. Defaults to 0.
            y (int, optional): Y-coordinate of the top-left corner of the crop region. Defaults to 0.
            
        Returns:
            ndarray: Cropped image.
        """
        if image.shape[0] < height or image.shape[1] < width:
            raise ValueError("The crop region is larger than the image.")
        if image.shape[0] < height + y or image.shape[1] < width + x:
            raise ValueError("The crop region is out of the image.")
                
        # Crop the image
        cropped_image = image[y:y+height, x:x+width]
        return cropped_image

############################################
# test the function above
data_dir = '..' + os.sep + 'demodata'  + os.sep
image_path = data_dir + 'demo_Image.jpg'
image = cv2.imread(image_path) # Load the image
#image = image_loader(image_path) # Load the image
width = 100
height = 100
x=100
y=100
cropped_image = image_cropping(image, width, height, x, y)
image_cropped_path = data_dir + 'demo_Image_cropped.jpg'
cv2.imwrite(image_cropped_path, cropped_image)
