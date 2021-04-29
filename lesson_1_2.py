cube = [number ** 3 for number in range(1, 1001) if number % 2 != 0]
summa = 0
for i in cube:
    sum_of_number = 0
    count = i
    while count != 0:
        sum_of_number += count % 10
        count //= 10
    if not sum_of_number % 7:
        summa += i
print(summa)
summa = 0
for i in cube:
    sum_of_number = 0
    count = i + 17
    while count != 0:
        sum_of_number += count % 10
        count //= 10
    if not sum_of_number % 7:
        summa += i + 17
print(summa)
