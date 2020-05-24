import cv2
import ex1a as ex1a
import ex1b as ex1b
import ex1c as ex1c
import matplotlib
from matplotlib import pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    while (True):
        ret, im = cap.read()
        ims = ex1a.split_into_4(im)
        for i in range(0, 4):
            ims[i] = ex1c.power_transform(ims[i], 2.2)
            cv2.imshow('Segment '+str(i+1), ims[i])
        ex1b.calcHistograms_RGB(ims)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()