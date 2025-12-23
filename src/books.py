from datetime import datetime
from constans import CoverType  


class Book:
    """ Базовый класс для представления книги"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, cover_type: CoverType, isbn: str, condition: int = 100, has_images: bool = False) -> None:
        """
        Конструктор класса Book с валидацией всех параметров
        Параметры:
        title - название книги
        author - автор книги
        year - год издания
        genre - жанр книги
        cover_type - тип обложки (из CoverType)
        isbn - ISBN книги
        condition - состояние книги (0-100, по умолчанию 100)
        has_images - наличие иллюстраций (по умолчанию False)
        """
        
        # Валидация названия книги
        if title == "" or title is None:
            raise ValueError("название не может быть пустым")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in title:
                raise ValueError(f"в названии не могут содержаться спец. символы {title}")

        # Валидация автора
        if author == "" or author is None:
            raise ValueError("автор должен быть назван")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in author:
                raise ValueError(f"автор не может содержать спец. символы. Значение {author} не допустимо")

        # Валидация года 
        if type(year) != int:
            raise TypeError('Год должен быть числом')
        if year < 1800 or year > 2027:
            raise ValueError(f"год должен быть от 1800 до 2027. Получено: {year}")

        # Валидация жанра
        if genre == "" or genre is None:
            raise ValueError("жанр не может быть пустым")
        for char in genre:
            if char.isdigit():
                raise ValueError(f"жанр не может быть числом. Значение {genre} не допустимо")
        for symbol in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            if symbol in genre:
                raise ValueError(f"жанр не может содержать спец. символы. Значение {genre} не допустимо")
        
        # Валидация состояния 
        if type(condition) != int:
            raise TypeError(f"состояние должно быть числом. Получено: {condition}")
        if condition < 0 or condition > 100:
            raise ValueError(f"состояние должно быть от 0 до 100. Получено: {condition}")

        # Валидация типа обложки
        if cover_type not in [CoverType.HARD, CoverType.SOFT, CoverType.GLOSSY]:
            raise ValueError(f"неверный тип обложки: {cover_type}")

        # Валидация ISBN
        if isbn == "" or isbn is None:
            raise ValueError("ISBN не может быть пустым")

        # Инициализация атрибутов объекта
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.cover_type = cover_type 
        self.isbn = isbn
        self.has_images = has_images
        self._borrow_count = 0  # Счетчик взятий книги
        self._is_borrowed = False  # Флаг взятия книги
        self.condition = condition  # Состояние книги (0-100)

    def __repr__(self) -> str:
        """Официальное строковое представление"""
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.cover_type}', '{self.isbn}', '{self.condition})"

    def __str__(self) -> str:
        """Неформальное строковое представление"""
        return f"'{self.title}' - {self.author} ({self.year})"

    def get_age(self, current_year: int = datetime.now().year) -> int:
        """Возраст книги в годах"""
        return current_year - self.year

    def get_condition(self) -> str:
        """Текстовое описание состояния книги"""
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
        """Обновление состояния книги, ограничение значения от 0 до 100"""
        self.condition = max(0, min(100, self.condition + change))

    def borrow(self) -> bool:
        """Взятие книги, если она ещё не взята"""
        if not self._is_borrowed:
            self._is_borrowed = True
            self._borrow_count += 1
            return True
        return False

    def return_book(self) -> None:
        """Возвращение книгу"""
        self._is_borrowed = False

    def is_borrowed(self) -> bool:
        """Проверка, взята ли книга"""
        return self._is_borrowed

    def borrow_count(self) -> int:
        """Количество взятий книги"""
        return self._borrow_count

    def damage(self, amount: int) -> None:
        """Нанесение урона"""
        if amount < 0:
            raise ValueError("урон не может быть отрицательным")
        self.update_condition(-amount)


class HardCover(Book):
    """Класс для книг с твердой обложкой"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, 
                 isbn: str, condition: int = 100, has_images: bool = False) -> None:
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, CoverType.HARD, isbn, condition, has_images)
        self.cover_type = CoverType.HARD
        self.has_images = has_images
        self.update_condition(20)  # Бонус к состоянию для твердой обложки

    def __repr__(self) -> str:
        """Официальное строковое представление"""
        return f"HardCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
               f"'{self.isbn}', has_images={self.has_images}')"

    def __str__(self) -> str:
        """Неформальное строковое представление"""
        return f"Твёрдая обложка '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:
        """Описание состояния книги (наследуется от Book)"""
        base_condition = super().get_condition()
        return base_condition

    def damage(self, amount: int = 5) -> None:
        """Нанесение урона книге с твердой обложкой"""
        actual_damage = max(1, amount // 2)  # Урон уменьшается вдвое
        self.update_condition(-actual_damage)


class SoftCover(Book):
    """Класс для книг с мягкой обложкой"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, 
                 isbn: str, condition: int = 100, has_images: bool = False) -> None:
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, CoverType.SOFT, isbn, condition, has_images)
        self.cover_type = CoverType.SOFT
        self.has_images = has_images

    def __repr__(self) -> str:
        """Официальное строковое представление"""
        return f"SoftCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
           f"'{self.isbn}', has_images={self.has_images}')"

    def __str__(self) -> str:
        """Неформальное строковое представление"""
        return f"Мягкая обложка '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:
        """Описание состояния книги (наследуется от Book)"""
        base_condition = super().get_condition()
        return base_condition

    def damage(self, amount: int = 10):
        """Нанесение урона книге с мягкой обложкой"""
        self.update_condition(-amount)


class GlossyCover(Book):
    """Класс для книг с глянцевой обложкой"""
    
    def __init__(self, title: str, author: str, year: int, genre: str, 
                 isbn: str, condition: int = 100, has_images: bool = True) -> None:
        # Вызов конструктора родительского класса
        super().__init__(title, author, year, genre, CoverType.GLOSSY, isbn, condition, has_images)
        self.cover_type = CoverType.GLOSSY
        self.has_images = has_images
        self._scratches = 0  # Счетчик царапин для глянцевой обложки

    def __repr__(self):
        """Официальное строковое представление"""
        return f"GlossyCover ('{self.title}', '{self.author}', {self.year}, '{self.genre}', " \
               f"'{self.isbn}', has_images={self.has_images}, scratches={self._scratches}')"
    
    def __str__(self):
        """Неформальное строковое представление"""
        images = "с иллюстрациями" if self.has_images else ""
        return f"Глянцевая обложка {images}: '{self.title}' - {self.author} ({self.year})"

    def get_condition(self) -> str:
        """Описание состояния книги с учетом царапин"""
        base_condition = super().get_condition()
        
        # Определение описания царапин
        if self._scratches == 0:
            scratch_text = "без царапин"
        elif self._scratches <= 3:
            scratch_text = "несколько царапин"
        elif self._scratches <= 10:
            scratch_text = "много царапин"
        else:
            scratch_text = "сильно поцарапана"

        return f"{base_condition}, {scratch_text}" # Возвращаем и общее состояние и царапины

    def add_scratches(self, count: int = 1) -> None:
        """Добавление царапин на глянцевую обложку"""
        self._scratches += count
        self.update_condition(-count * 2)  # Каждая царапина ухудшает состояние на 2

    def damage(self, amount: int = 10):
        """Нанесение урона книге с глянцевой обложкой"""
        self.update_condition(-amount)