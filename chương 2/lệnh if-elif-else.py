#vd1: Nhập vào 2 số x, y. Kiểm tra xem x = y, x > y, x < y hay không
x = float(input("Nhập x: "))
y = float(input("Nhập y: "))
if (x == y):
    print('x = y')
elif (x > y):
    print('x > y')
else:
    print('x < y')

#vd2: Cho mã: 1, 2, 3, 4, 5 ứng với dân tộc: Kinh, Tày, Nùng, Thái, Khơ-me. Hẫy lập chương trình nhập vào mã dân tộc và hiển thị dân tộc tương ứng
ma = int(input("Nhập mã dân tộc: "))
if ma == 1:
    print("Dân tộc: Kinh")
elif ma == 2:
    print("Dân tộc: Tày")
elif ma == 3:
    print("Dân tộc: Nùng")
elif ma == 4:
    print("Dân tộc: Thái")
elif ma == 5:
    print("Dân tộc: Khơ-me")
else:
    print("Mã dân tộc không hợp lệ")

#vd3: Giải phương trình bậc nhất: ax + b = 0 (a,b: nhập từ bàn phím (nguyên))
a = float(input("Nhập hệ số a = "))
b = float(input("Nhập hệ số b = "))
if (a == 0) and (b == 0):
    print("Phương trình vô số nghiệm")
elif (a == 0) and (b != 0):
    print("Phương trình vô nghiệm")
else:
    x = -b/a
    print("x = ", x)