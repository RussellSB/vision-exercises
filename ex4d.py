import cv2

# TODO
def main():
    im = cv2.imread("images/3_colour.jpeg", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original 1', im)
    cv2.waitKey(0)

    im = cv2.imread("images/2_colour.jpeg", 1)  # loads image
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Original 2', im)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()