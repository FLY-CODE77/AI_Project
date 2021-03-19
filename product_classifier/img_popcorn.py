import Augmentor 
from PIL import Image
import os, glob, numpy as np

categories = []
caltech_dir = "/mnt/nvme1n1/LPD_competition/train"

for filename in range(1000):
    img_dir = caltech_dir + "/" + str(filename)
    

    img = Augmentor.Pipeline(img_dir)

    img.flip_left_right(probability= 1.0)
    img.flip_random(probability=1.0)
    img.flip_top_bottom(probability=1.0)
    img.flip_left_right(probability= 0.3)
    img.flip_random(probability=0.2)
    img.flip_top_bottom(probability=0.5)
    img.random_distortion(probability=0.8,grid_width=10,grid_height=10, magnitude=8)
    img.crop_random(probability=1, percentage_area=0.5)
    img.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    img.sample(1000)

