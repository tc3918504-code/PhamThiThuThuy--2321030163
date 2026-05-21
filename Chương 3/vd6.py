#Đọc tệp abcd.txt
f = open("abcd.txt", "r")
l1 = f.readline()
print(l1)
l2 = f.readline()
print(l2)

r = open("abcd.txt", "r")
l = f.readline()
while l:
    print(l)
    i = i.readline()

f = open("abcd.txt", "r")
l1 = f.readlines()
print(l1)