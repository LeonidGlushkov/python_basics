def thesaurus(*args: str) -> dict:
    names = {}
    for i in args:
        names.setdefault(i[0],[])
        names[i[0]].append(i)
    return dict(sorted(names.items()))


print(thesaurus('Иван', 'Пётр', 'Идрак', 'Алексей', 'Василий', 'Артём'))


def thesaurus_adv(*args: str) -> dict:
    names = {}
    for i in args:
        names.setdefault(i.split()[1][0],{})
        names[i.split()[1][0]].setdefault(i.split()[0][0],[])
        names[i.split()[1][0]][i.split()[0][0]].append(i)
    return dict(sorted(names.items()))


print(thesaurus_adv('Иван Сергеев', "Инна Серова", "Петр Алексеев",
                    "Илья Иванов", "Анна Савельева"))