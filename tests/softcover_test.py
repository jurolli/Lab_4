from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *


class TestSoftCover:
    """Тесты для класса SoftCover (книги с мягкой обложкой)"""
    
    def test_create_softcover(self):
        """Тест создания объекта SoftCover"""
        book = SoftCover('Правила общения с морскими богами', 'Автор', 2000, 'Роман','ISBN-018', 100, False)
        
        # Проверка, что созданный объект является экземпляром SoftCover и Book
        assert isinstance(book, SoftCover)
        assert isinstance(book, Book)
        
        # Проверка атрибута has_images (для книги без иллюстраций)
        assert book.has_images == False

    def test_softcover_damage(self):
        """Тест нанесения урона книге с мягкой обложкой"""
        book = SoftCover('Почему дети так делают', 'Автор', 2000, 'Жанр', 'ISBN-019', 100)
        
        # Нанесение урона 15 единиц
        book.damage(15)
        
        # Для мягкой обложки урон применяется полностью: 100 - 15 = 85
        assert book.condition == 85

    def test_softcover_default_damage(self):
        """Тест нанесения урона по умолчанию (без указания значения) для мягкой обложки"""
        book = SoftCover('Как научиться молчать', 'Автор', 2020, 'Жанр', 'ISBN-020', 100)
        
        # Нанесение урона без указания значения (должно использоваться значение по умолчанию)
        book.damage()
        
        # Для SoftCover damage() по умолчанию должно наносить 10 единиц урона: 100 - 10 = 90
        assert book.condition == 90

    def test_softcover_severe_damage(self):
        """Тест сильного повреждения мягкой обложки (снижение состояния до минимального значения)"""
        book = SoftCover('Физика на пальцах', 'Автор', 2015, 'Жанр', 'ISBN-021', 80)
        
        # Нанесение значительного урона
        book.damage(90)
        
        # Состояние не должно опуститься ниже 0: 80 - 90 = -10, но ограничено 0
        assert book.condition == 0
        # Проверка текстового описания состояния
        assert book.get_condition() == "Аварийное состояние"

    def test_softcover_borrow_with_damage(self):
        """Тест взаимодействия взятия книги с повреждением мягкой обложки"""
        book = SoftCover('Почему вас не замечают', 'Автор', 2018, 'Жанр', 'ISBN-022', 95)
        
        # Взятие книги должно уменьшить состояние (в методе borrow_book в симуляции)
        # Здесь проверяем, что методы можно вызывать последовательно
        book.borrow()
        assert book.is_borrowed() == True
        
        # Нанесение урона взятой книге
        book.damage(20)
        assert book.condition == 75
        
        # Возврат книги и повторное нанесение урона
        book.return_book()
        assert book.is_borrowed() == False
        
        book.damage(10)
        assert book.condition == 65
        assert book.get_condition() == "Хорошая"