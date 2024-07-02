import numpy as np
import scipy
from matplotlib import colors
from configuration import config
import cv2


def generate_per_channel_saliency(data: dict, image: np.ndarray) -> np.ndarray:
    """
        Generates normalized saliency map per channel of an input image

        Parameters
        ----------
        image : numpy.ndarray
            Array of size (NxMxC), (NxM) is the size of the image and C 3 for RGB
            and 1 for black and white
        patch_size: int
            size of patch (patch_size x patch_size) to compute each pixel's saliency over

        Returns
        -------
        saliency_map : numpy.ndarray
            Array of size (NxMxC), (NxM) is the size of the image and C 3 for RGB
            and 1 for black and white containing normalized saliency values

    """
    if isinstance(image, str):
        image = cv2.imread(image)

    # import hyperparameters from data json file
    patch_size = data['patch_size']

    hsv_image = colors.rgb_to_hsv(image)
    saliency_maps = np.zeros(
        (hsv_image.shape[0] - patch_size + 1, hsv_image.shape[1] - patch_size + 1, hsv_image.shape[-1]))

    for channel in range(hsv_image.shape[-1]):
        for x in np.arange(int(patch_size / 2), hsv_image.shape[0] - int(patch_size / 2)):
            for y in np.arange(int(patch_size / 2), hsv_image.shape[1] - int(patch_size / 2)):
                patch = hsv_image[x - int(patch_size / 2):x + int(patch_size / 2),
                        y - int(patch_size / 2):y + int(patch_size / 2), channel]
                if channel == 1:
                    salience = scipy.stats.circstd(patch, high=1)
                else:
                    salience = np.std(patch)
                saliency_maps[x - int(patch_size / 2), y - int(patch_size / 2), channel] = salience
        saliency_maps[:, :, channel] = saliency_maps[:, :, channel]/np.max(saliency_maps[:, :, channel])

    return saliency_maps

def merge_saliency_maps(saliency_maps: np.ndarray) -> np.ndarray:
    """
    Merges three saliency maps into one by averaging their values.

    Parameters
    ----------
    saliency_maps : numpy.ndarray
        Array of size (NxMxC), (NxM) is the size of the image and C is 3 for RGB.

    Returns
    -------
    merged_map : numpy.ndarray
        Array of size (NxM) containing the averaged saliency values.
    """
    # Calculate the average saliency map across the channels
    merged_map = np.mean(saliency_maps, axis=-1)
    return merged_map