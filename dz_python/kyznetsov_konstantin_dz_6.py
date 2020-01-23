# 1
'''
    Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). 
    Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. 
    Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. 
    Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). 
    Проверить работу примера, создав экземпляр и вызвав описанный метод.

    Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
'''


import time


color_time = {'read' : 7, 'elloy' : 2, 'grean' : 10}


class TrafficLight:
    def __init__(self, color=None):
        self.__color = color

    def running(self):
        for repit in range(3):
            for el in self.__color:
                print(el)
                time.sleep(self.__color[el])


traffic_light = TrafficLight(color_time)

traffic_light.running()


# 2
'''
    Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина). 
    Значения данных атрибутов должны передаваться при создании экземпляра класса. 
    Атрибуты сделать защищенными. 
    Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна. 
    Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна. 
    Проверить работу метода.

    Например: 20м*5000м*25кг*5см = 12500 т
'''

class Road:
    def __init__(self, lenght=None, width=None):
        self._lenght = lenght
        self._width = width

    def asphalt_calculation(self, mass=None, height=None):
        need_asphalt = self._lenght * self._width * mass * height
        print(need_asphalt)


road = Road(20, 5000)

road.asphalt_calculation(25, 5)


# 3
'''
    Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход). 
    Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}. 
    Создать класс Position (должность) на базе класса Worker. 
    В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income). 
    Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


income_dict = {"wage": 20000, "bonus": 500}


class Worker:
    def __init__(self, name=None, surname=None, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income_dict


class Position(Worker):
    def get_full_name(self):
        print(f'{worker.name} {worker.surname}')

    def get_total_income(self):
        self.get_full_name()
        print(int(self._income['wage']) + int(self._income['bonus']))


worker = Worker(name='Edward', surname='Snowden', position='CIA agent')

print(worker.position)

position_worker = Position()
                                           
position_worker.get_total_income()

# 4
'''
    Реализуйте базовый класс Car. 
    У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).  
    А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда). 
    Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. 
    Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. 
    Для классов TownCar и WorkCar переопределите метод show_speed. 
    При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

    Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed=0, color=None, name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car go')

    def stop(self):
        print('Car stop')

    def turn(self, direction):
        print(f'Car direction {direction}')

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.speed} превышение скорости')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.speed} превышение скорости')


class PoliceCar(Car):
    pass


work_car = WorkCar(speed=70, color='Read', name='Lada')

print(f'speed = {work_car.speed}, color = {work_car.color}, name = {work_car.name}, is_police = {work_car.is_police}')
work_car.go()
work_car.show_speed()
work_car.stop()
work_car.turn('left')


                                                                                                                                                       63,0-1      Внизу

# 5
'''
    Реализовать класс Stationery (канцелярская принадлежность). 
    Определить в нем атрибут title (название) и метод draw (отрисовка). 
    Метод выводит сообщение “Запуск отрисовки.” 
    Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер). 
    В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение. 
    Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self, title=''):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):
    pass


class Pencil(Stationery):
    pass


class Handle(Stationery):
    pass


stationery = Stationery()
pen = Pen('pen')
pencil = Pencil('pencil')
handle = Handle('handle')

stationery.draw()
pen.draw()
pencil.draw()
handle.draw()



