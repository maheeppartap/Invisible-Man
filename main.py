
from filehandler import facedetection
import tkinterHandler
from openCVHandler import OpenCVHandler
from src import *

import sys


if __name__ == '__main__':
    # window = tk.Tk()
    # window.mainloop()
    opencv = OpenCVHandler(sys.argv[1], sys.argv[2])
    opencv.process()
    opencv = OpenCVHandler()
    tkinterHandler.begin()
    image1 = open('test_pictures/handsome_guy.jpg', 'r+b')
    facedetection(image1)




