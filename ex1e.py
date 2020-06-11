import cv2
import ex1a as ex1a
import ex1b as ex1b
import ex1c as ex1c
import matplotlib
from matplotlib import pyplot as plt

def main():
    cap = cv2.VideoCapture(0)
    i = 0

    while (True):
        ret, im = cap.read()
        im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        ims = ex1a.split_into_4(im)

        if(i == 0):
            (fig, ax) = ex1b.initSubPlots(ims)

        for i in range(0, 4):
            ims[i] = ex1a.binary_threshold(ims[i], 127)
            ims[i] = ex1c.power_transform(ims[i], 2.2)
            cv2.imshow('Segment '+str(i+1), ims[i])

        ax = ex1b.calcHistograms_BW(ims, ax)
        fig.canvas.draw()
        fig.canvas.flush_events()
        i += 1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()