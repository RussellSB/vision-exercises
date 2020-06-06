import cv2
import numpy as np
from skimage.exposure import rescale_intensity

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

# Performs convolution, sliding over image
def convolve(im, kernel, s=1):
    kernel = kernel.T

    kw, kh = kernel.shape[:2]  # kernel width and height
    ih, iw = im.shape[:2]  # image width and height

    pad = (kw - 1) // 2
    im = cv2.copyMakeBorder(im, pad, pad, pad, pad, cv2.BORDER_CONSTANT)  # Applies padding to convolve edges
    out = np.zeros((ih, iw), dtype='float32')  # Stores output

    for y in range(pad, ih + pad, s):
        for x in range(pad, iw + pad, s):
            roi = im[y-pad : y+pad+1, x-pad : x+pad+1]  # Region of interest
            out[y-pad, x-pad] = (roi * kernel).sum()  # convolve

    out = rescale_intensity(out, in_range=(0, 255))
    out = (out * 255).astype('uint8')

    return out

def main():
    im = cv2.imread("images/shapes.jpg", 0)

    r = cv2.selectROI('Select a region of interest', im, False, False)
    im = im[int(r[1]): int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]

    kernel = get_kernel_sobelX()
    sobx = convolve(im, kernel)
    cv2.imshow('Sobel X', sobx)
    cv2.waitKey(0)

    kernel = get_kernel_sobelY()
    soby = convolve(im, kernel)
    cv2.imshow('Sobel Y', soby)
    cv2.waitKey(0)

    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()