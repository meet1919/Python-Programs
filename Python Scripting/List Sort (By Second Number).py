list = [(2, 1), (5, 8), (7, 13), (4, 2), (6, 5), (8, 4)]
list1 = []
for i in list:
    x = i[0] + i[1]
    list1.append(x)

list.sort(key= lambda x: x[1])
print(list)
