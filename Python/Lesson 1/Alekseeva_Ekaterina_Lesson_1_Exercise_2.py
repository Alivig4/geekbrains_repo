a = int(input("Введите количество секунд:"))
# вычислим целое количество часов
hours = int(a / 3600)
# убираем количество часов из общего значения
# так мы получим количство оставшихся минут и секунд
minutes_and_seconds = a - hours * 3600
# вычисляем количество минут
minutes = int(minutes_and_seconds / 60)
# убираем количество минут из значения
# так мы получим количство оставшихся секунд
seconds = minutes_and_seconds - minutes * 60

print("Результат без формата: %i:%i:%i" % (hours, minutes, seconds))

# минуты и секунды всегда должны быть в 2 символа, т.е. 1 минута должна отображаться как 01
hours_s = str(hours)
if hours<10:
    hours_s = "0" + str(hours)
minutes_s = str(minutes)
if minutes<10:
    minutes_s = "0" + str(minutes)
seconds_s = str(seconds)
if seconds<10:
    seconds_s = "0%i" % seconds
print("Результат с форматированием: %s:%s:%s" % (hours_s, minutes_s, seconds_s))

print("Магия: %i:%i:%i" % (int(a/3600), int((a%3600)/60), a%60))