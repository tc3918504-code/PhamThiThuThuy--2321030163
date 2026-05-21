#Biến cục bộ
def msg():
    a = 10
    print("Giá trị của a là: ", a)
msg()

#Biến toàn cục
b = 20
def msg():
    a = 10
    print("Giá trị của a là: ", a)
    print("Gia trị của b là: ", b)
    return
msg()
print(b)