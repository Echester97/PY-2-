if __name__ == "__main__":
    class Animal:
        """Базавый класс, представляющий животное
        Атрибуты:
            name(str): Имя животного.
            age(int): Возраст животного в годах.
            _species(str): Вид животного
        """
        def __init__(self, name: str, age: int, species: str) -> None:
            self.name = name
            self.age = age
            self._species = species

        def __str__(self) -> str:
            return f"{self.name} ({self._species}), возраст: {self.age} лет"

        def __repr__(self) -> str:
            return f"Animal(name={self.name!r}, age={self.age!r}, species={self._species!r})"

        def make_sound(self) -> str:
            """Возвращает звукб который издает животное"""
            return "Звук не определен"

        def get_species(self) -> str:
            """Возвращает вид животного"""
            return self._species

    class Cat(Animal):
        """ Дочерний класс, представляющий кошку. Наследуется от Animal.

        Дополнительные атрибуты:
            color(str): Цвет шерсти.
            _lives(int): Количество жизней
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            super().__init__(name, age, species="Кошка")
            self.name = name
            self.color = color
            self._lives = 9
        def __str__(self) -> str:
            return f"{super().__str__()}, цвет: {self.color}"

        def __repr__(self) -> str:
            return f"Cat(name={self.name!r}, age={self.age!r}, color={self.color!r})"

        def make_sound(self) -> str:
            return "Мяу"

        def get_lives(self) -> int:
            return self._lives
