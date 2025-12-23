from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *


class TestGlossyCover:
    """Тесты для класса GlossyCover (книги с глянцевой обложкой)"""
    
    def test_create_glossycover(self):
        """Тест создания объекта GlossyCover"""
        book = GlossyCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', 'ISBN-026', 36, True)
        
        # Проверка, что созданный объект является экземпляром GlossyCover и Book
        assert isinstance(book, GlossyCover)
        assert isinstance(book, Book)
        
        # Проверка атрибута has_images (для глянцевых обложек обычно есть изображения)
        assert book.has_images == True

    def test_glossycover_add_scratches(self):
        """Тест добавления царапин на глянцевую обложку"""
        book = GlossyCover('Дневник последнего алхимика', 'Чжан Ли', 2000, 'Жанр', 'ISBN-024', 80)
    
        # Начальное состояние: 80 > 70 = "Хорошая", царапин нет
        assert book.get_condition() == 'Хорошая, без царапин'
    
        # Добавление 3 царапин
        book.add_scratches(3)
        # Каждая царапина ухудшает состояние на 2%, царапин: 3, состояние: 80 - (3*2) = 74
        # 74 > 70 = "Хорошая", царапин <= 3 = "несколько царапин"
        assert book.get_condition() == 'Хорошая, несколько царапин'
    
        # Добавление еще 2 царапин
        book.add_scratches(2)
        # Всего царапин: 5, состояние: 74 - (2*2) = 70
        # 70 <= 70 = "Поношенная", царапин <= 10 = "много царапин"
        assert book.get_condition() == 'Поношенная, много царапин'

    def test_glossycover_damage_with_scratches(self):
        """Тест нанесения урона книге с глянцевой обложкой с учетом царапин"""
        book = GlossyCover('Название', 'Чжан Ву', 2000, 'Жанр', 'ISBN-022', 100)
        # Добавление царапин и нанесение урона
        book.add_scratches(2)
        book.damage(10)
        
        # Проверка итогового состояния книги
        # Начальное состояние: 100
        # После 2 царапин: 100 - (2*2) = 96
        # После урона 10: 96 - 10 = 86
        # 86 > 70 = "Хорошая", царапин <= 3 = "несколько царапин"
        assert book.get_condition() == 'Хорошая, несколько царапин'