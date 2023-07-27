# list_1 = [1, 2, 15, 3, 4]
# k = 8
# for i in list_1:
#     if (k == i):
#         print(i)
#     elif (i<k):
#         near_k = i
#         if (i>near_k):
#             near_k = i
#     elif (i>k):
#         near_k1 = i
#         if (i < near_k1 and i>k):
#             near_k1 = i
# if (near_k1-k >= k - near_k):
#     print(near_k)
# else: print(near_k1)

list_1 = [1, 2, 3, 4, 33, 11, 12]
k = 5
 
def nearest_value(items, value):
    abs_list = list(map(lambda item: abs(item - value), items)) # создаем список значений разницы item - value по модулю 
    return items[abs_list.index(min(abs_list))]                 # находим индекс минимальной разницы и по этому индексу возвращаем элемент из items
 
print(nearest_value(list_1, k))