import numpy as np
import cv2
import sift
import os

class Image():
    def __init__(self,array,id):
        self.array = array
        self.id = id
        self.keypoints,self.descriptors = self.get_kp_d()
        self.rotation = np.zeros((3, 3), dtype=float)
        self.translation = np.zeros((3, 1), dtype=float)

    def get_kp_d(self):
        kp , d = sift.get_kp_d(self.array)
        return kp,d

def create_views(dir):
    views = []
    for id, image in enumerate(os.listdir(dir)):
        img = cv2.imread(f"{dir}/{image}")
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        view = Image(img, id)
        views.append(view)
    return views