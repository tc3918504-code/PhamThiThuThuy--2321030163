#Hàm len()
list1 = (123, 'abc', 'xyz')
list2 = ['java', 'python', 'php', 'c++']
print("Độ dài của list đầu tiên là: ", len(list1))
print("Độ dài của list thứ hai là: ", len(list2))

#Hàm max()
list1 = ['123', 'abc', 'xyz', 'def']
list2 = [333, 333, 111]
print("Phần tử có giá trị lớn nhất là: ", max(list1))
print("Phần tử có giá trị lớn nhất là: ", max(list2))

#Hàm min()
list1 = ['123', 'abc', 'xyz', 'def']
list2 = [333, 333, 111]
print("Phần tử có giá trị bé nhất là: ", min(list1))
print("Phần tử có giá trị bé nhất là: ", min(list2))

#Hàm list()
aTuple = ('123', 'abc', 'xyz', 'def')
aList = list(aTuple)
print("Các phần tử của Tuple là: ", aTuple)
print("Các phần tử của List là: ", aList)

#phương thức append()
list1 = ['java', 'python', 'c++']
print("Phần tử của list trước khi thêm: ", list1)
list1.append('php')
print("Phần tử của list sau khi thêm: ", list1)

#Phương thức count()
list1 = ['java', 'python', 'c++', 'python']
print("Số lần python xuất hiện trong list là: ", list1.count('python'))
print("Số lần 'java' xuất hiện trong list là: ", list1.count('java'))

#Phương thức extend()
list1 = ['java', 'python', 'c++']
list2 = ['c++', 'sql']
list1.extend(list2)
print("List sau khi được mở rộng thêm là: ", list1)

#Phương thức index()
list1 = ['java', 'python', 'c++', 'php', 'sql']
print("Chỉ mục của 'python' là: ", list1.index('python'))
print("Chỉ mục của 'php' là: ", list1.index('php'))

#Phương thức insert()
list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.insert(3, 'android')
print("List sau khi được chèn: ", list1)

#Phương thức pop()
list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.pop()
print("list: ", list1)
list1.pop(2)
print("list: ", list1)

#Phương thức remove()
list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.remove('c++')
print("list: ", list1)
list1.remove('java')
print("list: ", list1)

#Xóa phần tử ra khỏi list bằng lệnh del
fruits = ["apple", "banana", "quava"]
del fruits[0]
print(fruits)

#Phương thức reverse()
list1 = ['java', 'python', 'c++', 'php', 'sql']
list1.reverse()
print("list bị đảo ngược: ", list1)

#Phương thức clear()
fruits = ["apple", "banana", "quava"]
fruits.clear()
print(fruits)