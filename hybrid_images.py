import typing as T
import numpy as np
import cv2
import imageio

# Do not import additional modules, otherwise, there will be deductions

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
    high_imp = cv2.imread(image_high)
    low_imp = cv2.imread(image_low)

    # convert both images to grayscale
    high_gray = cv2.cvtColor(high_imp, cv2.COLOR_BGR2GRAY)
    low_gray = cv2.cvtColor(low_imp, cv2.COLOR_BGR2GRAY)

    # generate low-pass filter using a gausian blur filter
    kernel_size = int(2*7+1)
    kernel = cv2.getGaussianKernel(kernel_size,7) # change value of gaussian kernel
    kernel = np.outer(kernel, kernel)

    filtered_low = cv2.filter2D(low_gray, -1, kernel) # apply gaucian 
    filtered_high = cv2.filter2D(high_gray, -1, kernel) # apply gaucian

    high_frequency = low_gray - filtered_low # remove low freuency to get high frequency

    hybrid_output = filtered_high + high_frequency

    # save and write the image
    imageio.imwrite(output_file, hybrid_output)

    return hybrid_output

    raise NotImplementedError()


if __name__ == "__main__":
    image = hybrid_images("image_high.png", "image_low.png", "image_hybrid.png")  # Find images on your own
    print(image.shape)
