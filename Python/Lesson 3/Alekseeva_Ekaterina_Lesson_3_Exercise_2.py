# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def pretty_user_print(first_name, last_name, birth_year, city, email, phone):
    print(f"{last_name} {first_name}, {birth_year} года рождения.\nПроживает в городе {city}.\nemail: {email}\nтелефон: {phone}")


name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
year = int(input("Введите год рождения: "))
city = input("Введите город проживания: ")
email = input("Введите email: ")
phone_number = input("Введите телефон: ")

print("\nПолучены следующие данные: \n")
pretty_user_print(first_name=name, last_name=last_name, birth_year=year, city=city, email=email, phone=phone_number)