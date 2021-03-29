import cv2
import numpy as np
import pytesseract
import os

# pytesseract.pytesseract.tesseract_cmd = "/home/nelson/Documents/leitorDeFaturas/leitorDeFaturas"
path = r"/home/nelson/Documents/leitorDeFaturas/leitorDeFaturas/img/Celesc/jpg/fatura.jpg"
roi = [[(193*3, 104*3),(378*3, 184*3)]]
# roi = [[(193, 104),(378, 184)]]

sourceImg = cv2.imread(path)
h,w,c = sourceImg.shape
sourceImg = cv2.resize(sourceImg, (w//1,h//1))


image = cv2.rectangle(sourceImg, roi[0][0], roi[0][1], (255,0,0), 2)
imgCrop = sourceImg[193*3:104*3, 378*3: 184*3]

cv2.imshow('teste', imgCrop)
cv2.waitKey(0)