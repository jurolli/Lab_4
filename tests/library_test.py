from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *
import pytest

class TestLibrary:
    """Тесты для класса Library (библиотека)"""
    
    def test_create_library(self):
        """Тест создания библиотеки"""
        library = Library('Тестовая библиотека')
        
        # Проверка корректности инициализации имени библиотеки
        assert library.name == 'Тестовая библиотека'
        
        # Проверка, что библиотека пуста при создании
        assert len(library) == 0

    def test_add_book_to_library(self):
        """Тест добавления книги в библиотеку"""
        library = Library('Библиотека')
        book =  Book('Дневник алхимика', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        
        # Добавление книги в библиотеку
        library.add_book(book)
        
        # Проверка, что книга добавлена
        assert len(library) == 1
        
        # Попытка добавить книгу с уже существующим ISBN
        book2 =  Book('Дневник последнего cтоматолога', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        
        # Должно возникнуть исключение, так как ISBN уже существует
        with pytest.raises(ValueError):
            library.add_book(book2)

    def test_search_books(self):
        """Тест поиска книг в библиотеке по различным критериям"""
        library = Library('Библиотека')
        
        # Создание тестовых книг
        book1 = Book('Записки провинциального врача', 'Мария дель Мар Родригес', 2000, 'Жанр', CoverType.HARD,'ISBN-025', 69, True)
        book2 = Book('О чём молчат родители', 'Мария дель Мар Родригесе', 2010, 'Жанр', CoverType.HARD, 'ISBN-026', 90, True)
        
        # Добавление книг в библиотеку
        library.add_book(book1)
        library.add_book(book2)
        
        # Поиск книги по ISBN
        found = library.search_by_isbn('ISBN-025')
        assert found == book1  # Должна быть найдена книга с ISBN-025
    
        # Поиск книг по автору
        books = library.search_by_author('Мария дель Мар Родригес')
        assert len(books) == 1  # Должна быть найдена 1 книга этого автора
        
        # Поиск книг по году издания
        books = library.search_by_year(2000)
        assert len(books) == 1  # Должна быть найдена 1 книга 2000 года
        assert book1 in books  # Найденная книга должна быть book1

    def test_borrow_and_return_books(self):
        """Тест взятия и возврата книг"""
        library = Library('Библиотека')
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман', CoverType.HARD, 'ISBN-001', 79, False)
        
        # Добавление книги в библиотеку
        library.add_book(book)

        # Проверка начального состояния (книга не взята)
        assert not book.is_borrowed()
        
        # Взятие существующей книги по названию
        success = library.borrow_book_by_title('Эхо террора')
        assert success == True  # Успешное взятие
        assert book.is_borrowed() == True  # Книга теперь должна быть взята
        
        # Попытка взять несуществующую книгу
        success = library.borrow_book_by_title('Название')
        assert success == False  # Неудачная попытка
        
        # Возврат книги
        book.return_book()
        assert book.is_borrowed() == False  # Книга должна быть возвращена
        
        # Попытка взять книгу по несуществующему ISBN
        success = library.borrow_book_by_isbn('ISBN-030')
        assert success == False  # Неудачная попытка

    def test_remove_book_from_library(self):
        """Тест удаления книги из библиотеки"""
        library = Library('Библиотека')
        book = Book('Голос из прошлого', '"Михаил Богданов', 2000, 'Жанр',  CoverType.HARD, 'ISBN-031')
        
        # Добавление книги в библиотеку
        library.add_book(book)
        assert len(library) == 1  # Проверка, что книга добавлена
        
        # Удаление существующей книги по названию
        success = library.remove_book_by_title('Голос из прошлого')
        assert success == True  # Успешное удаление
        assert len(library) == 0  # Библиотека должна быть пуста
        
        # Попытка удалить несуществующую книгу
        success = library.remove_book_by_title('Несуществующая')
        assert success == False  # Неудачная попытка