import cv2
import ex1a as ex1a
import ex3b as ex3b
import ex3c as ex3c

def close(im, k1, k2):
    im = ex3b.dilate(im, k1)
    im = ex3c.erode(im, k2)

    return im

def main():
    im = cv2.imread("images/text.png", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 127)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    im = close(im, k1=1, k2=1)
    cv2.imshow('Closing', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()