#Nhập vào 1 chuỗi số cách nhau bởi dấu cách. Chuyển chuỗi số đó thành kiểu danh sách số nguyên. In ra ma trận 1 chiều của chuỗi đó
s = input("Nhap chuoi so: ")
lst = list(map(int, s.split()))
print("Ma tran 1 chieu:", lst)