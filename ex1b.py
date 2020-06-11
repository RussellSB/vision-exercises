import cv2
import ex1a as ex1a
import matplotlib
from matplotlib import pyplot as plt

def initSubPlots(ims):
    plot_size = int(len(ims) / 2)
    fig, ax = plt.subplots(nrows=plot_size, ncols=plot_size)
    fig.subplots_adjust(hspace=0, wspace=0)
    return (fig, ax)

def calcHistograms(ims, ax):
    colour_dimensions = len(ims[0].shape)
    if(colour_dimensions > 2):
        return calcHistograms_RGB(ims, ax)
    else:
        return calcHistograms_BW(ims, ax)

def calcHistograms_BW(ims, ax):
    i = 0
    for row in ax:
        for col in row:
            hist = cv2.calcHist([ims[i]], [0], None, [256], [0, 256])
            col.set_title('Histogram of Segment ' + str(i + 1))
            col.set_xlabel('Pixel intensity')
            col.set_ylabel('Frequency')
            col.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
            col.plot(hist)
            i += 1
    plt.tight_layout()
    plt.show()
    return ax


def calcHistograms_RGB(ims, ax):
    i = 0
    color = ('b', 'g', 'r')
    for row in ax:
        for col in row:
            for n, c in enumerate(color):
                hist = cv2.calcHist([ims[i]],[n],None,[256],[0,256])
                col.plot(hist, color=c)
            col.set_title('Histogram of Segment ' + str(i + 1))
            col.set_xlabel('Pixel intensity')
            col.set_ylabel('Frequency')
            col.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
            i += 1
    return ax

def main():
    im = cv2.imread("images/tol.jpg", 0)  # loads image
    ims = ex1a.split_into_4(im)


    for i in range(0, 4):
        ex1a.binary_threshold(ims[i], 127)
        cv2.imshow('Tunnel of Love (' + str(i + 1) + ')', ims[i])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    (fig, ax) = initSubPlots(ims)
    ax = calcHistograms(ims, ax)
    fig.canvas.draw()
    fig.canvas.flush_events()

if __name__ == '__main__':
    main()
