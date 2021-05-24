# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

original_list = input("Введите элементы списка через запятую:").split(',')
print("Оригинал:", original_list)

# перестановка на месте
switch_number = int(len(original_list)/2)
while switch_number > 0:
    original_list[switch_number*2-1], original_list[switch_number*2-2] = original_list[switch_number*2-2], original_list[switch_number*2-1]
    switch_number -= 1

print("После перестановки", original_list)

# перестановка через новый список
new_list = list()
switch_number = int(len(original_list)/2)
current_switch = 0
while current_switch < switch_number:
    new_list.append(original_list[current_switch*2+1])
    new_list.append(original_list[current_switch*2])
    current_switch += 1

new_list.append(original_list[-1]) if int(len(original_list))%2 > 0 else None

print("После обратной перестановки", new_list)