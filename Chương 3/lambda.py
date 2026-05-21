#Vd1
nhan_doi = lambda a: a*2
print(nhan_doi(10))

#Hàm lambda với filter()
list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
list_moi = list(filter(lambda a: a%2 == 0, list_goc))
print(list_moi)

#Hàm lambda với map()
list_goc = [10, 9, 8, 7, 6, 1, 2, 3, 4, 5]
list_moi = list(map(lambda a: a*2, list_goc))
print(list_moi)