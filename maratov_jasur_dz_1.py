one_min = 60
one_hour = one_min * 60
one_day = one_hour * 24

duration = int(input("Укажите продолжительность в секундах: "))
if duration < one_min:
    print(f"{duration} сек")
elif duration >= one_min and duration < one_hour:
    my_min = duration // one_min
    my_sec = duration * one_min
    print(f"{my_min} мин, {my_sec} сек")
elif duration >= one_hour and duration < one_day:
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration * one_min
    print(f"{my_hour} час, {my_min} мин, {my_sec} сек")
elif duration >=  one_day:
    my_day = duration // one_day
    duration = duration % one_day
    my_hour = duration // one_hour
    duration = duration % one_hour
    my_min = duration // one_min
    my_sec = duration % one_min
    print(f"{my_day} дн, {my_hour} час, {my_min} мин, {my_sec} сек")