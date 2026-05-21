#Viết chương trình đọc tệp dữ liệu import.txt bao gồm n dòng. Mỗi dòng là 1 số tự nhiên, Chương trình này sẽ đưa ra kết quả ở output.txt bao gồm n dòng. Mỗi dòng lần lượt là các ước số nguyên tố khác nhau
f = open("C:\\2321030163\\chương 3\\input.txt", "r")
s = f.readlines()
for i in s:
    num = int(i)
    print("Ước số nguyên tố của", num, "là: ")
    for j in range(2, num + 1):
        if num % j == 0:
            kt = True
            for k in range(2, int ( j ** 0.5) + 1):
                if j % k == 0:
                    kt = False
                    break
            if kt:
                print(j, " ")
    f.close()