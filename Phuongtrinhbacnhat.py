# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 13:40:17 2024

@author: NguyenThiThuHang
"""

a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
if a == 0 and b != 0:
    print("Phương trình vô nghiệm")
elif a == 0 and b == 0:
    print("Phương trình có vô số nghiệm")
else:
    print("Nghiệm của phương trình là: ", -b/a)