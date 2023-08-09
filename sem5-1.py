


def FibbonachyNumber(value):
    if value <= 1:
        return 1
    else:
        return (FibbonachyNumber(value - 1) + FibbonachyNumber(value - 2))

while True:
    n = int(input('Введите интересующую вас Номер числа Фиббоначи -> '))
    if n < 1:
        print('Вы ввели отрицательное число или 0')
    else:
        break
print(f'Число Фибонначи в позиции {n} - {FibbonachyNumber(n)}')