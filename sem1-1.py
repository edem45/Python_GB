
'''
1. В некоторой школе решили набрать три новых математических класса и 
оборудовать кабинеты для них новыми партами. За каждой партой может сидеть два учащихся. 
Известно количество учащихся в каждом из трех классов. Выведите наименьшее число парт, 
которое нужно приобрести для них.

**Input:**

20

21

22

**Output:**

32
'''
firstCountStudy = int(input("Введите количество учеников в 1 классе:"))
secondCountStudy = int(input("Введите количество учеников в 2 классе:"))
thirdCountStudy = int(input("Введите количество учеников в 3 классе:"))

firstCountDesk = firstCountStudy//2 + firstCountStudy%2
secondCountDesk = secondCountStudy//2 + secondCountStudy%2
thirdCountDesk = thirdCountStudy//2 + thirdCountStudy%2
print(firstCountDesk + secondCountDesk + thirdCountDesk)