import Augmentor 
from PIL import Image
import os, glob, numpy as np

categories = []
caltech_dir = "/mnt/nvme1n1/LPD_competition/train"

for filename in range(1000):
    img_dir = caltech_dir + "/" + str(filename)
    

    img = Augmentor.Pipeline(img_dir)

    img.flip_left_right(probability= 0.333)
    img.flip_random(probability=0.777)
    img.zoom(probability=0.3, min_factor=1.1, max_factor=1.6)
    img.random_distortion(probability=0.4,grid_width=10,grid_height=10, magnitude=8)
    img.crop_random(probability=0.4444, percentage_area=0.5)
    img.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    img.rotate270(probability=0.3333)
    img.sample(3000, multi_threaded=True)

