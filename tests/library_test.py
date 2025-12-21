

from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *
import pytest

class TestLibrary:
    
    def test_create_library(self):
        library = Library('Тестовая библиотека')
        assert library.name == 'Тестовая библиотека'
        assert len(library) == 0

    def test_add_book_to_library(self):
        library = Library('Библиотека')
        book =  Book('Дневник алхимика', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        
        library.add_book(book)
        assert len(library) == 1
        
        book2 =  Book('Дневник последнего cтоматолога', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        with pytest.raises(ValueError):
            library.add_book(book2)

    def test_search_books(self):
        library = Library('Библиотека')
        book1 = Book('Записки провинциального врача', 'Мария дель Мар Родригес', 2000, 'Жанр', CoverType.HARD,'ISBN-025', 69, True)
        book2 = Book('О чём молчат родители', 'Мария дель Мар Родригесе', 2010, 'Жанр', CoverType.HARD, 'ISBN-026', 90, True)
        
        library.add_book(book1)
        library.add_book(book2)
        
        found = library.search_by_isbn('ISBN-025')
        assert found == book1
    
            

        books = library.search_by_author('Мария дель Мар Родригес')
        assert len(books) == 1
        
        books = library.search_by_year(2000)
        assert len(books) == 1
        assert book1 in books

    def test_borrow_and_return_books(self):
        library = Library('Библиотека')
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман', CoverType.HARD, 'ISBN-001', 79, False)
        library.add_book(book)

        assert not book.is_borrowed()
        
        success = library.borrow_book_by_title('Эхо террора')
        assert success == True
        assert book.is_borrowed() == True
        
        success = library.borrow_book_by_title('Название')
        assert success == False
        
        book.return_book()
        assert book.is_borrowed() == False
        
        success = library.borrow_book_by_isbn('ISBN-030')
        assert success == False

    def test_remove_book_from_library(self):
        library = Library('Библиотека')
        book = Book('Голос из прошлого', '"Михаил Богданов', 2000, 'Жанр',  CoverType.HARD, 'ISBN-031')
        library.add_book(book)
        
        assert len(library) == 1
        
        success = library.remove_book_by_title('Голос из прошлого')
        assert success == True
        assert len(library) == 0
        
        success = library.remove_book_by_title('Несуществующая')
        assert success == False