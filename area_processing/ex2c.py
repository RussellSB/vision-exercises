import cv2
import numpy as np
from skimage.exposure import rescale_intensity
import ex2b as ex2b

# TODO: Rephrase
def kernel_Gaussian(size_x, size_y=None, sigma_x=1, sigma_y=None):
    if size_y == None:
        size_y = size_x
    if sigma_y == None:
        sigma_y = sigma_x

    x0 = size_x // 2
    y0 = size_y // 2

    x = np.arange(0, size_x, dtype=float)
    y = np.arange(0, size_y, dtype=float)[:, np.newaxis]

    x -= x0
    y -= y0

    exp_part = x ** 2 / (2 * sigma_x ** 2) + y ** 2 / (2 * sigma_y ** 2)
    return 1 / (2 * np.pi * sigma_x * sigma_y) * np.exp(-exp_part)

def main():
    im = cv2.imread("community.jpg", 1)
    ex2b.convolve(im, ex2b.kernel_SerbelX(), 'Serbel-X')
    ex2b.convolve(im, kernel_Gaussian(3, 3), 'Gaussian')

if __name__ == '__main__':
    main()

# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/


