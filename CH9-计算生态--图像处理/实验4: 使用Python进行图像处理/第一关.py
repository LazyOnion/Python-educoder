import numpy as np
import cv2 as cv

'''****************BEGIN****************'''
# 读取图片
image_path = 'step1/image/face.jpg'
img = cv.imread(image_path)
# 转换为灰度图片
gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# 人脸检测器
modle_path = 'sample/data/haarcascades/haarcascade_frontalface_default.xml'
face_cascade = cv.CascadeClassifier(modle_path)
# 识别人脸
faces = face_cascade.detectMultiScale(gray_img, 1.3, 5)
'''**************** END ****************'''

print(faces)
