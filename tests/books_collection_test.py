
from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *

class TestBookCollection:
    
    def test_create_collection(self):
        collection = BookCollection('Моя коллекция')
        assert collection.name == 'Моя коллекция'
        assert len(collection) == 0

    def test_add_book_to_collection(self):
        collection = BookCollection('Коллекция')
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман', CoverType.HARD, 'ISBN-001', 79, False)
        
        collection.add_book(book)
        assert len(collection) == 1
        assert book in collection

    def test_remove_book_from_collection(self):
        collection = BookCollection('Коллекция')
        book = Book('Дневник последнего алхимика', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        
        collection.add_book(book)
        assert len(collection) == 1
    
        result = collection.remove_by_title('Дневник последнего алхимика')
        assert result == True
        assert len(collection) == 0
        
        result = collection.remove_by_title('Несуществующая')
        assert result == False

    def test_collection_iteration(self):
        collection = BookCollection('Коллекция')
        book1 = Book('Записки провинциального врача', 'Мария дель Мар Родригес', 2000, 'Жанр', CoverType.HARD,'ISBN-025')
        book2 = Book('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', CoverType.HARD, 'ISBN-026', 36)
        
        collection.add_book(book1)
        collection.add_book(book2)
        
        books = list(collection)
        assert len(books) == 2
        assert book1 in books
        assert book2 in books