# Реализовать класс Road (дорога),
# в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.

# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        height = 5
        mass_per_square_meter = 25
        return self._length * self._width * height * mass_per_square_meter


some_road_1 = Road(10, 2)
some_road_2 = Road(100, 5)
some_road_3 = Road(100, 3)

print(f"Для дороги длинной {some_road_1._length} и шириной {some_road_1._width} понадобится {some_road_1.calculate_mass()} кг асфальта")
print(f"Для дороги длинной {some_road_2._length} и шириной {some_road_2._width} понадобится {some_road_2.calculate_mass()} кг асфальта")
print(f"Для дороги длинной {some_road_3._length} и шириной {some_road_3._width} понадобится {some_road_3.calculate_mass()} кг асфальта")