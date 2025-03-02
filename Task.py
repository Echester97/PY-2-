class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
    @property
    def name(self):
        return self.name
    @name.setter
    def name(self, value):
        raise AttributeError("Атрибут 'name' является неизменяемым")
    @property
    def author(self):
        return self.author
    @author.setter
    def author(self, value):
        raise AttributeError("Атрибут 'author' является неизменяемым")

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name,author)
        self.pages = pages
    @property
    def pages(self):
        self.pages
    @pages.setter
    def pages (self, value):
        if isinstance(value, int) or value <= 0:
            raise ValueError("pages должно быть положительным целым числом")
        self.pages = value
    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"pages={self.pages!r})")


class AudioBook:
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    @property
    def duration(self):
        self.duration
    @duration.setter
    def duration(self, value):
        if isinstance(value,(int,float)) or value <= 0:
            raise ValueError("duration должно быть положительным числом")
        self.duration = float(value)
    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, "
                f"duration={self.duration!r})")
