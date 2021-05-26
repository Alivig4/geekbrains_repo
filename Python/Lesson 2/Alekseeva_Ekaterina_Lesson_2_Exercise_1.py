# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

result_list = list()
# будем добавлять к списку данные разных типов
result_list.append(int(3.14))                               # целое
result_list.append(bin(52))                                 # двоичное
result_list.append(hex(124))                                # шестнадцатиричное
result_list.append(float(123.6112))                         # вещественное
result_list.append(complex(23.1, 12.2))                     # комплексное
result_list.append("hello"+" "+"world")                     # строка
result_list.append(reversed("!olleh"))                      # реверс строки
result_list.append(list("hello"))                           # список
result_list.append((12, 11, "hello", True))                 # кортеж
result_list.append(set("mylittlepony"))                     # множество
result_list.append({"a": 1, "c": False, 2: "True"})         # словарь
result_list.append(True)                                    # булевый тип
result_list.append(b"hello")                                # байтовый тип
result_list.append(None)                                    # None

for element in result_list:
    print(str(element)+" --> is type of "+ str(type(element)))
