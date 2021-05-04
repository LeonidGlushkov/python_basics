this_is_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '-5', 'градусов']
new_list = []
for i in this_is_list:
    if i.isdigit():
        new_list.append('"')
        new_list.append(f'{int(i):02}')
        new_list.append('"')
    elif i[0] == '+' or i[0] == '-':
        new_list.append('"')
        new_list.append(f'{i[0]}{int(i[1:]):02}')
        new_list.append('"')
    else:
        new_list.append(i)
print(new_list)

a = ' '.join(new_list)
print(a)






print(this_is_list)
