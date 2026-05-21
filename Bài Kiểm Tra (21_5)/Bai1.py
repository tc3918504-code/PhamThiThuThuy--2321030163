#Viết chương trình nhập vào một dãy số thực x1, x2,... xn(0 < n < 100), sau đó tìm trung bình cộng các phần tử dương trong dãy mà giá trị nằm trong khoảng (0, 1000)
n = int(input("Nhập số phần tử n: "))
tong = 0
dem = 0
for i in range(n):
    x = float(input(f"Phần tử thứ {i+1}: "))
    if 0 < x < 1000:
        tong += x
        dem += 1
if dem > 0:
    tbc = tong/dem
    print("Trung bình cộng: ", tbc)
else:
    print("Không có phần tử phù hợp")