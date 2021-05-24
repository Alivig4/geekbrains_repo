earnings = float(input("Введите значение выручки:"))
expenses = float(input("Введите значение издержек:"))

if earnings > expenses:
    print("Прибыль — выручка больше издержек")
    profit = earnings - expenses
    efficiency = profit / earnings
    print("Рентабельность составляет %.2f" % efficiency)
    employers = int(input("Введите количество сотрудников:"))
    print("Прибыль на одного сотрудника составляет: %.2f" % (profit / employers))
else:
    print("Убыток — издержки больше выручки")