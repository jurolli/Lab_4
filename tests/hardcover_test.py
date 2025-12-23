from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *
import pytest


class TestHardCover:
    """Тесты для класса HardCover (книги с твердой обложкой)"""
    
    def test_create_hardcover(self):
        """Тест создания объекта HardCover"""
        book = HardCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', 'ISBN-026', 36, True)
        
        # Проверка, что созданный объект является экземпляром HardCover и Book
        assert isinstance(book, HardCover)
        assert isinstance(book, Book)
        
        # Проверка атрибута has_images (для книги с иллюстрациями)
        assert book.has_images == True

    def test_hardcover_damage(self):
        """Тест нанесения урона книге с твердой обложкой"""
        book = HardCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', 'ISBN-026', 100, True)
        
        # Нанесение урона 10 единиц
        book.damage(10)
        # Для твердой обложки урон уменьшается вдвое: 100 - (10 // 2) = 100 - 5 = 95
        assert book.condition == 95
        
        # Нанесение урона 100 единиц
        book.damage(100)
        # Урон уменьшается вдвое: 95 - (100 // 2) = 95 - 50 = 45
        assert book.condition == 45