import cv2

def resize(im, percentage):
    w = int(im.shape[1] * percentage / 100)
    h = int(im.shape[0] * percentage / 100)
    dim = (w, h)
    # resize image
    return cv2.resize(im, dim, interpolation=cv2.INTER_AREA)

def feature_match(im1, im2):
    orb = cv2.ORB_create(nfeatures=10000)  # (set to more than default to include second book features)

    kp1, des1 = orb.detectAndCompute(im1, None)
    kp2, des2 = orb.detectAndCompute(im2, None)

    # Create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # Match descriptors
    matches = bf.match(des1, des2)

    # Sort them in order of their distance
    matches = sorted(matches, key = lambda x:x.distance)

    # Draw first 100 matches
    img3 = cv2.drawMatches(im1, kp1, im2, kp2, matches[:100], None, flags=2)

    return img3

def main():
    im1 = cv2.imread("images/3_colour.jpeg", 1)  # loads image
    im1 = resize(im1, 50)

    cv2.imshow('Original 1', im1)
    cv2.waitKey(0)

    im2 = cv2.imread("images/2_colour.jpeg", 1)  # loads image
    im2 = resize(im2, 50)

    cv2.imshow('Original 2', im2)
    cv2.waitKey(0)

    im = feature_match(im1, im2)
    cv2.imshow('BFMatching - Orb', im)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()