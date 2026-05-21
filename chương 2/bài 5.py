#Viết chương trình nhập 2 dãy số nguyên gồm n phần tử. Tính và in tổng các số trong dãy đó
a = []
n = int(input("Nhập số phần tử của dãy số: "))
for i in range(1, n+1):
    k = int(input("Nhập phần tử thứ " + str(i) + ":"))
    a.append(k)
s = 0
for i in a:
    s = s+i
print("Tổng của dãy số là:" + str(s))