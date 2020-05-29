import cv2

def split_into_4(im):
    h, w = im.shape[:2]
    im1 = im[0:int(h / 2), 0:int(w / 2)]
    im2 = im[0:int(h / 2), int(w / 2):w]
    im3 = im[int(h / 2):h, 0:int(w / 2)]
    im4 = im[int(h / 2):h, int(w / 2):w]
    return [im1, im2, im3, im4]

def binary_threshold(im, value):
    h, w = im.shape[0], im.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            im[y, x] = 255 if im[y, x] >= value else 0

def main():
    im = cv2.imread("images/lena.png", 0) # loads image
    ims = split_into_4(im)
    for i in range(0, 4):
        binary_threshold(ims[i], 127)
        cv2.imshow('Lena ('+str(i+1)+')', ims[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()