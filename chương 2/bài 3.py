#Nhập vào dãy số khác 0. Tính tổng các số chẵn
n = input("nhập vào 1 dãy số: ")
a = list(map(int, n.split()))
s = 0
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        s += a[i]
    i += 1
print(s)