
from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *
import pytest

class TestHardCover:
    
    def test_create_hardcover(self):
        book = HardCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', CoverType.HARD, 'ISBN-026', 36, True)
        assert isinstance(book, HardCover)
        assert isinstance(book, Book)
        assert book.has_images == True

    def test_hardcover_damage(self):
        book = HardCover('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', CoverType.GLOSSY, 'ISBN-026', 100, True)
        
        book.damage(10)
        assert book.condition == 95
        
        book.damage(100)
        assert book.condition == 45