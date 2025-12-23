from books import Book
from books_collection import BookCollection
from index_dict import IndexDict


class Library:
    """Класс библиотеки, объединяющий коллекцию книг и индексы для быстрого поиска"""
    
    def __init__(self, name: str):
        """
        Инициализация библиотеки
        Параметры:
        name - название библиотеки
        """
        self.name = name
        # Создаем коллекцию книг для хранения
        self.book_collection = BookCollection(f"Коллекция библиотеки '{name}'")
        # Создаем индексы для быстрого поиска
        self.index = IndexDict()

    def __len__(self):
        """Количество книг в библиотеке"""
        return len(self.book_collection)

    def add_book(self, book: Book) -> None:
        """Добавление книги в библиотеку (в коллекцию и индексы)"""
        if book.isbn in self.index:
            raise ValueError(f"Книга с ISBN {book.isbn} уже существует")
        
        # Добавляем книгу в коллекцию
        self.book_collection.add_book(book)
        # Добавляем книгу в индексы для быстрого поиска
        self.index.add_book(book)

    def borrow_book_by_title(self, title: str) -> bool:
        """Взятие книги по названию"""
        for book in self.book_collection:
            if book.title == title:
                if book.borrow():
                    return True  # Книга успешно взята
                else:
                    return False  # Книга уже взята
            else:
                return False  # Книга с таким названием не найдена
        return False  # Книга не найдена

    def borrow_book_by_isbn(self, isbn: str) -> bool:
        """Взятие книги по ISBN"""
        book = self.index.search_by_isbn(isbn)
        if book:
            # Используем поиск по названию для взятия книги
            return self.borrow_book_by_title(book.title)
        return False  # Книга не найдена

    def remove_book_by_title(self, title: str) -> bool:
        """Удаление книги из библиотеки по названию"""
        for book in self.book_collection:
            if book.title == title:
                # Удаляем книгу из индексов
                self.index.remove_book(book.isbn)
                # Удаляем книгу из коллекции
                self.book_collection.remove_by_title(title)
                return True  # Книга успешно удалена
            return False  # Книга с таким названием не найдена
        return False  # Книга не найдена

    def search_by_isbn(self, isbn: str):
        """Поиск книги по ISBN"""
        result = self.index.search_by_isbn(isbn)
        if result:
            print(f"[Библиотека] Найдена книга по ISBN {isbn}: {result.title}")
        else:
            print(f"[Библиотека] Книга с ISBN {isbn} не найдена")
        return result

    def search_by_title(self, title: str):
        """Поиск книги по названию"""
        result = self.index.search_by_title(title)
        if result:
            print(f"[Библиотека] Найдена книга {title}")
        else:
            print(f"[Библиотека] Книга {title} не найдена")
        return result

    def search_by_author(self, author: str) -> list:
        """Поиск книг по автору"""
        result = self.index.search_by_author(author)
        print(f"[Библиотека] Найдено {len(result)} книг автора '{author}'")
        return result

    def search_by_year(self, year: int) -> list:
        """Поиск книг по году издания"""
        result = self.index.search_by_year(year)
        print(f"[Библиотека] Найдено {len(result)} книг {year} года")
        return result

    def show_all_books(self) -> None:
        """Отображение всех книг в библиотеке"""
        print(f"\n{'='*50}")
        print(f"БИБЛИОТЕКА: {self.name}")
        print(f"{'='*50}")
        # Метод коллекции для отображения книг
        self.book_collection.show_collection()