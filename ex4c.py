import cv2

def orb(im):
    orb = cv2.ORB_create(nfeatures=1500)
    keypoints_orb, descriptors = orb.detectAndCompute(im, None)
    im = cv2.drawKeypoints(im, keypoints_orb, None)
    return im

def main():
    im = cv2.imread("images/shapes.jpg", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', orb(im))
    cv2.waitKey(0)

    im = cv2.imread("images/lena.png", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original', im)
    cv2.waitKey(0)
    cv2.imshow('Original', orb(im))
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()