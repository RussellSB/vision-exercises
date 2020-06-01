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

    print(h, w)

    im_labels = np.zeros(im.shape, dtype='uint8')
    new_label_cnt = 1  # Keeps track of the newest component group
    components = []

    # 1st pass: Create labels and note components
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

                            # Find union sets
                            for i in range(0, len(components)):
                                if maxi in components[i]:  # Removes max element from max set
                                    components[i].remove(maxi)
                                if mini in components[i]:  # Adds max element to min set
                                    components[i].add(maxi)
                            # removes empty sets
                            components[:] = [c for c in components if len(c) > 0]
                        else:
                            im_labels[y, x] = top

    print('1 pass ready')

    # 2nd pass: Globally set labels for each component
    for y in range(0, h):
        for x in range(0, w):
            label = im_labels[y, x]
            for i in range(0, len(components)):
                if label in components[i]:
                    im_labels[y,x] = i+1

    print('2 pass ready')

    # Change image to make labelled components represented as randomly unique colours
    colors = []
    for i in range (0, len(components)):
        colors.append(list(np.random.choice(range(256), size=3)))
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    for y in range(0, h):
        for x in range(0, w):
            b = im[y, x][0]
            g = im[y, x][1]
            r = im[y, x][2]
            if (r != 0 and g != 0 and b != 0):
                im[y, x] = colors[im_labels[y, x]  - 1]

    print('=============')

    cv2.imshow('4-Connectivity', im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    im = cv2.imread("images/shapes.jpg", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 20)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    four_connected_components_labelling(im)

if __name__ == '__main__':
    main()