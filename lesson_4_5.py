from sys import argv
import utils

if len(argv) == 1:
    print('Укажите наименование валюты!')
elif len(argv) == 2:
    print(utils.currency_rates(argv[1]))
else:
    print('только одно наименование!')