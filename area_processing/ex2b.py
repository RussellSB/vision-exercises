import cv2
import numpy as np
from skimage.exposure import rescale_intensity

def convolve(im, kernel):
    colour_dimensions = len(im.shape)
    if(colour_dimensions > 2):
        return convolve_RGB(im, kernel)
    else:
        return convolve_BW(im, kernel)

def convolve_BW(im, kernel):
    (h_im, w_im) = im.shape[:2]
    (h_kernel, w_kernel) = kernel.shape[:2]

    # For padding
    h = (h_kernel - 1) // 2
    w = (w_kernel - 1) // 2
    im = cv2.copyMakeBorder(im, h, w, h, w, cv2.BORDER_REPLICATE)

    kernel = np.flip(kernel) # flip kernel, for convolution (not correlation)
    out = np.zeros(im.shape)  # initialization
    for y in range(h, h_im + h):
        for x in range(w, w_im + w):
            roi = im[y - h:y + h + 1, x - w:x + w + 1]  # extract by center region
            conv = (roi * kernel).sum()  # perform convolution operation
            out[y - h, x - w] = conv  # store convolved region in out


    out = rescale_intensity(out, in_range=(0, 255))
    out = (out * 255).astype("uint8")
    return out

def convolve_RGB(im, kernel):
    color = ('b', 'g', 'r')
    (h_im, w_im) = im.shape[:2]
    (h_kernel, w_kernel) = kernel.shape[:2]

    # For padding
    h = (h_kernel - 1) // 2
    w = (w_kernel - 1) // 2
    im = cv2.copyMakeBorder(im, h, w, h, w, cv2.BORDER_REPLICATE)

    kernel = np.flip(kernel) # flip kernel, for convolution (not correlation)
    out = np.zeros(im.shape)  # initialization
    for y in range(h, h_im + h):
        for x in range(w, w_im + w):
            roi = im[y - h:y + h + 1, x - w:x + w + 1]  # extract by center region
            for n, _ in enumerate(color):
                conv = (roi[n] * kernel).sum()  # perform convolution operation on color channel
                out[y - h, x - w, n] = conv  # store convolved region in out

    for n, _ in enumerate(color):
        out[:,:,n] = rescale_intensity(out[:,:,n], in_range=(0, 255))
        out[:,:,n] = (out[:,:,n] * 255).astype('uint8')
    out = out.astype('uint8')
    return out

# 1/8 for right derivatives
def kernel_SerbelX():
    sobelX = 1/8 * np.array((
        [1, 2, 1],
        [0, 0, 0],
        [-1, -2, -1]), dtype="int")
    return sobelX

# 1/8 for right derivatives
def kernel_SerbelY():
    sobelY = 1/8 * np.array((
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]), dtype="int")
    return sobelY

def main():
    im = cv2.imread("community.jpg", 0)
    r = cv2.selectROI('Select a region of interest', im, False, False)
    roi = im[int(r[1]): int(r[1] + r[3]), int(r[0]):int(r[0] + r[2])]
    sobelx = convolve(roi, kernel_SerbelX())
    sobely = convolve(roi, kernel_SerbelY())

    cv2.imshow("Convolution - Sobel X", sobelx)
    cv2.imshow("Convolution - Sobel Y", sobely)
    cv2.imshow("Convolution - Sobel XY", sobelx + sobely)
    cv2.waitKey()

if __name__ == '__main__':
    main()

# https://www.pyimagesearch.com/2016/07/25/convolutions-with-opencv-and-python/