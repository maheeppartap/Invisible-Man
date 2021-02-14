
import tkinter as tk

from openCVHandler import OpenCVHandler
from src import *

import sys


if __name__ == '__main__':
    # window = tk.Tk()
    # window.mainloop()
    opencv = OpenCVHandler(sys.argv[1], sys.argv[2])
    opencv.process()






