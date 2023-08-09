while True:
    n = int(input('Кол-во оценок -> '))
    if n < 1:
        print('Вам не нужно менять оценки')
    else:
        break

arr = []

while n > 0:
    b = int(input('Введите оценку -> '))
    arr.append(b)
    n -= 1

print(arr)

max_val = max(arr)
min_val = min(arr)

for i in range(0, len(arr)):
    if arr[i] == max_val:
        arr[i] = min_val

print(arr)


# my_list = [1, 2, 3, 4, 5, 5, 5, 5]

# def min_max(my_list):
#     min = max = my_list[0]
#     for i in my_list:
#         if i>max:
#             max=i
#         if i<min:
#             min = i
#     return (min, max)

# # min, max = min_max(my_list)

# def change_min_max(my_list, temp):
#     for i in range(len(my_list)):
#         if my_list[i]==temp[1]:
#             my_list[i]=temp[0]
#     return my_list

# print (change_min_max(my_list, min_max(my_list)))