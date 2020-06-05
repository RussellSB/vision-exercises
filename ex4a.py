import cv2

# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html
def cornerHarrisPerform(gray, im):
    dst = cv2.cornerHarris(gray, 5, 3, 0.04) # second param controls neighbourhood
    # Threshold for an optimal value, it may vary depending on the image.
    im[dst > 0.01 * dst.max()] = [0, 0, 255]
    return im

# Compare shapes to Lena with diff strategies
def main():
    im = cv2.imread("images/shapes.jpg", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', cornerHarrisPerform(gray, im))
    cv2.waitKey(0)

    im = cv2.imread("images/lena.png", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', cornerHarrisPerform(gray, im))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()