from itertools import zip_longest
import sys

# 3
dict_users_hobby = {}
with open('users.csv', encoding='utf-8') as users, open('hobby.csv', encoding='utf-8') as hobby:
        users_list = users.readlines()
        hobby_list = hobby.readlines()
        if len(users_list) >= len(hobby_list):
            for k, v in zip_longest(users_list, hobby_list):
                dict_users_hobby.setdefault(k,v)
            with open('users_hobby.csv', 'w', encoding='utf-8') as f:
                f.write(str(dict_users_hobby))
        else:
            print('Ошибка')
            sys.exit(1)

# 4
with open('users.csv', encoding='utf-8') as users, open('hobby.csv', encoding='utf-8') as hobby, open('users_hobby.txt',
                                                                                                      'w',
                                                                                                      encoding='utf-8') as f:
    for k, v in zip_longest(users, hobby):
        if k:
            f.write(f'{str(k).strip()}:{str(v).strip()}\n')
        else:
            sys.exit(1)

# 5
with open(sys.argv[1], encoding='utf-8') as users, open(sys.argv[2], encoding='utf-8') as hobby, open(sys.argv[3],
                                                                                                      'w',
                                                                                                      encoding='utf-8') as f:
    for k, v in zip_longest(users, hobby):
        if k:
            f.write(f'{str(k).strip()}:{str(v).strip()}\n')
        else:
            sys.exit(1)
