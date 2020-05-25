import cv2
import numpy as np
from skimage.exposure import rescale_intensity
import ex2a as ex2a
import ex2b as ex2b
import math

# TODO: Rephrase (IMPROVE w/ pseudocode in slides)
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
    im = cv2.imread("community.jpg", 0)

    sobelx = im.copy()  # initialization
    gaussian = im.copy()  # initialization

    # Traverse through windows of the image
    windows = ex2a.slide_window(im, 50, 50, verbose=False, speed=1)
    for w in windows:
        print(w[0],w[1], w[2],w[3])
        roi = im[w[0]:w[1], w[2]:w[3]]
        roi = ex2b.convolve(roi, ex2b.kernel_SerbelX())
        #gaussian[w[0]:w[1], w[2]:w[3]] = ex2b.convolve(roi.copy(), kernel_Gaussian(3, 3))

    cv2.imshow("Convolution - Sobel X", roi)
    #cv2.imshow("Convolution - Gaussian", gaussian)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()

# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/


