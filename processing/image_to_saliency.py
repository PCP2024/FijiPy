from typing import Tuple

import numpy as np
import scipy
from matplotlib import colors
import cv2
from tqdm import tqdm


def generate_per_channel_saliency(data: dict, image: np.ndarray) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Generates normalized saliency map per channel of an input image

    Parameters
    ----------
    data: dict :
        Extra argument to saliency map calculation: Possible argument includes the
        'patch_size' of type `int`.
    image: Union[str : Image file path.

                 np.ndarray] : Array of size (NxMxC), (NxM) is the size of the image and C=3 for RGB.

    Returns
    -------
    Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray] :
        Normalized saliency with pixel values from 0 to 255 (Array of size (N-(patch_size-1)xM-(patch_size-1)xC),
        (NxM) is the size of the image and C 3 for RGB and 1 for black and white containing normalized saliency values)
        and each of 3 channels' saliency map separately in that order.

    
    """
    if isinstance(image, str):
        image = cv2.imread(image)
    #print("Shape of image into saliency: ", image.shape)
    # import hyperparameters from data json file
    patch_size = data['patch_size']

    hsv_image = colors.rgb_to_hsv(image)
    saliency_maps = np.zeros(
        (hsv_image.shape[0] - patch_size + 1, hsv_image.shape[1] - patch_size + 1, hsv_image.shape[-1]))

    for channel in range(hsv_image.shape[-1]):
        for x in tqdm(np.arange(int(patch_size / 2), hsv_image.shape[0] - int(patch_size / 2)), desc=f'Processing channel {channel+1}/{hsv_image.shape[-1]}'):
            for y in np.arange(int(patch_size / 2), hsv_image.shape[1] - int(patch_size / 2)):
                patch = hsv_image[x - int(patch_size / 2):x + int(patch_size / 2),
                        y - int(patch_size / 2):y + int(patch_size / 2), channel]
                if channel == 1:
                    salience = scipy.stats.circstd(patch, high=1)
                else:
                    salience = np.std(patch)
                saliency_maps[x - int(patch_size / 2), y - int(patch_size / 2), channel] = salience
        saliency_maps[:, :, channel] = saliency_maps[:, :, channel]/np.max(saliency_maps[:, :, channel])

    #print("Shape of saliency map: ", saliency_maps.shape)
    saliency_maps *= 255 # return pixel values in range [0,255]
    return saliency_maps, saliency_maps[:, :, 0], saliency_maps[:, :, 1], saliency_maps[:, :, 2]


def merge_saliency_maps(saliency_maps: np.ndarray) -> np.ndarray:
    """Merges three saliency maps into one by averaging their values.

    Parameters
    ----------
    saliency_maps : np.ndarray :
        Array of size (NxMxC), (NxM) is the size of the image and C is 3 for RGB.
        

    Returns
    -------
    np.ndarray:
        Merged saliency maps
    
    """
    # Calculate the average saliency map across the channels
    merged_map = np.mean(saliency_maps, axis=-1)
    #print("Shape of merged saliency map: ", merged_map.shape)
    return merged_map

# # test the function
# img, saliency_map, saliency_map1, saliency_map2 = generate_per_channel_saliency({'patch_size': 15}, 'demodata/demo_Image.jpg')

# # save the saliency maps to jpg
# cv2.imwrite('demodata/saliency_map1.jpg', saliency_map*255)
# cv2.imwrite('demodata/saliency_map2.jpg', saliency_map1*255)
# cv2.imwrite('demodata/saliency_map3.jpg', saliency_map2*255)
# cv2.imwrite('demodata/saliency_map_full.jpg', img*255)
# cv2.imwrite('demodata/saliency_map_merged.jpg', merge_saliency_maps(img)*255)

# cv2.imwrite('demodata/saliency_map1_ALT.jpg', saliency_map)
# cv2.imwrite('demodata/saliency_map2_ALT.jpg', saliency_map1)
# cv2.imwrite('demodata/saliency_map3_ALT.jpg', saliency_map2)
# cv2.imwrite('demodata/saliency_map_full_ALT.jpg', img)
# cv2.imwrite('demodata/saliency_map_merged_ALT.jpg', merge_saliency_maps(img))

