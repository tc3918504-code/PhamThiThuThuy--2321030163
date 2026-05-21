#Nhập vào 1 số n. Hãy viết hàm tính giai thừa của n đó
n = int(input("Nhập n: "))
def giaithua(m):
    gt = 1
    for i in range(1, m+1):
        gt = gt + i
    return gt
print("%d != %d" %(n, giaithua(n)))