#for với range
x = [3, 4, 5, 6]
for x in range(3, 7):
    print("Value of x = ", x)

#for và mảng
fruits = ['apple', 'banana', 'cherry']
for x in fruits:
    if x == 'banana':
        continue
    print(x)

#Vòng lặp lồng nhau
adj = ['red', 'big', 'tasty']
fruits = ['apple', 'banana', 'cherry']
for x in adj:
    for y in fruits:
        print(x, y)