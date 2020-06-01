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

def find_union(mini, maxi, compenents):
    min_set_i = 0
    max_set_i = 0

    for i in range (0, len(compenents)):
        set = compenents[i]
        if mini in set:
            min_set_i = i

    for i in range (0, len(compenents)):
        set = compenents[i]
        if maxi in set:
            max_set_i = i


    if max_set_i != min_set_i:
        print(min_set_i, max_set_i)
        compenents[min_set_i] = compenents[min_set_i].union(compenents[max_set_i])
        del compenents[max_set_i]
    return compenents

def four_connected_components_labelling(im):
    h, w = im.shape[0], im.shape[1]

    im_labels = np.zeros(im.shape, dtype='uint8')
    new_label_cnt = 1  # Keeps track of the newest component group
    components = []

    # 1st pass
    for y in range(0, h):
        for x in range(0, w):
            hasTop = has_neighbour(im_labels, y - 1, x)
            hasLeft = has_neighbour(im_labels, y, x - 1)

            if(x == 126 and y == 76):
                print("debug")

            if (im[y, x] != 0):
                if(not hasTop and not hasLeft):
                    im_labels[y, x] = new_label_cnt
                    components.append({new_label_cnt})
                    new_label_cnt += 1
                else:
                    if (hasLeft and not hasTop):
                        im_labels[y, x] = im_labels[y, x - 1]
                    elif (hasTop and not hasLeft):
                        im_labels[y, x] = im_labels[y - 1, x]
                    elif (hasTop and hasLeft):
                        top = im_labels[y - 1, x]
                        left = im_labels[y, x - 1]
                        if(top != left):
                            (mini, maxi) = (left,top) if left < top else (top, left)
                            im_labels[y, x] = mini
                            components = find_union(mini, maxi, components)


    print('=============')

    # 2nd pass
    # TODO

    cv2.imshow('4-Connectivity', im_labels)
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