# -*- coding: utf-8 -*-
# @Time         : 2018/10/27 15:39
# @Author       : sodalife
# @File         : traditional_verify
# @Description  : 传统的验证码识别

# 需要用到 tesseract-ocr 识别验证码
import pytesseract
from PIL import Image
image = Image.open('C:\\Users\du\Desktop\download.png')
print(image)
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
print(pytesseract.image_to_string(image))