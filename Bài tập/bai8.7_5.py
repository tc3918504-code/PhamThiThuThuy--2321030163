#Viết chương trình nhập vào ba số nguyên dương x, y, z. Sau đó tìm xem tích (x * y * z) có mấy chữ số và chữ số lớn nhất bằng bao nhiêu
x = int(input("Nhập x: "))
y = int(input("Nhập y: "))
z = int(input("Nhập z: "))
tich = x * y * z
print("Tích là: ", tich)
chuoi_tich = str(tich)
print("Số chữ số của tích: ", len(chuoi_tich))
print("Chữ số lớn nhất là: ", max(chuoi_tich))