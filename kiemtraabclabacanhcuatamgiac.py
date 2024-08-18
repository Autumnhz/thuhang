# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:22:12 2024

@author: NguyenThiThuHang
"""
print("Nhập 3 kích thước xem có phải tam giác không?")
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
if a + b > c and a + c > b and b + c > a:
    print("a, b, c là ba cạnh của một tam giác.")
else:
    print("a, b, c không là ba cạnh của một tam giác")          
