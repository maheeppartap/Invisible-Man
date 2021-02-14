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


        image = cv2.imread(self.file_in_one, 0)
        sigma = 0.33

        v = np.median(image)
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edges = cv2.Canny(image, lower, upper)




        #edges = cv2.Canny(img, 100, 200)

        plt.subplot(121), plt.imshow(image, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

        '''
               image = cv2.imread(self.file_in_one)
        original = image.copy()
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (3, 3), 0)
        canny = cv2.Canny(blurred, 120, 255, 1)
        kernel = np.ones((5, 5), np.uint8)
        dilate = cv2.dilate(canny, kernel, iterations=2)

        # Find contours
        cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]

        # Iterate thorugh contours and filter for ROI
        image_number = 0
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            cv2.rectangle(image, (x, y), (x + w, y + h), (36, 255, 12), 2)
            ROI = original[y:y + h, x:x + w]
           # cv2.imwrite("ROI_{}.png".format(image_number), ROI)
            image_number += 1

        imS = cv2.resize(canny, (960, 960))
        cv2.imshow('canny', imS)
        # cv2.imshow('image', image)
        cv2.waitKey(0)
        '''

