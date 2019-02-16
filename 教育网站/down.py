#!/usr/bin/python3
import os
path = "/home/download" #文件夹目录  
files= os.listdir(path)
for file in files:
    if file.find('mp4')>0:
        print('http://[2604:a880:800:10::1a:b001]/download/'+file)