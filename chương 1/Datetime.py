#Trả về ngày giờ hiện tại
import datetime
ngay_gio = datetime.datetime.now()
print(ngay_gio)

#Trả về ngày hiện tại
import datetime
ngay = datetime.date.today()
print(ngay)

#Tạo ra đối tượng date
import datetime
x = datetime.datetime(2021, 6, 17)
print(x)

#Phương thức steftime()
import datetime
now = datetime.datetime.now()
print(now)
s = now.strftime("%d/%m/%y, %H:%M:%S")
print("s:", s)

#Phương thức strptime()
from datetime import datetime
dt_string = "11/07/2021"
ngay_thang = datetime.strptime(dt_string, "%d/%m/%Y")
print(ngay_thang)
s = ngay_thang.strftime("%d/%m/%Y")
print(s)