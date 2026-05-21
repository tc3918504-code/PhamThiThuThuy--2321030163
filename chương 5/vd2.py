class Circle:
    def Dientich(self):
        return self.bk*self.bk*3.141592
    def Nhap(self):
        self.bk = float(input("Nhập bán kinh: "))
c = Circle()
c.Nhap()
print("Diện tích của hình tròn là: ", c.Dientich())