# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
#
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.


from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def required_fabric_length(self):  # возвращает сколько нужно ткани
        pass


class Coat(Clothes):
    def __init__(self, V):
        self.V = V

    @property
    def required_fabric_length(self):
        return self.V/6.5 + 0.5

    def __str__(self):
        return f"Пальто {self.V} размера"


class Costume(Clothes):
    def __init__(self, H):
        self.H = H

    @property
    def required_fabric_length(self):
        return 2 * self.H + 0.3

    def __str__(self):
        return f"Костюм на рост {self.H}"


clothes_to_produce = [
    Costume(150),
    Costume(165),
    Coat(42),
    Coat(53),
    Coat(57),
    Costume(180),
    Costume(195),
]

total_fabric_needed = 0
print("Нужно произвести следующее:")
for item in clothes_to_produce:
    print(item)
    total_fabric_needed += item.required_fabric_length

print(f"\nПонадобится {total_fabric_needed:.2f} метров ткани")
