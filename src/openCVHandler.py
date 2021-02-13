import cv2

from filehandler import *


class OpenCVHandler:

    def __init__(self, file_in_one, file_in_two):
        print("OpenCV init: " + cv2.__version__)
        self.file_in_one = file_in_one
        self.file_in_two = file_in_two
        self.file_handler = FileHandler(file_in_one, file_in_one)



