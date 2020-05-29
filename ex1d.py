import cv2
import ex1a as ex1a

def bitwise_splicing(im, plane):
    i = (7 + 0) - (plane - 1) # maps plane to byte index
    h, w = im.shape[0], im.shape[1]
    for y in range(0, h):
        for x in range(0, w):
            byte = '{0:08b}'.format(im[y,x])
            im[y, x] = 255 if byte[i] == '1' else 0

def main():
    im = cv2.imread("images/lena.png", 0)  # loads image
    ims = ex1a.split_into_4(im)
    for i in range(0, 4):
        bitwise_splicing(ims[i], 8)
        cv2.imshow('Lena (' + str(i + 1) + ')', ims[i])
    cv2.waitKey()

if __name__ == '__main__':
    main()