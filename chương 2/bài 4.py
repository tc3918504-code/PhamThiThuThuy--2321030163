#Viết chương trình nhập 1 số tự nhiên n và tính các giá trị ước số nguyên tố (tính số các ước nguyên tố khác n)
n = int(input("Nhập n = "))
đếm = 0
i = 2
while n > 1:
    if n % i != 0:
        i = i + 1
    else:
        đếm = đếm + 1
        while n %i == 0:
            n = n//i
    print ()
    print("Số nguyên tố là: ", đếm)