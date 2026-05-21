#Nhập vào 1 số, kiểm tra xem số đó có phải số hoàn hảo hay không?
n = int(input("Nhập n ="))
s = 0
for i in range(1, n):
    if n % i == 0:
        s = s + i
if s == n:
    print(n, "là số hoàn hảo")
else:
    print(n, "không là số hoàn hảo")