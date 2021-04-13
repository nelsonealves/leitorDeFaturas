import cv2
import numpy as np
import pytesseract
import os
import re

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"
path = r"/home/nelson/Documents/leitorDeFaturas/img/Celesc/jpg/fatura.jpg"

mult = 3
# x1, y1, x2, y2
# x1 = 192 * mult
# y1 = 104 * mult
# x2 = 378 * mult
# y2 = 250 * mult

x1 = 16 * mult
y1 = 160 * mult
x2 = 193 * mult 
y2 = 230 * mult
roi = [[(x1, y1), (x2, y2)]]
# roi = [[(193, 104),(378, 184)]]

sourceImg = cv2.imread(path)
h, w, c = sourceImg.shape
#sourceImg = cv2.resize(sourceImg, (w//3, h//3))


imgMask = np.zeros_like(sourceImg)

# image =
imgShow = cv2.addWeighted(sourceImg, 0.99, imgMask, 0.1, 0)

imgCrop = sourceImg[y1: y2, x1: x2]


# cv2.imshow('teste', imgCrop)

# Dados do Faturamento [x1, y1, x2, y2, color]
# pos1 = [
#     [1, 0, 292, 437, 'red'], [290, 0, 370, 437, 'red'], [
#         368, 0, 455, 437, 'red'], [482, 0, 554, 437, 'red'],
# ]
pos1 = [
    [1, 0, 44, 208, 'red'], [290, 0, 370, 437, 'red'], [
        368, 0, 455, 437, 'red'], [482, 0, 554, 437, 'red'],
]
col1 = imgCrop[pos1[0][1]:pos1[0][3], pos1[0][0]:pos1[0][2]]
col2 = imgCrop[pos1[1][1]:pos1[1][3], pos1[1][0]:pos1[1][2]]
col3 = imgCrop[pos1[2][1]:pos1[2][3], pos1[2][0]:pos1[2][2]]
col4 = imgCrop[pos1[3][1]:pos1[3][3], pos1[3][0]:pos1[3][2]]


def trataImagem(img):
    img = cv2.resize(img, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    img = cv2.threshold(cv2.bilateralFilter(img, 5, 75, 75),
                        0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return img


col1Tratado = trataImagem(col1)
col2Tratado = trataImagem(col2)
col3Tratado = trataImagem(col3)
col4Tratado = trataImagem(col4)


# cv2.imshow('SEM RESIZE', col4)



def separate(array, separator):
    results = []
    a = array[:]
    i = 0
    while i <= len(a)-len(separator):
        if (a[i:i+len(separator)] == separator):

            if a[:i] != '':
               # print(f'Palavra: {a[:i]}')
                # print('true')
                results.append(a[:i])
            a = a[i+len(separator):]
            i = 0
        else:
            i += 1
    results.append(a)
    return results

col1Array = pytesseract.image_to_string(col1Tratado)
col2Array = pytesseract.image_to_string(col2Tratado)
col3Array = pytesseract.image_to_string(col3Tratado)
col4Array = pytesseract.image_to_string(col4Tratado)


cv2.imshow('com resize', col1Tratado)
# cv2.imshow('com resize1', col2Array)
# cv2.imshow('com resize2', col3Array)
# cv2.imshow('com resize3', col4Array)

cv2.waitKey(0)

print(col1Array)
print(col2Array)
print(col3Array)
print(col4Array)


# col1Array = separate(pytesseract.image_to_string(col1Tratado), '\n')
# col2Array = separate(pytesseract.image_to_string(col2Tratado), '\n')
# col3Array = separate(pytesseract.image_to_string(col3Tratado), '\n')
# col4Array = separate(pytesseract.image_to_string(col4Tratado), '\n')



# i = 6
# print (f'{col1Array}')
# print (f'{col2Array}')
# print (f'{col3Array}')
# print (f'{col4Array}')


# print (len(col1Array))
# print (len(col2Array))
# print (len(col3Array))
# print (len(col4Array))
print(col1Array)
arrayFinal = []

for x in range(1, len(col1Array)):
    # arrayFinal
    if (col1Array[x][0:4] == 'Subt'):
        break
    else:
        arrayFinal.append(col1Array[x])

# print(arrayFinal)

# for x in range():
#     arrayFinal.append([col1Array[i], col2Array[i], col3Array[i], col4Array[i]])

# print (arrayFinal)
# print(f'{image}')
# print('valores')
# print(f'{pytesseract.image_to_string(col4)}')


# cv2.imshow('Dados faturamento', col1)
