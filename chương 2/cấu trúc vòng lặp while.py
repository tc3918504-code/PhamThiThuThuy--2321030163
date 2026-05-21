#vd1: Tính tổng: 1 + 2 + 3 + 4 + 5 + 6
i = 1
s = 0
while i <= 6:
    s += i
    i += 1
print(s)

#vd2: Sử dụng while để tính tổng các số từ 1 đến n (với n là 1 số nguyên dương được nhập vào từ bàn phím)
n = int(input("Nhập n: "))
tổng = 0
i = 1
while i <= n:
    tổng = tổng + 1
    i = i + 1
print("Tổng là:", tổng)

#Lệnh break
var = 10
while var > 0:
    print("Giá trị biến hiện tại là: ", var)
    var = var -1
    if var == 5:
        break
    print("Giá biến hiện tại là: ")

#Lệnh continue
var = 5
while var > 0:
    var = var - 1
    if var == 3:
        continue
    print("Giá trị hiện tại là: ", var)

#Lệnh pass
i = 1
while i <= 10:
    if (i % 2 == 0):
        pass
    else:
        print(i)
    i = i + 1