# Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней прибыли ее не включать.

# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.

companies_dict = {}
total_positive_companies = 0
average_income = 0
with open("Files/File_Exercise_7.txt") as data_file:
    for line in data_file:
        company_name, company_type, income, outcome = line.split(" ")
        company_total = float(income) - float(outcome)
        companies_dict[company_name] = company_total
        if company_total > 0:
            average_income += company_total
            total_positive_companies += 1

# составим итоговый список
companies_list = [(companies_dict), {"average_profit": average_income/total_positive_companies}]

# сохраним в файл
with open("Files/File_Exercise_7_out.json", "w") as out_file:
    print(companies_list, file=out_file)
