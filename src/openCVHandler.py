import cv2

from filehandler import *
import numpy as np
from matplotlib import pyplot as plt


class OpenCVHandler:

    def __init__(self, file_in_one, file_in_two):
        print("OpenCV init: " + cv2.__version__)
        self.file_in_one = file_in_one
        self.file_in_two = file_in_two
        self.file_handler = FileHandler(file_in_one, file_in_one)

    # this will apply the gaussian blur
    def process(self):
        edges_one = do_canny(self.file_in_one)
        edges_two = do_canny(self.file_in_two)

        # now we calculate false positives
        compare_edges(cv2.imread(self.file_in_one), cv2.imread(self.file_in_two), edges_one, edges_two)


def compare_edges(img1, img2, edges_one, edges_two):
        plt.subplot(121), plt.imshow(img1, cmap='gray')
        plt.title('before'), plt.xticks([]), plt.yticks([])

        i = -1
        for row in edges_one:
            i += 1
            j = -1
            stored_pixel_left = -1
            stored_pixel_right = -1
            for pixel in row:
                j += 1
                if pixel == 255:
                    stored_pixel_left = j
                    break

            j = len(row)
            for pixel in reversed(row):
                j -= 1
                if pixel == 255:
                    stored_pixel_right = j
                    break
            if(stored_pixel_right < 0 or stored_pixel_right < 0): continue
            j = stored_pixel_left
            while j < stored_pixel_right:
                diff = (stored_pixel_right - stored_pixel_left)
                img1[i][j] = img2[i][j]
                j += 1

        plt.subplot(122), plt.imshow(img1, cmap='gray')
        plt.title('after'), plt.xticks([]), plt.yticks([])
        plt.show()







def do_canny(im):
    image = cv2.imread(im, 0)
    sigma = 0.33

    v = np.median(image)
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))

    edges = cv2.Canny(image, 100, 200, L2gradient = True)


   # edges = cv2.Canny(image, lower, upper)


    # plt.subplot(121), plt.imshow(image, cmap='gray')
    # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(edges, cmap='gray')
    # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    #plt.show()

    return edges
