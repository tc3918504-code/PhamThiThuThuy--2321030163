#vd1: Nhập vào 1 số nguyên. Kiểm tra số nguyên đó là chẵn hay lẻ?
n = int(input("Nhập vào 1 số nguyên: "))
if (n % 2 == 0):
    print("Số" + repr(n) + "là số chẵn")
else:
    print("Số" + repr(n) + "là số lẻ")

#vd2: Giải hệ phương trình: ax + b = 0; a,b nhập từ bàn phím (nguyên)
a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))
if a == 0:
    if (b == 0):
        print("Phương trình vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("x = ", x)

#vd3: Nhập vào 2 số x,y. Kiểm tra xem x = y, x > y, x < y hay không?
x = float(input("Nhập x = "))
y = float(input("Nhập y = "))
if x == y:
    print("x = y")
if x > y:
    print("x > y")
if x < y:
    print("x < y")