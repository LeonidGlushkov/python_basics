duration = int(input('введите время в секундах - '))
if duration < 60:
    print(duration, 'сек')
elif 60 <= duration < 3600:
    minutes = duration // 60
    second = duration % 60
    # if second == 0:
    #     print(minutes, 'мин')
    # else:
    print(minutes, 'мин', second, 'сек')
elif 3600 <= duration < 86400:
    hour = duration // 3600
    minutes = duration % 3600 // 60
    second = duration % 3600 % 60
    # if minutes == 0:
    #     print(hour, 'ч', second, 'сек')
    #     if second == 0:
    #         print(hour, 'ч', minutes, 'мин')
    #         if minutes and second == 0:
    #             print(hour, 'ч')
    # else:
    print(hour, 'ч', minutes, 'мин', second, 'сек')
elif 86400 <= duration < 2592000:
    day = duration // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 86400 % 3600 // 60
    second = duration % 86400 % 3600 % 60
    print(day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')
elif 2592000 <= duration < 31104000:
    months = duration // 2592000
    day = duration % 2592000 // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 3600 // 60
    second = duration % 60
    print(months, 'мес', day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')
elif duration >= 31104000:
    years = duration // 31104000
    months = duration % 31104000 // 2592000
    day = duration % 2592000 // 86400
    hour = duration % 86400 // 3600
    minutes = duration % 3600 // 60
    second = duration % 60
    print(years, 'г', months, 'мес', day, 'д', hour, 'ч', minutes, 'мин', second, 'сек')