#Viết chương trình nhập vào một số nguyên dương n, kiểm tra xem tích các chữ số của n có phải là số chẵn và lớn hơn 20 hay không
n = int(input("Nhap so nguyen duong n: "))
tich = 1
for i in str(n):
    tich = tich * int(i)
if tich > 20:
    if tich % 2 == 0:
        print("Tích các chữ số là sô chẵn và lớn hơn 20")
    else:
        print("Tích lớn hơn 20 nhưng không phải số chẵn")
else:
    print("Tích không lớn hơn 20")