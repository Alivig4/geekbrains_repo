# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

try:
    script_name, hours_worked, hour_rate, extra_reward = argv
except:
    print("Данные переданы неверно!")
    print("Необходимо передать последовательно 3 параметра:")
    print("<выработка в часах> <ставка в час> <премия>")
    exit()

hours_worked = float(hours_worked)
hour_rate = float(hour_rate)
extra_reward = float(extra_reward)

print("Переданы следующие значения:")
print("Выработка в часах =", hours_worked)
print("Ставка в час =", hour_rate)
print("Премия =", extra_reward)

print("Итого необходимо выплатить:", hours_worked * hour_rate + extra_reward)