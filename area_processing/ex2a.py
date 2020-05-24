import cv2

def slide_window(im, n, s):
    im_tmp = im
    (w, h) = (n, n)
    for y in range(0, im.shape[0] - w, s):
        for x in range(0, im.shape[1] - w, s):
            cv2.rectangle(im_tmp, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draws active window
            cv2.imshow('Community - Sliding Window   ', im_tmp)
            cv2.waitKey()
            cv2.rectangle(im_tmp, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draws traversed window

def main():
    im = cv2.imread("community.jpg", 1)
    slide_window(im, 50, 50)

if __name__ == '__main__':
    main()