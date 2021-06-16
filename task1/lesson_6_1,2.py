import requests


#задача 1
r = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
list_of_tuple = []
with open('pars.txt', encoding='utf-8') as f:
    for line in f:
        list_from_string = line.replace('-', '').replace('"', '').split()  # created a list from a string
        list_of_tuple.append((list_from_string[0], list_from_string[3], list_from_string[4]))
print(list_of_tuple)

#задача 2
