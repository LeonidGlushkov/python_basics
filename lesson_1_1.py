duration = int(input('введите время в секундах - '))
    years = duration // 31104000
    months = duration % 31104000 // 2592000
    day = duration % 2592000 // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 3600 // 60
    second = duration % 60
if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    print(minutes, 'мин', second, 'сек')
elif 3600 <= duration < 86400:
    print(hour, 'ч', minutes, 'мин', second, 'сек')
elif 86400 <= duration < 2592000:
    print(day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')
elif 2592000 <= duration < 31104000:
    print(months, 'мес', day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')
elif duration >= 31104000:
    print(years, 'г', months, 'мес', day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')
