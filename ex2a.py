import cv2

# Demonstrates sliding window over an image, with padding
def slide_window(im, n, s, verbose=False, speed=30):
    (kw, kh) = (n, n)             # kernel width and height
    ih, iw = im.shape[:2]  # padded image width and height

    pad = (kw - 1) // 2
    im = cv2.copyMakeBorder(im, pad, pad, pad, pad, cv2.BORDER_CONSTANT)  # Applies padding to convolve edges

    cv2.imshow('Padded', im)
    cv2.waitKey(0)

    im_r = im[pad: ih - pad, pad: iw - pad]  # Removes padding
    cv2.imshow('Padding can be removed after', im_r)
    cv2.waitKey(0)

    for y in range(pad, im.shape[0] + pad, s):
        for x in range(pad, im.shape[1] + pad, s):
            if(verbose):
                cv2.rectangle(im, (x-pad, y-pad), (x+pad+1, y+pad+1), (0, 0, 255), 2)  # Draws active window
                cv2.imshow('Sliding Window', im)
                cv2.waitKey(speed)
                cv2.rectangle(im, (x-pad, y-pad), (x+pad+1, y+pad+1), (255, 0, 0), 2)  # Draws traversed window

def main():
    im = cv2.imread("images/lena.png", 1)
    slide_window(im, 50, 10, verbose=True)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()