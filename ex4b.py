import cv2
import numpy as np

# Shin Tomasi corner detector
# https://www.programcreek.com/python/example/89311/cv2.goodFeaturesToTrack
def goodFeaturesToTack(gray, im):
    corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
    corners = np.int0(corners)
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(im, (x, y), 3, [0, 0, 255], -1)
    return im

def main():
    im = cv2.imread("images/shapes.jpg", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', goodFeaturesToTack(gray, im))
    cv2.waitKey(0)

    im = cv2.imread("images/lena.png", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', goodFeaturesToTack(gray, im))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()