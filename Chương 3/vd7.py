#Đọc vào 1 ma trận từ tệp matran.txt (vd2). Tính và in ra tổng của ma trận đó
f = open("C:\\matran.txt", "r")
f.readline()
ma = []
ma = [dong.split() for dong in f]
print(ma)
s = 0
for subma in ma:
    for j in subma:
        s = s + float(j)
print("Tổng của ma trận là:", s)
f.close()