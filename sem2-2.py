


# натуральное число A > 1. Определите, 
#каким по счету числом Фибоначчи оно является, 
#то есть выведите такое число n, что φ(n)=A.
#Если А не является числом Фибоначчи, выведите число -1.

A = 7
num1 = 0
num2 = 1
series = 0
s = 0
while s <= A:
    s = s+1
    if (A == series):
        print(s)
        break
    num1 = num2
    num2 = series
    series = num1 + num2
else: print("-1")




a = int(input('Введите число: '))
if (a <= 1):
    print ("Число не удовлетворяет условию задачи")

else:
    count = 3
    num = 1
    a1 = 1
    a2 = 1
    while (num < a):
        num = a1 + a2
        a1 = a2
        a2 = num
        count = count + 1
    if (num == a):
        print("Порядковый номер данного числа в последовательности Фибоначчи")
        print (count)
    else:
        print (-1)



n = int(input('Введите число -> '))

if n == 0:
    print(1)
else:
    frst, scnd, count = 0, 1, 2
    while scnd <= n:
        if scnd == n:
            print(count)
            break
        frst, scnd = scnd, frst + scnd
        count += 1
    else:
        print(-1)

