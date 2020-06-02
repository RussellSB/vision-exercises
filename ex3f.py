import cv2
import ex1a as ex1a
import ex3a as ex3a
import ex3b as ex3b
import ex3c as ex3c
import ex3d as ex3d
import ex3e as ex3e
import numpy as np

def close_cv2(im, kernel, iterations):
    im = cv2.dilate(im, kernel, iterations)
    im = cv2.erode(im, kernel, iterations)
    return im

def open_cv2(im, kernel, iterations):
    im = cv2.erode(im, kernel, iterations)
    im = cv2.dilate(im, kernel, iterations)
    return im

def segment_lines(im):

    # opening closing opening was found to work best !!!

    kernel = np.ones((8, 1), np.uint8)
    im = open_cv2(im, kernel, 5) # spaces vertically
    #cv2.imshow('Opened', im)
    #cv2.waitKey(0)

    kernel = np.ones((1, 150), np.uint8)
    im = close_cv2(im, kernel, 50) # joins horizontally
    #cv2.imshow('Closed', im)
    #cv2.waitKey(0)

    kernel = np.ones((3, 1), np.uint8)
    im = open_cv2(im, kernel, 50)  # spaces vertically again (as closing horizontally affects vertical a little)
    #cv2.imshow('Opened', im)
    #cv2.waitKey(0)

    im = ex3a.four_connected_components_labelling(im) # can be improved with eight connected components
    #cv2.imshow('Segmented', im)
    #cv2.waitKey(0)

    #contours, hierarchy = cv2.findContours(im.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    #cv2.imshow('Results', im)
    #cv2.waitKey(0)

    return im

def mask_segmented_lines(im, segmented):
    h, w = im.shape[0], im.shape[1]
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)

    for y in range(0, h):
        for x in range(0, w):
            b = im[y, x][0]
            g = im[y, x][1]
            r = im[y, x][2]
            if(r != 0 and g != 0 and b != 0):
                im[y,x] = segmented[y,x]

    return im

def main():
    im = cv2.imread("images/text.png", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 127)

    segmented = segment_lines(im)
    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)
    cv2.imshow('Line area segmentations', segmented)
    cv2.waitKey(0)

    im = mask_segmented_lines(im, segmented)
    im = (255 - im)  # inverts image
    cv2.imshow('Segmented image', im)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()