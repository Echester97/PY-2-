# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
class Chair:
    def __init__(self, material: str, height: float, weight_capacity: float, color:str):
        """
        Создание и подготовка к работе объекта "Стул"

        :param material: Материал, из которого сделан стул
        :param height: Высота стула
        :param weight_capacity: Максимальная нагрузка, которую может выдержать стул
        :param color: Цвет стула
        :raise TypeError: Если материал не является строкой
        :raise TypeError: Если цвет стула не является строкой
        :raise ValueError: Если высота стула не является положительным числом
        :raise ValueError: Если максимальная нагрузка не является положительным числом

        Примеры:
        >>> chair = Chair("Дерево", 1.0, 100,"Красная")  # инициализация экземпляра класса
        """
        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        self.material = material

        if not isinstance(height, (int, float)) or height <= 0:
            raise ValueError("Высота стула должна быть положительным числом")
        self.height = height

        if not isinstance(weight_capacity, (int, float)) or weight_capacity <= 0:
            raise ValueError("Максимальная нагрузка должна быть положительным числом")
        self.weight_capacity = weight_capacity

        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        self.color = color

    def sit_on_chair(self, weight: float) -> None:
        """
        Садиться на стул.

        :param weight: Вес сидящего
        :raise ValueError: Если вес сидящего превышает максимальную нагрузку стула.
        :raise ValueError: Если вес сидящего не являетя положительным числом

        Примеры:
        >>> chair = Chair("Пластик", 1.0, 90, "Красная")
        >>> chair.sit_on_chair(80)
        """
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес сидящего должен быть положительным числом")
        if weight > self.weight_capacity:
            raise ValueError("Вес превышает максимальную нагрузку стула")

    def change_material(self, new_material: str) -> None:
        """
        Изменить материал стула.

        :param new_material: Новый материал
        :raise TypeError: Если материал стула не является строкой

        Примеры:
        >>> chair = Chair("Дерево", 1.0, 100,"Красная")
        >>> chair.change_material("Металл")
        """
        if not isinstance(new_material, str):
            raise TypeError("Материал должен быть строкой")

    def paint_chair(self, new_color: str) -> None:
        """
        Покрасить стул в новый цвет.

        :param new_color: Новый цвет стула
        :raise TypeError: Если новый цвет сутла не является строкой

        Примеры:
        >>> chair = Chair("Дерево", 1.0, 100,"Коричневый")
        >>> chair.paint_chair("Синий")
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет должен быть строкой")




if __name__ == "__main__":
 # TODO работоспособность экземпляров класса проверить с помощью doctest
 doctest.testmod()
 pass
