#Viết chương trình nhập vào một số nguyên dương n, kiểm tra xem tổng các chữ số của n có phải là số chia hết cho 3 hay không
n = int(input("Nhap so nguyen duong n: "))
a = []
while n > 0:
    a.append(n % 10)
    n = n // 10
tong = sum(a)
if tong % 3 == 0:
    print("Tổng các chữ số chia hết cho 3")
else:
    print("Tổng các chữ số không chia hết cho 3")