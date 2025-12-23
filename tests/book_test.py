from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *

import pytest


class TestBook:
    """Тесты для класса Book"""
    
    def test_create_valid_book(self):
        """Тест создания валидного объекта Book"""
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман', CoverType.HARD, 'ISBN-001', 79, False)
        # Проверка корректности инициализации всех атрибутов
        assert book.title == 'Эхо террора'
        assert book.author == 'Харуки Мия'
        assert book.year == 1869
        assert book.genre == 'Роман'
        assert book.isbn == 'ISBN-001'
        assert book.condition == 79
        assert not book.has_images
        assert not book.is_borrowed()  # Книга не должна быть взята при создании

    def test_book_creation_with_defaults(self):
        """Тест создания книги со значениями по умолчанию"""
        book = Book('Название', 'Автор', 2000, 'Роман', CoverType.HARD, 'ISBN-002')
        # Проверка значений по умолчанию
        assert book.condition == 100  # Состояние по умолчанию должно быть 100%
        assert not book.has_images  # По умолчанию без изображений

    def test_book_title_validation(self):
        """Тест валидации названия книги"""
        book = Book('1984', 'Джордж Оруэлл', 1949, 'Антиутопия', CoverType.SOFT, 'ISBN-003')
        assert book.title == '1984'
        # Проверка на пустое название
        with pytest.raises(ValueError):
            Book('', 'Автор', 2000, 'Жанр', CoverType.SOFT, 'ISBN-004')

    def test_book_author_validation(self):
        """Тест валидации автора книги"""
        # Проверка на пустого автора
        with pytest.raises(ValueError):
            Book('Название', '', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-005')

    def test_book_genre_validation(self):
        """Тест валидации жанра книги"""
        # Проверка на пустой жанр
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000,'', CoverType.HARD, 'ISBN-008')

    def test_book_isbn_validation(self):
        """Тест валидации ISBN"""
        # Проверка на пустые ISBN и состояние
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр', '', '')

    def test_book_condition_validation(self):
        """Тест валидации состояния книги"""
        # Проверка на состояние больше 100
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-009', 150)
        
        # Проверка на отрицательное состояние
        with pytest.raises(ValueError):
            Book('Название', 'Автор', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-010', -10)

    def test_book_borrow_and_return(self):
        """Тест взятия и возврата книги"""
        book = Book('Название', 'Автор', 2000, 'Жанр', CoverType.SOFT, 'ISBN-011')
        
        # Проверка начального состояния
        assert not book.is_borrowed()
        
        # Взятие книги
        assert book.borrow() == True
        assert book.is_borrowed() == True
        
        # Попытка повторного взятия (должна вернуть False)
        assert book.borrow() == False
        assert book.is_borrowed() == True
        
        # Возврат книги
        book.return_book()
        assert not book.is_borrowed()
        
        # Повторное взятие после возврата
        assert book.borrow() == True

    def test_book_damage(self):
        """Тест нанесения урона книге"""
        book = Book('Название', 'Автор', 2000, 'Жанр', CoverType.SOFT, 'ISBN-012', 100)
        
        # Нанесение урона 20%
        book.damage(20)
        assert book.condition == 80
        
        # Нанесение урона 30%
        book.damage(30)
        assert book.condition == 50
        
        # Нанесение урона больше, чем текущее состояние
        book.damage(60)
        assert book.condition == 0  # Состояние не должно быть отрицательным

    def test_book_equality(self):
        """Тест сравнения книг (по ISBN)"""
        book1 = Book('Название1', 'Автор1', 2000, 'Жанр', CoverType.GLOSSY, 'ISBN-013', 70)
        book2 = Book('Название2', 'Автор2', 2010, 'Жанр', CoverType.GLOSSY, 'ISBN-013', 70)
        book3 = Book('Название3', 'Автор3', 2020, 'Жанр', CoverType.GLOSSY, 'ISBN-014', 80)
        
        # Книги с одинаковым ISBN должны быть равны
        assert book1 == book2  
        # Книги с разным ISBN должны быть разными
        assert book1 != book3  

    def test_book_repr(self):
        """Тест строкового представления книги"""
        book = Book('Война и мир', 'Толстой', 1869, 'Роман', CoverType.SOFT, 'ISBN-015')
        repr_str = repr(book)
        
        # Проверка, что важная информация присутствует в строковом представлении
        assert 'Война и мир' in repr_str
        assert 'Толстой' in repr_str
        assert 'ISBN-015' in repr_str