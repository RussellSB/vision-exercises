import cv2
import ex1a as ex1a
import ex3a as ex3a

def erode(im, k):
    h, w = im.shape[0], im.shape[1]

    for i in range(k):
        for y in range(0, h):
            for x in range(0, w):
                if (im[y, x] == 255):
                    hasTop = ex3a.has_neighbour(im, y - 1, x)
                    hasLeft = ex3a.has_neighbour(im, y, x - 1)
                    hasBottom = ex3a.has_neighbour(im, y + 1, x)
                    hasRight = ex3a.has_neighbour(im, y, x + 1)

                    hasTopLeft = ex3a.has_neighbour(im, y - 1, x - 1)
                    hasTopRight = ex3a.has_neighbour(im, y - 1, x + 1)
                    hasBottomLeft = ex3a.has_neighbour(im, y + 1, x - 1)
                    hasBottomRight = ex3a.has_neighbour(im, y + 1, x + 1)

                    if (hasTop == 0 or hasLeft == 0 or hasRight == 0 or hasBottom == 0 or
                    hasTopLeft == 0 or hasTopRight == 0 or hasBottomLeft == 0 or hasBottomRight == 0):
                        im[y, x] = 2

        for y in range(0, h):
            for x in range(0, w):
                if (im[y, x] == 2):
                    im[y, x] = 0

    cv2.imshow('Erosion', im)
    cv2.waitKey(0)

    return im

def main():
    im = cv2.imread("images/shapes.jpg", 0)  # loads image
    im = (255 - im) # inverts image
    ex1a.binary_threshold(im, 20)

    cv2.imshow('Binarized image', im)
    cv2.waitKey(0)

    erode(im, k=10)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()