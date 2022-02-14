m = 60 # 1 мин
h = m * 60 # 1 час
d = h * 24 # 1 день

duration = int(input("Укажите продолжительность в секундах: "))
if duration <= m:
    print(f"{duration} сек")
elif m <= duration and h > duration:
    my_min = duration // m
    my_sec = duration % m
    print(f"{}{}")

    seconds = int(input("Укажите продолжительность в секундах: "))
    seconds = seconds % (24 * 3600)
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    days = seconds // 86400
    seconds = seconds % 86400
    print(f"{days} дн, {hours} час, {minutes} мин, {seconds} сек")