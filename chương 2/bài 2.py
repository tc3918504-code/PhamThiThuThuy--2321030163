#Nhập vào 1 dãy số tính tổng các chữ số chẵn có mặt trong dãy đó
n = input("Nhập vào 1 dãy số: ")
s = 0
i = 0
while i < len(n):
    if n[i].isdigit() and int(n[i]) % 2 == 0:
        s += int(n[i])
    i += 1
print(s)