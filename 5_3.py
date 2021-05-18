from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена',
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А',
]

tutors_classes = (i for i in zip_longest(tutors, classes[:len(tutors)]))


print(type(tutors_classes))