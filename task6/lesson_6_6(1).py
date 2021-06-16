import sys

with open('bakery.csv', 'a+', encoding='utf-8') as price:
    for line in sys.argv[1:]:
        price.write(f'{line}\n')