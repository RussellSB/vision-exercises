import cv2
import numpy as np
from skimage.exposure import rescale_intensity
import ex2b as ex2b

# TODO: Rephrase (IMPROVE w/ pseudocode in slides)
def kernel_Gaussian(size, fwhm=10, center=None):
    x = np.arange(0, size, dtype=float)
    y = x[:,np.newaxis]

    if center is None:
        x0 = y0 = size // 2
    else:
        x0 = center[0]
        y0 = center[1]

    x -= x0
    y -= y0

    return np.exp(-4 * np.log(2) * ((x - x0) ** 2 + (y - y0) **2) / fwhm **2)

# https://gist.github.com/andrewgiessel/4635563

def main():
    im = cv2.imread("community.jpg", 1)

    #sobelx = ex2b.convolve(im, ex2b.kernel_SerbelX())
    #sobely = ex2b.convolve(im, ex2b.kernel_SerbelY())
    gaussian = ex2b.convolve(im, kernel_Gaussian(3))

    cv2.imshow("Original", im)
    #cv2.imshow("Convolution - Sobel XY", sobelx + sobely)
    cv2.imshow("Convolution - Gaussian", gaussian)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/


