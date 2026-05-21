#Viết chương trình nhập vào 2 số nguyên dương m và n, sau đó tính tổng (a+b) và tìm ra chữ số lớn nhất trong tổng đó
m = int(input("Nhap m: "))
n = int(input("Nhap n: "))
tong = m + n
print("Tong =", tong)
ds = []
for i in str(tong):
    ds.append(int(i))
print("Chu so lon nhat trong tong la:", max(ds))