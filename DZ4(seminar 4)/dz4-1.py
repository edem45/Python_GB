# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


n = int(input("Введите кол-во элементов 1-го списка: "))
m = int(input("Введите кол-во элементов 2-го списка: "))
spisok1 = []
spisok2 = []
for i in range(n):
    spisok1.append(input())
for i in range(m):
    spisok2.append(input())
spisok3 = spisok1 + spisok2
set1 = sorted(set(spisok3))
print(set1)

# from random import randint
# n_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов первого множества: '))))
# print(n_set)
# m_set = set(randint(1, 20) for i in range(int(input('Введите кол-во элементов второго множества: '))))
# print(m_set)
# s_set = sorted(n_set.intersection(m_set))
# print(s_set)