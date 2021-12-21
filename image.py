import numpy as np
import cv2
import sift

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