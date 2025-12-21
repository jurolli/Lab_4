
from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *

class TestSoftCover:
    
    def test_create_softcover(self):
        book = SoftCover('Правила общения с морскими богами', 'Автор', 2000, 'Роман', CoverType.SOFT, 'ISBN-018', 100, False)
        assert isinstance(book, SoftCover)
        assert isinstance(book, Book)
        assert book.has_images == False

    def test_softcover_damage(self):
        book = SoftCover('Почему дети так делают', 'Автор', 2000, 'Жанр', 'ISBN-019', 100)
        
        book.damage(15)
        assert book.condition == 85