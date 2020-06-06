import cv2

# Demonstrates sliding window over an image, with padding
def slide_window(im, n, s, verbose=False, speed=30):
    (kw, kh) = (n, n)             # kernel width and height

    pad = (kw - 1) // 2
    im = cv2.copyMakeBorder(im, pad, pad, pad, pad, cv2.BORDER_CONSTANT)  # Applies padding to convolve edges
    ih, iw = im.shape[:2]  # padded image width and height

    cv2.imshow('Padded', im)
    cv2.waitKey(0)

    im_r = im[pad: ih - pad, pad: iw - pad]  # Removes padding
    cv2.imshow('Padding can be removed after', im_r)
    cv2.waitKey(0)

    for y in range(0, im.shape[0] + pad, s):
        for x in range(0, im.shape[1] + pad, s):
            if(verbose):
                cv2.rectangle(im, (x, y), (x + kw, y + kh), (0, 0, 255), 2)  # Draws active window
                cv2.imshow('Sliding Window (Preparing areas for convolution)', im)
                cv2.waitKey(speed)
                cv2.rectangle(im, (x, y), (x + kw, y + kh), (255, 0, 0), 2)  # Draws traversed window

def main():
    im = cv2.imread("images/lena.png", 1)
    slide_window(im, 50, 50, verbose=True)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()