import cv2
import ex1a as ex1a
import ex3a as ex3a
import ex3b as ex3b
import ex3c as ex3c
import ex3d as ex3d
import ex3e as ex3e

def segment(im):

    im = ex3d.open(im, 1, 1)
    im = ex3e.close(im, 1, 1)
    im = ex3a.four_connected_components_labelling(im)

    cv2.imshow('4-Connectivity', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return im

def main():
    im = cv2.imread("images/text.png", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 127)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    im = segment(im)

if __name__ == '__main__':
    main()