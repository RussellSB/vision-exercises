import cv2

def slide_window(im, n, s, verbose=False, speed=30):
    im_tmp = im.copy()
    (w, h) = (n, n)
    windows = []            # list to store windows by [y0, y1, x0, x1]

    for y in range(0, im.shape[0] - h, s):
        for x in range(0, im.shape[1] - w, s):
            windows.append([y, y+h, x, x+w])
            if(verbose):
                cv2.rectangle(im_tmp, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Draws active window
                cv2.imshow('Sliding Window   ', im_tmp)
                cv2.waitKey(speed)
                cv2.rectangle(im_tmp, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draws traversed window
    return windows

def main():
    im = cv2.imread("images/community.jpg", 1)
    slide_window(im, 50, 50, verbose=True)

if __name__ == '__main__':
    main()