price_list = [57.8, 23.51, 23, 54, 93.46, 1007, 2345, 500, 5, 78, 7, 0.55]
# A
for i in price_list:
    if price_list[::-1].index(i) == 0:
        print(f'{int(i):02} руб {(i%1)}')

# B
print(id(price_list))
price_list.sort()
print(id(price_list))

# C
price_list_sort = sorted(price_list, reverse=True)
print(price_list,id(price_list))
print(price_list_sort,id(price_list_sort))

#D
for i in price_list[-5:]:
    if price_list[::-1].index(i) == 0:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп')
    else:
        print(f'{int(i)} руб {(i % 1 * 100):02.0f} коп', end=', ')
