import cv2
import numpy as np
from skimage.exposure import rescale_intensity
import ex2b as ex2b

# TODO: Rephrase (IMPROVE w/ pseudocode in slides)
def kernel_Gaussian(size, sigma=1):
    x0 = y0 = size // 2

    x = np.arange(0, size, dtype=float)
    y = np.arange(0, size, dtype=float)[:, np.newaxis]
    x -= x0
    y -= y0

    exp_formula = (x ** 2 + y ** 2) / (2 * sigma ** 2)
    return 1 / (2 * np.pi * sigma ** 2) * np.exp(-exp_formula)

def main():
    im = cv2.imread("images/lena.png", 1)

    #sobelx = ex2b.convolve(im, ex2b.kernel_SerbelX())
    #sobely = ex2b.convolve(im, ex2b.kernel_SerbelY())
    gaussian = ex2b.convolve(im, kernel_Gaussian(3, 1))

    cv2.imshow("Original", im)
    #cv2.imshow("Convolution - Sobel XY", sobelx + sobely)
    cv2.imshow("Convolution - Gaussian", gaussian)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/


