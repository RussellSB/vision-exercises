import cv2
import numpy as np
import ex1a as ex1a

def power_transform(im, gamma, c=255):
    return np.array(c * (im / c) ** gamma, dtype='uint8')

def main():
    im = cv2.imread("images/lena.png", 0)  # loads image
    ims = ex1a.split_into_4(im)
    for i in range(0, 4):
        ims[i] = power_transform(ims[i], 0.3)
        cv2.imshow('Lena (' + str(i + 1) + ')', ims[i])
    cv2.waitKey()

if __name__ == '__main__':
    main()