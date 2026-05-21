#Viết chương trình nhập vào một dãy số nguyên x1, x2, ..., xn (0 < n < 100). Tính tổng các phần tử là số nguyên tố tỏng dqayx và kiểm tra xem tổng này có phải là số lẻ và lớn hơn 50 hay không?
a = list(map(int, input("Nhap day so: ").split()))
tong = 0
for x in a:
    if x > 1:
        la_ngto = True
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                la_ngto = False
                break
        if la_ngto:
            tong += x
if tong % 2 == 1 and tong > 50:
    print("Tong =", tong)
    print("La so le va lon hon 50")
else:
    print("Tong =", tong)
    print("Khong thoa dieu kien")