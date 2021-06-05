# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов методы должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self, color):
        self.title = "Ручка"
        self.color = color

    def draw(self):
        print(f"{self.title} пишет чернилами. Цвет чернил: {self.color}")


class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        print(f"{self.title} простой, черный. Хорошо заточен!")


class Handle(Stationery):
    def __init__(self, color):
        self.title = "Маркер"
        self.color = color

    def draw(self):
        print(f"{self.title} рисует на любой поверхности! Цвет: {self.color}")


stationeries = [Pen("Синий"), Pencil(), Handle("Красный"), Handle("Зеленый")]
print("Канцелярские принадлежности которые у нас есть:")
for obj in stationeries:
    obj.draw()
