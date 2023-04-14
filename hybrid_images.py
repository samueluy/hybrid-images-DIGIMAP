import typing as T
import numpy as np
import cv2
import imageio

# Do not import additional modules, otherwise, there will be deductions

# Other references:
# https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15463-f12/www/proj2/www/aktan/#:~:text=To%20create%20hybrid%20images%2C%20I,as%20the%20low%20frequency%20image.
# https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15463-f13/www/proj2/www/euboweja/
# https://chat.openai.com/

def hybrid_images(image_high: T.Union[str, np.ndarray], image_low: T.Union[str, np.ndarray], output_file: str = None) -> np.ndarray:
    """
    Creates a hybrid image by combining a high-pass filtered version of the first input image
    with a low-pass filtered version of the second input image. The resulting image is a
    mixture of the high-frequency content of the first image and the low-frequency content of
    the second image.

    Args:
        image_high (Union[str, np.ndarray]): The first input image, either a filename (str) or a numpy array of shape CxHxW.
        image_low (Union[str, np.ndarray]): The second input image, either a filename (str) or a numpy array of shape CxHxW.
        output_file (str, optional): The filename to save the resulting image if not None.

    Returns:
        np.ndarray: The resulting hybrid image, as a numpy array (always returns a value)
    """

    # import images
    first_image = cv2.imread(image_high)
    second_image = cv2.imread(image_low)

    # convert both images to grayscale
    # Ref: https://techtutorialsx.com/2018/06/02/python-opencv-converting-an-image-to-gray-scale/
    high_gray = cv2.cvtColor(first_image, cv2.COLOR_BGR2GRAY)
    low_gray = cv2.cvtColor(second_image, cv2.COLOR_BGR2GRAY)

    # generate low-pass filter using a gausian blur filter

    # Gaussian blur
    # Ref: https://www.geeksforgeeks.org/python-image-blurring-using-opencv/, https://chat.openai.com/
    kernel_size = (31, 31) # kernel size for gaussian -> more blur
    sigma = 10
    filtered_low = cv2.GaussianBlur(low_gray, kernel_size, sigma, cv2.BORDER_DEFAULT)
    filtered_high = cv2.GaussianBlur(high_gray, kernel_size, sigma, cv2.BORDER_DEFAULT)

    high_frequency = high_gray - filtered_high 
    hybrid_output = filtered_low + high_frequency

    # save and write the image
    imageio.imwrite(output_file, hybrid_output)
    return hybrid_output
if __name__ == "__main__":
    image = hybrid_images("image_high.png", "image_low.png", "image_hybrid.png")  # Find images on your own
    print(image.shape)
