#Đọc vào 1 dãy số từ tệp dulieu.txt (vd1). Tính và in ra tổng của dãy số đó
f = open("C:\\dulieu.txt", "r")
s = f.read()
s = s.strip()
a = s.split(" ")
t = 0
print("Dãy số đọc được là: ", a)
for i in a:
    t = t + int(i)
print("Tổng của dãy số là: ", t)