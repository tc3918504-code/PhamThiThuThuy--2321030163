#Cách khai báo
import mymath
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
print("Tổng hai số là: ", mymath.cong(x, y))
print("Hiệu sai số là: ", mymath.tru(x, y))
print("Tích hai số là: ", mymath.nhan(x, y))

#Lệnh from..import
from mymath import cong, tru
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
print("Tông hai số là: ", cong(x, y))
print("Hiệu hai số là: ", tru(x, y))

#Lệnh from...import*
from mymath import*
x = int(input("Nhập số thứ nhất: "))
y = int(input("Nhập số thứ hai: "))
print("Tổng hai số là: ", cong(x, y))
print("Hiệu hai số là: ", tru(x, y))
print("Tích hai số là: ", nhan(x, y))
print("Thương hai số là: ", chia(x, y))