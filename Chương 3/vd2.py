#Chương trình cho phép nhập vào 1 ma trận gồm m hàng, n cột (các số thực). Ghi ma trận vừa nhập ra tệp "matran.txt"
m = int(input("Nhập số hàng = "))
n = int(input("Nhập số cột = "))
a = []
for i in range(0, m):
    a.append([])
    for j in range(0, n):
        x = float(input("Nhập phần tử thứ a[%2d][%2d]: " % (i + 1, j + 1)))
        a[i].append(x)
obj = open("C:\\matran.txt", "w")
obj.write("Mang vua nhap la:\n")
for i in range(0, m):
    for j in range(0, n):
        obj.write(str(a[i][j]) + " ")
    obj.write("\n")
obj.close()