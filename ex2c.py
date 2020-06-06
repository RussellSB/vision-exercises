import cv2
import numpy as np
from skimage.exposure import rescale_intensity
import ex2b as ex2b

def get_kernel_bilinear():
    bilinear = 1/9 * np.array((
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]), dtype="float32")
    return bilinear

def get_kernel_sobelY():
    sobelY = np.array((
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]), dtype="int")
    return sobelY

def get_kernel_sobelX():
    sobelX = np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")
    return sobelX

def get_kernel_gaussian():
    gauss = np.array((
        [1/16, 1/8, 1/16],
        [1/8, 1/4, 1/8],
        [1/16, 1/8, 1/16]), dtype='float32')
    return gauss

def main():
    im = cv2.imread("images/lena.png", 0)

    cv2.imshow('Original', im)
    cv2.waitKey(0)

    kernel = get_kernel_sobelX()
    sobx = ex2b.convolve(im, kernel)
    cv2.imshow('Sobel X', sobx)
    cv2.waitKey(0)

    kernel = get_kernel_sobelY()
    soby = ex2b.convolve(im, kernel)
    cv2.imshow('Sobel Y', soby)
    cv2.waitKey(0)

    kernel = get_kernel_gaussian()
    gauss = ex2b.convolve(im, kernel)
    cv2.imshow('Gaussian', gauss)
    cv2.waitKey(0)

    kernel = get_kernel_bilinear()
    bil = ex2b.convolve(im, kernel)
    cv2.imshow('Bilinear', bil)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()