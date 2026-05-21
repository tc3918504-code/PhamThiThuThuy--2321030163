#Viết chương trình nhập vào 1 ma trận n cột và m hàng. In ra ma trận vừa nhập
m = int(input("Nhập m = "))
n = int(input("Nhập n = "))
a = []
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = float(input("Nhập phần tử thứ a [%d] [%d]: " %(i+1, j+1)))
        a[i].append(x)
print("Mảng vừa nhập là: ")
for i in range(0, m):
    for j in range(0, n):
        print("%8.2f" %a[i][j], end ="" )
    print()