import os
from image import Image
import cv2

images_dir = "./images"
views = []

for id,image in enumerate(os.listdir(images_dir)):
    img = cv2.imread(f"{images_dir}/{image}")
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    view = Image(img,id)
