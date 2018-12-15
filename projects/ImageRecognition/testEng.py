# -*- coding: utf-8 -*-
"""
Created on Thu Oct 04 11:53:23 2017

@author: Srikrishna.Sadula
"""

from PIL import Image
from pytesseract import image_to_string

#print('Hello Text Image Recognition')

print (image_to_string(Image.open('D:\\projects\\ImageRecognition\\test-english.jpg'), lang='eng'))