this_is_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(this_is_list):
    if not this_is_list[i].isalpha():
        if this_is_list[i][0] == '+' or this_is_list[i][0] == '-':
            this_is_list[i] = f'{this_is_list[i][0]}{int(this_is_list[i][1:]):02}'
            this_is_list.insert(i, '"')
            this_is_list.insert(i + 2, '"')
            i += 3
            continue
        this_is_list[i] = f'{int(this_is_list[i]):02}'
        this_is_list.insert(i, '"')
        this_is_list.insert(i + 2, '"')
        i += 3
    else:
        i += 1

print(' '.join(this_is_list))
