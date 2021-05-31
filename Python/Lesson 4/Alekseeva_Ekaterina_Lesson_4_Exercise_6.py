# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count
from itertools import cycle
from sys import argv


def generate_integers(start_number, quantity):
    # Первый скрипт
    return_value = []
    for number in count(start_number):
        if number >= start_number+quantity:
            break
        else:
            return_value.append(number)
    return return_value


def repeat_from_list(initial_list, quantity):
    # Второй скрипт
    return_value = []
    i = 0
    for number in cycle(initial_list):
        i += 1
        if i > quantity:
            break
        else:
            return_value.append(number)
    return return_value


command_recognized = False
if len(argv) > 1:
    command = argv[1]
    if command == "generate_integers":
        if len(argv) > 3:
            command_recognized = True
            start_number = int(argv[2])
            quantity = int(argv[3])
            print("Результат:", generate_integers(start_number, quantity))
    elif command == "repeat_integers":
        if len(argv) > 3:
            command_recognized = True
            quantity = int(argv[2])
            initial_list = [el for i, el in enumerate(argv) if i > 2]
            print("Результат:", repeat_from_list(initial_list, quantity))


if command_recognized == False:
    print("Ошибка!")
    print("\nДоступные команды:")
    print("generate_integers <start> <quantity>")
    print("\tвыводит список целых чисел начиная от start в количестве quantity")
    print("\nrepeat_integers <quantity> <numbers...>")
    print("\tвыводит списком повторяющиеся числа в количестве quantity числа передаются через запятую в любом количестве")
    exit()

