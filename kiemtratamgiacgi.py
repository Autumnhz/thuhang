# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:42:48 2024

@author: NguyenThiThuHang
"""
a = float(input("Nhập a:"))
b = float(input("Nhập b:"))
c = float(input("Nhập c:"))
if a + b > c and a + c > b and b + c > a:
   print("a, b, c là một tam giác.") 
   if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
      print("Đây là tam giác vuông.")
   elif a==b and b==c:
      print("Đây là tam giác đều.")
   elif a==b or a==c or a==c:
      print("Đây là tam giác cân.")
else:
    print("a, b, c không là ba cạnh của một tam giác")
    