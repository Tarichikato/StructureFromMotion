import cv2

sift = cv2.SIFT_create()

def get_kp_d(img):
    kp,d = sift.detectAndCompute(img,None)
    return kp,d