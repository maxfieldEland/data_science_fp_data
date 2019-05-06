# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 13:15:26 2019

@author: mgreen13
"""

from imutils import paths
import argparse
import cv2
import json
import os
import matplotlib.pyplot as plt
from PIL import Image, ImageFont, ImageDraw



file = "hold_labels.json"
holds = []

with open(file, 'r') as f:
    for line in f:
        if len(line) > 1:
            holds.append(json.loads(line))
holds = holds[0]

imagePaths = []
for i in range(1,41):
    imagePath = "web_scrape/hold_pngs/{}.png".format(i)
    imagePaths.append(imagePath)

for i in range(50,150):
    imagePath = "web_scrape/hold_pngs/{}.png".format(i)
    imagePaths.append(imagePath)



# assign the location coordinate of every hold to the photo of every hold
for idx in range(0,40):
    imagePath = imagePaths[idx]
    imgNum = idx+1
    # skip over 40-50 for the image path retrieval 
    img = Image.open(imagePath)
    font_type = ImageFont.load_default()
    draw = ImageDraw.Draw(img)
    hold_label = holds['{}'.format(imgNum)]
    draw.text(xy = (0,0),text = "{}".format(hold_label), fill = (64,52,140), font = font_type)
    img.save("web_scrape/labelled_imgs/{}.png".format(imgNum),quality = 95)


for idx in range(40,140):
    imagePath = imagePaths[idx]
    imgNum = idx+10
    # skip over 40-50 for the image path retrieval 
    img = Image.open(imagePath)
    font_type = ImageFont.load_default()
    draw = ImageDraw.Draw(img)
    hold_label = holds['{}'.format(imgNum)]
    draw.text(xy = (0,0),text = "{}".format(hold_label), fill = (64,52,140), font = font_type)
    img.save("web_scrape/labelled_imgs/{}.png".format(imgNum),quality = 95)

imagesPaths = sorted(os.listdir("web_scrape/labelled_imgs"))

paths = []
for path in imagesPaths:
    paths.append(path)