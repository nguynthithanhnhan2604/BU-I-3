# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:50:46 2024

@author: DELL
"""
import math
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))
A= ((math.sqrt(a) - math.sqrt(b)) / (math.pow(a, 0.25) - math.pow(b, 0.25)))-((math.sqrt(a) + math.pow(a*b, 0.25)) / (math.pow(a, 0.25) + math.pow(b, 0.25)))
print("Kết quả là:",A)
