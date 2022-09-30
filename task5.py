# Задайте список из n чисел последовательности (1+ (1/n))^n и выведите на экран их сумму.
# Пример:
# - Для n = 5: сумма = 11,55

n = int(input('Введите количество чисел в последовательности '))
sum = 0
lst = []
for i in range(1, n+1):
    while i <=n:
        a = (1+(1/i))**i
        lst.append(a)
        sum += a
        i+=1
    else:
        break
print(lst)
print(round(sum,2))