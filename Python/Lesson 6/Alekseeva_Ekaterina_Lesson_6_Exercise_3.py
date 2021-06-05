# Реализовать базовый класс Worker (работник),
# в котором определить атрибуты: name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
#
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]


position_1 = Position("Иван", "Иванов", "Инженер", {"wage": 50000, "bonus": 30000})
position_2 = Position("Петр", "Петров", "Начальник", {"wage": 100000, "bonus": 20000})

print(f"{position_1.get_full_name()}, {position_1.position}. Итого к выплате: {position_1.get_total_income()}")
print(f"{position_2.get_full_name()}, {position_2.position}. Итого к выплате: {position_2.get_total_income()}")