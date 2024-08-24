# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 16:12:38 2024

@author: DELL
"""

print(" =========== MENU ============ ")
print("\t1. Hủ tiếu")
print("\t2. Cháo lòng")
print("\t3. Bánh canh")
print("\t4. Bún riêu")
print("\t5. Phở bò")
print(" ============================== ")

menu = ["1","2","3","4","5","hủ tiếu","cháo lòng","bánh canh", "bún riêu","phở bò"]

luachon = input(" Mời nhập lựa chọn: ").lower()
if luachon in menu: 
   print(" ============================== ")
else:
    print("Món bạn chọn không có trong menu. Vui lòng nhập lại !")


