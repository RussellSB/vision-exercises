import cv2
import ex1a as ex1a

BACKGROUND_LBL = -100000

# Returns True for presence and False for absence
def check_neighbour(im, pixelLabels, y, x):
    try:
        if(im[y,x] == 0 or pixelLabels[hash_function(y,x) == BACKGROUND_LBL]):
            return False
        else:
            return True
    except (IndexError, ValueError):
        return False

def hash_function(y, x):
    return y - x

def four_connected_components_labelling(im):
    h, w = im.shape[0], im.shape[1]

    # Dictionary of labels of pixels
    pixelLabels = {}
    new_label_cnt = 0  # Keeps track of the newest component group
    for y in range(0, h):
        for x in range(0, w):
            hasTop = check_neighbour(im, pixelLabels, y - 1, x)
            hasBottom = check_neighbour(im, pixelLabels, y + 1, x)
            hasLeft = check_neighbour(im, pixelLabels, y, x - 1)
            hasRight = check_neighbour(im, pixelLabels, y, x + 1)

            if(x == 126 and y == 76):
                print("debug")

            if (im[y, x] == 0): # Label background as -1000000
                pixelLabels[hash_function(y, x)] = BACKGROUND_LBL
            else: # Label foreground with various groups
                if(not hasTop and not hasBottom and not hasLeft and not hasRight):
                    pixelLabels[hash_function(y, x)] = new_label_cnt
                    new_label_cnt += 1

                if(hasBottom):
                    label_bottom = pixelLabels[hash_function(y + 1, x)]
                    pixelLabels[hash_function(y, x)] = label_bottom
                if (hasRight):
                    label_right = pixelLabels[hash_function(y, x + 1)]
                    pixelLabels[hash_function(y, x)] = label_right
                if (hasTop):
                    label_top = pixelLabels[hash_function(y - 1, x)]
                    pixelLabels[hash_function(y, x)] = label_top
                if (hasLeft):
                    label_left = pixelLabels[hash_function(y, x - 1)]
                    pixelLabels[hash_function(y, x)] = label_left

    # Modify image for display
    im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR)
    for y in range(0, h):
        for x in range(0, w):
            if(pixelLabels[hash_function(y, x)] != BACKGROUND_LBL):
                print(y, x)
                im[y, x] = (225,0,0)

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