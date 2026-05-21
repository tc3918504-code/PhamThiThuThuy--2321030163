#Viết chương trình nhập vào 2 số nguyên duong m và n, sau đó kiểm tra xem m có chia hết cho tổng các chữ số của n hay không
m = int(input("Nhap m = "))
n = int(input("Nhap n = "))
tong = 0
while n > 0:
    tong += n % 10
    n = n // 10
if m % tong == 0:
    print("m chia hết cho tổng các chữ số của n")
else:
    print("m không chia hết cho tổng các chữ số của n")