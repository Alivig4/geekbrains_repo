# Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

item_list = list()  # здесь будем хранить товары
# что бы не напутать с неймингом будем хранить названия ключей
name_key = "название"
price_key = "цена"
counter_key = "ед"
quantity_key = "количество"

while True:
    # запросим данные у пользователя
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    counter = input("Введите единицу измерения товара: ")
    quantity = int(input("Введите количество товара: "))

    # сформируем словарь товара
    item_dict = {name_key: name, price_key: price, counter_key: counter, quantity_key: quantity}
    # добавим в список товаров. в качестве номера будем использовать размер списка + 1
    item_list.append((len(item_list)+1, item_dict))

    retry = int(input("Продолжить? (1/0) "))
    if retry == 0:
        break

print("Полученные данные: ")
print(item_list)

# проанализируем данные. для каждой характеристики будем использовать свой список
names_list = list()
prices_list = list()
counters_list = list()
quantities_list = list()

for item_tuple in item_list:
    names_list.append(item_tuple[1][name_key])
    prices_list.append(item_tuple[1][price_key])
    counters_list.append(item_tuple[1][counter_key])
    quantities_list.append(item_tuple[1][quantity_key])

analytics_dict = {name_key: names_list, price_key: prices_list, counter_key: counters_list, quantity_key: quantities_list}

# выведем данные
print(analytics_dict)