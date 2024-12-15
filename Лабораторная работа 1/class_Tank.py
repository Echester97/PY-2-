# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Tank:
    def __init__(self, capacity_volume:int, occupied_volume:int):
        """
        Создание объекта "Танк"

        :param capacity_volume: Вместимость танка
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> tank = Tank(5000,2000)
        """
        if capacity_volume <= 0:
            raise ValueError ("Объем танка должен быть положительный числом")
        if occupied_volume < 0 or occupied_volume > capacity_volume:
            raise ValueError ("Неверный объем жидкости")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume

    def is_full(self) -> bool:
        """"
        Функция которая проверяет, заполнен ли танк.

        :return: Является ли танк заполненным

        Примеры:
        >>> tank = Tank(5000, 5000)
        >>> tank.is_full()
        """
        ...

    def fill_fuel(self, fuel:float) -> None:
        """
        Заполняет танк топливом.

        :param fuel: Объем добавляемого топлива
        :raise ValueError: Если добавляемое топливо превышает вместимость танка
        :raise ValueError: Ecли добавляемое топливо не является положительным числом
        :raise TypeError: Ecли топливо не является числом

        Примеры:
        >>> tank = Tank(5000,1000)
        >>> tank.fill_fuel(3000)
        """
        if not isinstance(fuel,(int,float)):
          raise TypeError("Добавляемое топливо должно быть числом (int или float)")
        if fuel <= 0:
          raise ValueError("Добавляемое топливо должно быть положительным числом")
        if self.occupied_volume + fuel > self.capacity_volume:
          raise ValueError("Недостаточно места в танке для добавления топлива")
        ...

    def use_fuel(self, used_fuel:int) -> int:
      """
      Использование топлива из танка.

      : param used_fuel: Объем используемого топлива
      : return: Реально использованный объем топлива
      : raise ValueError: Если объем топлива меньше нуля
      : raise TypeError: Если объем топлива не является числом

      Примеры:
      >>> tank = Tank(5000,2000)
      >>> tank.use_fuel(1500)
      """
      if not isinstance(used_fuel,(int,float)):
        raise TypeError("Используемое топливо должно быть числом (int или float)")
      if used_fuel < 0:
        raise ValueError("Используемое топливо должно быть положительным числом")
      ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
    pass
