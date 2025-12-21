
from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *

import pytest


class TestBook:
    
    def test_create_valid_book(self):
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман',CoverType.HARD,'ISBN-001', 79, False)
        assert book.title == 'Эхо террора'
        assert book.author == 'Харуки Мия'
        assert book.year == 1869
        assert book.genre == 'Роман'
        assert book.isbn == 'ISBN-001'
        assert book.condition == 79
        assert not book.has_images
        assert not book.is_borrowed()

    def test_book_creation_with_defaults(self):
        book = Book('Название', 'Автор', 2000, 'Роман',CoverType.HARD, 'ISBN-002')
        assert book.condition == 100 
        assert not book.has_images

    def test_book_title_validation(self):
        book = Book('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', CoverType.SOFT, 'ISBN-003')
        assert book.title == '1984'
        with pytest.raises(ValueError):
            Book('', 'Автор', 2000, 'Жанр', CoverType.SOFT, 'ISBN-004')

    def test_book_author_validation(self):
        with pytest.raises(ValueError):
            Book('Название', '', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-005')


    def test_book_genre_validation(self):
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000,'', CoverType.HARD, 'ISBN-008')

    def test_book_isbn_validation(self):
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр', '', '')

    def test_book_condition_validation(self):
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-009', 150)
        
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр',   CoverType.GLOSSY, 'ISBN-010', -10)

    def test_book_borrow_and_return(self):
        book = Book('Название', 'Автор', 2000, 'Жанр',  CoverType.SOFT, 'ISBN-011')
        
        assert not book.is_borrowed()
        
        assert book.borrow() == True
        assert book.is_borrowed() == True
        
        assert book.borrow() == False
        assert book.is_borrowed() == True
        
        book.return_book()
        assert not book.is_borrowed()
        
        assert book.borrow() == True

    def test_book_damage(self):
        book = Book('Название', 'Автор', 2000, 'Жанр',  CoverType.SOFT, 'ISBN-012', 100)
        
        book.damage(20)
        assert book.condition == 80
        
        book.damage(30)
        assert book.condition == 50
        
        book.damage(60)
        assert book.condition == 0 

    def test_book_equality(self):
        book1 = Book('Название1', 'Автор1', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-013', 70)
        book2 = Book('Название2', 'Автор2', 2010, 'Жанр', CoverType.GLOSSY, 'ISBN-013', 70)
        book3 = Book('Название3', 'Автор3', 2020, 'Жанр', CoverType.GLOSSY, 'ISBN-014', 80)
        
        assert book1 == book2  
        assert book1 != book3  

    def test_book_repr(self):
        book = Book('Война и мир', 'Толстой', 1869, 'Роман', CoverType.SOFT, 'ISBN-015')
        repr_str = repr(book)
        
        assert 'Война и мир' in repr_str
        assert 'Толстой' in repr_str
        assert 'ISBN-015' in repr_str