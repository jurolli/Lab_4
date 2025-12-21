
from datetime import datetime
from constans import CoverType

class Book:


    def __init__(self, title: str, author: str, year: int, genre: str, cover_type: CoverType, isbn: str, condition:int = 100, has_images: bool = False) -> None:
        
        if title == "" or title is None:
            raise ValueError("название не может быть пустым")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in title:
                raise ValueError(f"в названии не могут содержаться спец. символы {title}")

        if author == "" or author is None:
            raise ValueError("автор должен быть назван")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in author:
                raise ValueError(f"автор не может содержать спец. символы. Значение {author} не допустимо")


        if type(year) != int:
            raise TypeError('Год должен быть числом')
        
        if year < 1800 or year > 2027:
            raise ValueError(f"год должен быть от 1800 до 2027. Получено: {year}")

        if genre == "" or genre is None:
            raise ValueError("жанр не может быть пустым")
        for char in genre:
            if char.isdigit():
                raise ValueError(f"жанр не может быть числом. Значение {genre} не допустимо")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in genre:
                raise ValueError(f"жанр не может содержать спец. символы. Значение {genre} не допустимо")
        
        if type(condition) != int:
            raise TypeError(f"состояние должно быть числом. Получено: {condition}")
        
        if condition < 0 or condition > 100:
            raise ValueError(f"состояние должно быть от 0 до 100. Получено: {condition}")

        if cover_type not in [CoverType.HARD, CoverType.SOFT, CoverType.GLOSSY]:
            raise ValueError(f"неверный тип обложки: {cover_type}")

        if isbn == "" or isbn is None:
            raise ValueError("ISBN не может быть пустым")

        
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.cover_type = cover_type 
        self.isbn = isbn
        self.has_images = has_images
        self._borrow_count = 0 
        self._is_borrowed = False
        self.condition = condition


    def __repr__(self) -> str:
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.cover_type}', '{self.isbn}', '{self.condition})"

    def __str__(self) -> str:
        return f"'{self.title}' - {self.author} ({self.year})"

    def get_age(self, current_year: int = datetime.now().year) -> int:
        return current_year - self.year

    def get_condition(self) -> str:

        if self.condition > 90:
            return "Как новая"
        elif self.condition > 70:
            return "Хорошая"
        elif self.condition > 40:
            return "Поношенная"
        elif self.condition > 15:
            return "Сильно изношенная"
        else:
            return "Аварийное состояние"


    def update_condition(self, change: int) -> None:
        self.condition = max(0, min(100, self.condition + change))

    def borrow(self) -> bool:
        if not self._is_borrowed:
            self._is_borrowed = True
            self._borrow_count += 1
            return True
        return False

    def return_book(self) -> None:
        self._is_borrowed = False

    def is_borrowed(self) -> bool:
        return self._is_borrowed

    def borrow_count(self) -> int:
        return self._borrow_count

    def damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("урон не может быть отрицательным")
        self.update_condition(-amount)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return NotImplemented
        return self.isbn == other.isbn

class HardCover(Book):
    
    
    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, condition:int = 100, has_images: bool = False) -> None:
        super().__init__(title, author, year, genre, CoverType.HARD, isbn, condition, has_images)
        self.cover_type = CoverType.HARD
        self.has_images = has_images
        self.update_condition(20)

    def __repr__(self) -> str:
        return f"HardCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
               f"'{self.isbn}', has_images={self.has_images}')"

    def __str__(self) -> str:
        return f"Твёрдая обложка '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:
        base_condition = super().get_condition()
        return base_condition

    def damage(self, amount: int = 5) -> None:
        actual_damage = max(1, amount // 2)
        self.update_condition(-actual_damage)


class SoftCover(Book):

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, condition:int = 100, has_images: bool = False) -> None:
        super().__init__(title, author, year, genre, CoverType.SOFT, isbn, condition, has_images)
        self.cover_type = CoverType.SOFT
        self.has_images = has_images

    def __repr__(self) -> str:
        return f"SoftCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
           f"'{self.isbn}', has_images={self.has_images}')"

    def __str__(self) -> str:
        return f"Мягкая обложка '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:
        
        base_condition = super().get_condition()
        return base_condition


    def damage(self, amount: int = 10):
        self.update_condition(-amount)  

class GlossyCover(Book):

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, condition:int = 100, has_images: bool = True) -> None:
        super().__init__(title, author, year, genre, CoverType.GLOSSY, isbn, condition, has_images)
        self.cover_type = CoverType.GLOSSY
        self.has_images = has_images
        self._scratches = 0

    
    def __repr__(self):
        return f"GlossyCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
               f"'{self.isbn}', has_images={self.has_images}, scratches={self._scratches}')"
    
    def __str__(self):
        images = "с иллюстрациями" if self.has_images else ""
        return f"Глянцевая обложка {images}: '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:

        base_condition = super().get_condition()
        
        if self._scratches == 0:
            scratch_text = "без царапин"
        elif self._scratches <= 3:
            scratch_text = "несколько царапин"
        elif self._scratches <= 10:
            scratch_text = "много царапин"
        else:
            scratch_text = "сильно поцарапана"

        return f"{base_condition}, {scratch_text}"

    def add_scratches(self, count: int = 1) -> None:
        self._scratches += count
        self.update_condition(-count * 2)

    def damage(self, amount: int = 10):
        self.update_condition(-amount)  