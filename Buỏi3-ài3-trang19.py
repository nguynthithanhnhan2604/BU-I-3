# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:49:13 2024

@author: DELL
"""

N=int(input("Nhập số nguyên N có 2 chữ số:"))
if 10<=N<=99:
    hang_chuc=N//10
    print("hàng chục là:",hang_chuc)
    hang_don_vi= N%10
    print("hàng đơn vị là:",hang_don_vi)
    N= hang_chuc+ hang_don_vi
    print(" Tổng các chữ số của N là:",N)
else:
    print(" Nhập số có 2 chữ số:")
    

