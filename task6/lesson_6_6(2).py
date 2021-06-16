from sys import argv, maxsize
from itertools import islice

with open('bakery.csv', encoding='utf-8') as price:
    if len(argv) == 1:
        content = price.read()
        print(content, end='')
    elif len(argv) == 2:
        for line in islice(price, int(argv[1]) - 1, maxsize):
            print(line, end='')
    elif len(argv) == 3:
        for line in islice(price, int(argv[1]) - 1, int(argv[2])):
            print(line, end='')