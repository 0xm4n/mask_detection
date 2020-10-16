# -*- coding:utf-8 -*-
import cv2, os
from PIL import Image
import numpy as np

from .pytorch_infer import inference


def start(img): 
    # img = cv2.imread(img_path)
    # img = cv2.cvtColor(response, cv2.COLOR_BGR2RGB)

    nfaces, nmasks, flag, image_ori, image = inference(img, show_result=True, target_shape=(360, 360))
    
    return nfaces, nmasks, flag, image_ori, image

# nfaces, nmasks, flag, image_out = start(img_path='./myapp/FaceMaskDetection/test/test1.jpeg')

# print(nfaces)
# print(flag)
# Image.fromarray(image_out).show()