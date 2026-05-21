#Toán tử +
a = 'Hello'
b = 'python'
s = a + 'python'
print(s)
s2 = ', goobye'
s3 = s + s2
print(s3)

#Toán tử in
print('a' in 'abc')
print('ab' in 'abc')
print('ac' in 'abc')
print('ac' not in 'abc')

#Hàm len()
a = "Hello World!"
print(len(a))

#Phương thức lower()
a = "Hello World!"
print(a.lower())

#Phương thức upper()
a = "Hello World!"
print(a.upper())

#Phương thức find()
strl = "Ví dụ hàm find() trong python"; str2 = "find"
print(strl.find(str2))
print(strl.find(str2, 10))
print(strl.find(str2, 20))

#Phương thức count()
strl = "Ví dụ hàm count trong python, học lập trình python"
sub = "py"
print("strl.count(sub, 10):", strl.count(sub, 10))
print("strl.count(sub, 10, 30):", strl.count(sub, 10, 30))
sub = "hàm"
print("strl.count(sub):", strl.count(sub))

#Phương thức replace()
str = 'Hello World'
newstr = str.replace('Hello', 'Bye')
print(newstr)

str = "AA BB AA CC AA DD AA EE"
newstr = str.replace("AA", "aa", 2)
print(newstr)

#Phương thức split()
print("Hello World")
print(str.split(" "))
print("A B C D E".split(" "))
print("A B C D E".split(" ",1))
print("A B C D E".split(" ", 3))

#Phương thức lstrip()
strl = "     Ví dụ hàm lstrip() trong python     "
print(strl.lstrip())

strl = "-----Ví dụ hàm lstrip() trong python-----"
print(strl.lstrip('-'))

#Phương thức isalpha()
strl = "hello python"
print(strl.isalpha())

strl = "hello"
print(strl.isalpha())

strl = "hello123"
print(strl.isalpha())

#Phương thức isdigit()
strl = "hello python"
print(strl.isdigit())

strl = "hello123"
print(strl.isdigit())

strl = "123"
print(strl.isdigit())