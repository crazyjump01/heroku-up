#-*- encoding: utf8 -*-
import cv2
from PIL import ImageFont, ImageDraw, Image
from tkinter import *
from tkinter import filedialog
import PIL.Image, PIL.ImageTk
import numpy as np
import datetime

import test2

def testimg():

    global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
    test2.window.filename = filedialog.askopenfilename(initialdir='', title='img', filetypes=(
    ('jpg files', '*.jpg'), ('png files', '*.png'), ('mp4 files', '*.mp4'), ('all files', '*.*')))
    print(test2.window.filename);

    xml = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
    ff = np.fromfile(test2.window.filename, np.uint8)
    img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = xml.detectMultiScale(gray, 1.05, 5)
    now = datetime.datetime.now().strftime("%d_%H-%M-%S")



    if len(faces):
        for (x,y,w,h) in faces:
            face_img = img[y:y+h, x:x+w] 
            face_img = cv2.resize(face_img, dsize=(0, 0), fx=0.04, fy=0.04)
            face_img = cv2.resize(face_img, (w, h), interpolation=cv2.INTER_AREA)
            img[y:y+h, x:x+w] = face_img 


    cv2.imshow('img',img)
    cv2.imwrite(str(now) + ".jpg",img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()

