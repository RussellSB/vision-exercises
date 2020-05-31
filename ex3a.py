import cv2
import ex1a as ex1a

class labelledPixel:
    def __init__(self, y, x, label):
        x = x
        y = y
        label = label

def getLabelFromPixel(y, x, labelledPixels):
    for px in labelledPixels:
        if(px.x == x and px.y == y):
            return px.label
    raise IndexError("A specified pixel does not exist")

# Returns True for presence and False for absence
def check_neighbour(im, y, x):
    try:
        if(im[y,x] == 0):
            return False
        else:
            return True
    except (IndexError, ValueError):
        return False

def four_connected_components_labelling(im):
    labelledPixels = []  # labelled pixels
    new_label_cnt = 0  # keeps track of newest group

    h, w = im.shape[0], im.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            hasTop = check_neighbour(im, y - 1, x)
            hasBottom = check_neighbour(im, y + 1, x)
            hasLeft = check_neighbour(im, y, x - 1)
            hasRight = check_neighbour(im, y, x + 1)

            if(not hasTop and not hasBottom and not hasLeft and not hasRight):
                px = labelledPixel(y, x, new_label_cnt)
                labelledPixels.append(px)

            if(hasTop):
                px_top_label = getLabelFromPixel(y - 1, x, labelledPixels)
                px = labelledPixel(y, x, px_top_label)
                labelledPixels.append(px)
            if(hasBottom):
                px_top_label = getLabelFromPixel(y + 1, x, labelledPixels)
                px = labelledPixel(y, x, px_top_label)
                labelledPixels.append(px)
            if(hasLeft):
                px_top_label = getLabelFromPixel(y - 1, x, labelledPixels)
                px = labelledPixel(y, x, px_top_label)
                labelledPixels.append(px)
            if (hasRight):
                px_top_label = getLabelFromPixel(y + 1, x, labelledPixels)
                px = labelledPixel(y, x, px_top_label)
                labelledPixels.append(px)

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