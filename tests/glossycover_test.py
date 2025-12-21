

from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *


class TestGlossyCover:
    
    def test_create_glossycover(self):
        book = GlossyCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', 'ISBN-026', 36, True)
        assert isinstance(book, GlossyCover)
        assert isinstance(book, Book)
        assert book.has_images == True


    def test_glossycover_add_scratches(self):
        book = GlossyCover('Дневник последнего алхимика', 'Чжан Ли', 2000, 
                        'Жанр', 'ISBN-024', 80)
    
        # Начальное состояние: 80 > 70 = "Хорошая"
        assert book.get_condition() == 'Хорошая, без царапин'
    
        book.add_scratches(3)
        # Каждая царапина ухудшает состояние на 2%, царапин: 3, состояние: 80 - (3*2) = 74
        # 74 > 70 = "Хорошая", царапин <= 3 = "несколько царапин"
        assert book.get_condition() == 'Хорошая, несколько царапин'
    
        book.add_scratches(2)
        # Всего царапин: 5, состояние: 74 - (2*2) = 70
        # 70 <= 70 = "Поношенная", царапин <= 10 = "много царапин"
        assert book.get_condition() == 'Поношенная, много царапин'


    def test_glossycover_damage_with_scratches(self):
        book = GlossyCover('Название', 'Чжан Ву', 2000, 'Жанр', 'ISBN-022', 100)
        
        book.add_scratches(2)
        book.damage(10)
        
        assert book.get_condition() == 'Хорошая, несколько царапин'
        
