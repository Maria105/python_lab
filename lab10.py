#!/usr/bin/env python3
# -*- codding: utf-8 -*-

from PIL import Image
from re import all

def decrypt_text():
    """This function decrypt text from the image"""
    a=[]
    keys = []
    img = Image.open(input("path to image: "))
    pix = img.load()
    f = open(input("path to keys: "), 'r')
    fw = open("new_image.png", 'r+b')
    img_code = str(fw.read())
    fl = open('code_img.txt', 'w')
    flw = fl.write(img_code)
    fl.flush()
    fl.close()
    a = str([line.strip() for line in f])

    for i in range(len(all(r'\((\d+)\,',a))):
        keys.append((int(all(r'\((\d+)\,', a)[i]), int(all(r'\,\s(\d+)\)', a)[i])))
    for key in keys:
        k.append(pix[tuple(key)][0])
    return ''.join([chr(elem) for elem in k])

print("Massage: ", decrypt_text())
