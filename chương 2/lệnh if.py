#nhập vào 3 số a, b, c. In ra số lớn nhất/bé nhất
a = float(input("Nhập số thứ nhất = "))
b = float(input("Nhập số thứ hai = "))
c = float(input("Nhập số thứ ba = "))
max = a
if (b > max):
    max = b
if (c > max):
    max = c
    print("Số lớn nhất trong 3 số %f, %f và %f là %f" %(a, b, c, max))