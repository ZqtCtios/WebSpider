# -*- coding: utf-8 -*-
# @Time    : 2019-09-04 11:59
# @Author  : ctios
# @Software: PyCharm
from PIL import Image
def convertImg(filename):
    img = Image.open(filename)
    img = img.convert('L')
    imgSize=img.size
    for i in range(imgSize[0]):
        for j in range(imgSize[1]):
            x = img.getpixel((i,j))
            if 247<x<252:
                img.putpixel((i,j),255)
    img.save(filename)

if __name__ == '__main__':
    convertImg('2.png')