# Hybrid Images

This Python code creates a hybrid image by combining a high-pass filtered version of the first input image with a low-pass filtered version of the second input image. The resulting image is a mixture of the high-frequency content of the first image and the low-frequency content of the second image.

## Code Details

```python
import typing as T
import numpy as np
import cv2
import imageio

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

    # Rest of the code...

# Rest of the code...

if __name__ == "__main__":
    image = hybrid_images("image_high.png", "image_low.png", "image_hybrid.png")
    print(image.shape)
```
## Usage

1. Ensure that you have the following dependencies installed:
   - `typing`
   - `numpy`
   - `cv2`
   - `imageio`

2. Import the required modules:
```python
import typing as T
import numpy as np
import cv2
import imageio
```
  ## References
 [CMU - Andrew Tan](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15463-f12/www/proj2/www/aktan/#:~:text=To%20create%20hybrid%20images%2C%20I,as%20the%20low%20frequency%20image.)\
 [CMU - Esha Uboweja](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15463-f13/www/proj2/www/euboweja/)
