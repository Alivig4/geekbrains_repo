# Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
#
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    direction_left = "лево"
    direction_right = "право"

    def __init__(self, name, color, is_police, initial_speed):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = initial_speed

    def print_description(self):
        if self.is_police:
            print(f"Полицейская {self.color} {self.name}")
        else:
            print(f"{self.color} {self.name}")

    def show_speed(self):
        print("\tТекущая скорость:", self.speed)

    def go(self):
        self.speed += 10
        print("Скорость увеличена")
        self.show_speed()

    def stop(self):
        self.speed = 0
        print("Машина остановилась")
        self.show_speed()

    def turn(self, direction):
        print("Поворот на", direction)


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print("\tСкорость превышена!!!")


class SportCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed < 100:
            print("\tПоднажми!!!")

    def go(self):
        self.speed += 10
        super().go()


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print("\tСкорость превышена!!!")


class PoliceCar(Car):
    def __init__(self, name, color, is_police, initial_speed):
        super().__init__(name, color, True, initial_speed)
        self.serene_is_on = initial_speed > 0

    def switch_serene(self):
        if not self.serene_is_on:
            self.serene_is_on = True
            print("\tСирена включена")
        else:
            self.serene_is_on = False
            print("\tСирена выключена")

    def go(self):
        if self.speed == 0:
            super().go()
            self.switch_serene()
        else:
            super().go()

    def stop(self):
        if self.speed > 0:
            super().stop()
            self.switch_serene()
        else:
            super().stop()


# основная программа
# создаем объекты
cars = [
    TownCar("Kia", "Белая", False, 0),
    TownCar("Reno", "Красная", False, 40),
    PoliceCar("Porsche", "Белая", False, 50),
    PoliceCar("Porsche", "Черная", True, 0),
    WorkCar("Трактор", "Грязный", False, 0),
    SportCar("Гоночная Lambo", "Красная", False, 0)
]

# прогоняем все функции на всех объектах
for car in cars:
    print("Тестирование машины начато")
    car.print_description()
    print("Разгон:")
    car.go()
    car.go()
    car.go()
    car.go()
    car.go()
    car.go()
    print("Остановка:")
    car.stop()
    print("Повороты:")
    car.turn(Car.direction_left)
    car.turn(Car.direction_right)
    print("Тестирование машины закончено\n")


