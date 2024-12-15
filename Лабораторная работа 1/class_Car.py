# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Car:
    def __init__(self,brand:str, model:str, fuel_capacity: float, fuel_level:float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param brand: Марка автомобиля
        :param model: Модель автомобиля
        :param fuel_capacity: Емкость топливного бака
        :param fuel_level: Уровень топлива в баке

        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 10)  # инициализация экземпляра класса
        """
        if not isinstance(brand, str):
            raise TypeError("Марка автомобиля должна быть строкой")
        if not isinstance(model, str):
            raise TypeError("Модель автомобиля должна быть строкой")
        self.brand = brand
        self.model = model
        if not isinstance(fuel_capacity, (int, float)) or fuel_capacity <= 0:
            raise ValueError("Емкость топливного бака должна быть положительным числом")
        self.fuel_capacity = fuel_capacity
        if not isinstance(fuel_level, (int, float)) or fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным числом")
        if fuel_level > fuel_capacity:
            raise ValueError("Уровень топлива не может превышать емкость бака")
        self.fuel_level = fuel_level
        ...
    def is_empty_tank(self) -> bool:
        """
        Функция котороя проверяет, является ли топливный бак пустым.
        :return: True, если бак пустой, иначе False.

        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 0)
        >>> car.is_empty_tank()
        """
        ...
    def refuel(self, fuel_added: float) -> None:
        """
        Заправка автомобиля топливом.

        :param fuel_added: Количество добавляемого топлива
        :raise ValueError: Если добавляемое топливо превышает свободный объем бака.

        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 10)
        >>> car.refuel(30)
        """
        if not isinstance(fuel_added, (int, float)):
            raise TypeError("Добавляемое топливо должно быть числом")
        if fuel_added <= 0:
            raise ValueError("Количество добавляемого топлива должно быть положительным числом")
        if self.fuel_level + fuel_added > self.fuel_capacity:
            raise ValueError("Добавляемое топливо превышает объем бака")
        ...

    def drive(self, distance: float, fuel_consumption: float) -> None:
        """
        Движение автомобиля.

        :param distance: Расстояние в километрах
        :param fuel_consumption: Расход топлива на 100 км
        :raise ValueError: Если топлива недостаточно для поездки
        :raise ValueError: Ecли расстояние не является положительным числом
        :raise ValueError: Если расход топлива не является положителным числом
        Примеры:
        >>> car = Car("Toyota", "Camry", 60, 10)
        >>> car.drive(50, 8)
        """
        if not isinstance(distance, (int, float)) or distance <= 0:
            raise ValueError("Расстояние должно быть положительным числом")
        if not isinstance(fuel_consumption, (int, float)) or fuel_consumption <= 0:
            raise ValueError("Расход топлива должен быть положительным числом")
        required_fuel = (distance / 100) * fuel_consumption
        if required_fuel > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки")
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
