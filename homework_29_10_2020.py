import operator
list_to_sort = [[3,2,3], [2,0,2], [3,0,1], [3,1,0]]
print(list_to_sort)

list_to_sort.sort(key = operator.itemgetter(1, 2))
print(list_to_sort)