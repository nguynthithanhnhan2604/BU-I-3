# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 15:15:34 2024

@author: DELL
"""

giờ=int(input("Nhập số giờ:"))
phút=int(input("Nhập số phút:"))
giây=int(input(" Nhập số giây:"))
if giờ>=0 and giờ<24 and phút>=1 and phút<60 and giây>=1 and giây<=60:
    print(" Hiện tại là:",giờ,phút,giây)
    Tổng_giây=giờ*3600+phút*60+giây
    print("Tổng số giây là:",Tổng_giây)
else:
    print("Nhập lại giờ, phút, giây")
   


