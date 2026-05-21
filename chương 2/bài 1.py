#Nhập vào 3 điểm Toán, Lí, Hóa và tính điểm trung bình. Kiểm tra xem điểm trung bình bé hơn 5: yếu, bé hơn 7: trung bình, bé hơn 9: khá, còn lại giỏi
toán = float(input("Nhập điểm toán: "))
lí = float(input("Nhập điểm lí: "))
hóa = float(input("Nhập điểm hóa: "))
đtb= (toán + lí + hóa)/3
print("Điểm trung bình: ", đtb)
if đtb < 5:
    print("Xếp loại: yếu")
elif đtb < 7:
    print("Xếp loại: trung bình")
elif đtb < 9:
    print("Xếp loại: khá")
elif đtb <= 10:
    print("Xếp loại giỏi")
else:
    pass