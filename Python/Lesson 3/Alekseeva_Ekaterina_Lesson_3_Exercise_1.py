# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_division(val_1, val_2):
    if val_2 == 0:
        return "Ошибка! Деление на ноль!"
    return val_1/val_2

print(my_division(float(input("Введите делимое")), float(input("Введите делитель"))))