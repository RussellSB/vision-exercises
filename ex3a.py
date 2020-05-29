import cv2
import ex1a as ex1a

def four_connected_components_labelling(im):
    cv2.imshow('4-Connectivity', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    im = cv2.imread("images/shapes.jpg", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 127)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    four_connected_components_labelling(im)

if __name__ == '__main__':
    main()