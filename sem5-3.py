# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def CommonOrNot(value):
    if value == 2:
        return ('yes')
    for i in range(2,(value//2) + 1):
        if value % i == 1:
            print('yes')
            exit()
    print('no')

CommonOrNot(int(input('Введите число -> ')))


def ReverseString(value):
    n = int(input('Введите элемент -> '))
    if value > 1:
        ReverseString(value - 1)
    print(n, end = ' ')

ReverseString(int(input('Введите колличество элементов -> ')))