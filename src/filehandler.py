# step 1: verify files
# step 2: look for faces in file
# step 3: verify faces in file
# step 4: create function to return image buffers to opencv handler as a tuple
import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from matplotlib import pyplot as plt
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


class FileHandler:
    file_in_one = ""
    file_in_two = ""

    def __init__(self, file_in_one, file_in_two):
        print("created file handler object")

def facedetection(image):
    key = "07a542bc7f1c4cc888f4ea123956f568"
    ENDPOINT = "https://invisiblemanproj.cognitiveservices.azure.com/"
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(key))
    detected_faces = face_client.face.detect_with_stream(image, detection_model='detection_03')
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(image))
    first_image_face_ID = detected_faces[0].face_id
    print('Drawing rectangle around face... see popup for results.')
    img = Image.open(BytesIO(image))
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(getRectangle(face), outline='red')
    plt.subplot(121), plt.imshow(img)
    plt.show()


def getRectangle(faceDictionary):
    rect = faceDictionary.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    return ((left, top), (right, bottom))

