import cv2
import ex1a as ex1a
import numpy as np

# Returns True for presence and False for absence
def has_neighbour(im_labels, y, x):
    try:
        if(im_labels[y, x] != 0):
            return True
        else:
            return False
    except (IndexError, ValueError):
        return False

def four_connected_components_labelling(im):
    h, w = im.shape[0], im.shape[1]

    # Dictionary of labels of pixels
    im_labels = np.zeros(im.shape, dtype='uint8')
    new_label_cnt = 1  # Keeps track of the newest component group
    for y in range(0, h):
        for x in range(0, w):
            hasTop = has_neighbour(im_labels, y - 1, x)
            hasBottom = has_neighbour(im_labels, y + 1, x)
            hasLeft = has_neighbour(im_labels, y, x - 1)
            hasRight = has_neighbour(im_labels, y, x + 1)

            if(x == 126 and y == 76):
                print("debug")

            if (im[y, x] != 0):
                if(not hasTop and not hasBottom and not hasLeft and not hasRight):
                    im_labels[y, x] = new_label_cnt
                    print(new_label_cnt)
                    new_label_cnt += 1
                else:
                    if(hasBottom):
                        im_labels[y, x] = im_labels[y + 1, x]
                    if (hasRight):
                        im_labels[y, x] = im_labels[y, x + 1]
                    if (hasTop):
                        im_labels[y, x] = im_labels[y - 1, x]
                    if (hasLeft):
                        im_labels[y, x] = im_labels[y, x - 1]

    # cv2.imshow('4-Connectivity', im_labels)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    print('debug')


def main():
    im = cv2.imread("images/shapes.jpg", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 127)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    four_connected_components_labelling(im)

if __name__ == '__main__':
    main()