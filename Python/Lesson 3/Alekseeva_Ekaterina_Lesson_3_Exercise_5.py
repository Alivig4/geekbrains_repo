# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

print("Вводите числа разделяя их пробелом.\nПосле каждого ввода будет выводиться сумма этих чисел.")
print("Продолжайте вводить числа и они будут добавляться к предыдущему значению.")
print("Для завершения используйте символ \"!\".")


def sum_from_input(input_string):
    """
    Возвращает сумму всех чисел в строке, разделенных пробелом
    Не числа будут игнорироваться
    И флаг нужно ли продолжить выполнение программы
    Если встретится символ "!" то посчитается сумма до этого символа и программа завершится
    """
    values = input_string.split()
    current_sum = 0
    for string_value in values:
        # если число, прибавляем к сумме
        if string_value.isdigit():
            current_sum += float(string_value)
        # если содержит "!" завершаем не доходя до конца
        if "!" in string_value:
            # выйти из функции, указав что нужно закончить выполнение программы
            return current_sum, False
    return current_sum, True


total_sum = 0
should_continue = True
while should_continue:
    new_sum, should_continue = sum_from_input(input("Введите строку: "))
    total_sum += new_sum
    print("Текущая сумма:", total_sum)

print("Работа завершена!")