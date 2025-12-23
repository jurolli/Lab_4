from src.books import Book, HardCover, SoftCover, GlossyCover
from src.books_collection import BookCollection
from src.library import Library
from src.index_dict import IndexDict
from src.constans import *

class TestBookCollection:
    """Тесты для класса BookCollection (коллекция книг)"""
    
    def test_create_collection(self):
        """Тест создания пустой коллекции книг"""
        collection = BookCollection('Моя коллекция')
        
        # Проверка инициализации имени коллекции
        assert collection.name == 'Моя коллекция'
        
        # Проверка, что коллекция пуста при создании
        assert len(collection) == 0

    def test_add_book_to_collection(self):
        """Тест добавления книги в коллекцию"""
        collection = BookCollection('Коллекция')
        book = Book('Эхо террора', 'Харуки Мия', 1869, 'Роман', CoverType.HARD, 'ISBN-001', 79, False)
        
        # Добавление книги в коллекцию
        collection.add_book(book)
        
        # Проверка, что книга добавлена и коллекция содержит 1 элемент
        assert len(collection) == 1
        
        # Проверка, что книга действительно находится в коллекции
        assert book in collection

    def test_remove_book_from_collection(self):
        """Тест удаления книги из коллекции по названию"""
        collection = BookCollection('Коллекция')
        book = Book('Дневник последнего алхимика', 'Чжан Ли', 2000, 'Жанр', CoverType.HARD, 'ISBN-024', 46)
        
        # Добавление книги в коллекцию
        collection.add_book(book)
        assert len(collection) == 1
    
        # Удаление существующей книги по названию
        result = collection.remove_by_title('Дневник последнего алхимика')
        assert result == True  # Должен вернуть True при успешном удалении
        
        # Проверка, что коллекция теперь пуста
        assert len(collection) == 0
        
        # Попытка удаления несуществующей книги
        result = collection.remove_by_title('Несуществующая')
        assert result == False  # Должен вернуть False, так как книга не найдена

    def test_collection_iteration(self):
        """Тест итерации по коллекции книг"""
        collection = BookCollection('Коллекция')
        
        # Создание тестовых книг
        book1 = Book('Записки провинциального врача', 'Мария дель Мар Родригес', 2000, 'Жанр', CoverType.HARD,'ISBN-025')
        book2 = Book('Химия эмоций', 'Ана Мария Дуарте', 2010, 'Жанр', CoverType.HARD, 'ISBN-026', 36)
        
        # Добавление книг в коллекцию
        collection.add_book(book1)
        collection.add_book(book2)
        
        # Преобразование коллекции в список
        books = list(collection)
        
        # Проверка, что список содержит 2 книги
        assert len(books) == 2
        
        # Проверка, что обе книги присутствуют в списке
        assert book1 in books
        assert book2 in books