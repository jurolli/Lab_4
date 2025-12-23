from books import Book

class IndexDict:
    """Класс для индексации книг по различным критериям"""
    
    def __init__(self):
        # Инициализация индексов для разных типов поиска
        self._isbn_index = {}   # Индекс по ISBN (ISBN -> Book)
        self._title_index = {}  # Индекс по названию (title -> list[Book])
        self._author_index = {} # Индекс по автору (author -> list[Book])
        self._year_index = {}   # Индекс по году (year -> list[Book])
        self._all_books = []    # Список всех книг

    def __len__(self) -> int:
        """Общее количество книг в коллекции"""
        return len(self._all_books)

    def __iter__(self):
        """Итератор по всем книгам"""
        return iter(self._all_books)

    def __getitem__(self, key):
        """
        Обращение к книгам по различным ключам
        Поддерживаемые ключи:
        - str: поиск по ISBN или автору
        - int: поиск по году
        Возвращает:
        - Для ISBN: Book
        - Для автора: список книг автора
        - Для года: список книг этого года
        """
        if isinstance(key, str):
            # Проверяем, ISBN это или имя автора
            if key in self._isbn_index:
                return self._isbn_index[key]  # Возвращаем книгу по ISBN
            elif key in self._author_index:
                return self._author_index[key] # Возвращаем список книг автора
            else:
                raise KeyError(f"Не найден ISBN или автор: {key}")
        elif isinstance(key, int):
            if key in self._year_index:
                return self._year_index[key]  # Возвращаем список книг года
            else:
                return []  # Возвращаем пустой список если год не найден
        else:
            raise KeyError(f"Неподдерживаемый тип ключа: {type(key)}")

    def add_to_isbn_index(self, book: Book) -> None:
        """Добавление книги в индекс по ISBN"""
        if book.isbn in self._isbn_index:
            raise ValueError(f"Книга с ISBN {book.isbn} уже существует в индексе")
        self._isbn_index[book.isbn] = book

    def add_to_author_index(self, book: Book) -> None:
        """Добавление книги в индекс по автору"""
        if book.author not in self._author_index:
            self._author_index[book.author] = []
        self._author_index[book.author].append(book)

    def add_to_title_index(self, book: Book) -> None:
        """Добавление книги в индекс по названию"""
        if book.title not in self._title_index:
            self._title_index[book.title] = []
        self._title_index[book.title].append(book)

    def add_to_year_index(self, book: Book) -> None:
        """Добавление книги в индекс по году"""
        if book.year not in self._year_index:
            self._year_index[book.year] = []
        self._year_index[book.year].append(book)

    def add_book(self, book: Book) -> None:
        """Добавление книги во все индексы и общий список"""
        if book in self._all_books:
            raise ValueError("Книга уже есть в коллекции")
        
        try:
            # Добавляем книгу во все индексы
            self.add_to_isbn_index(book)
            self.add_to_author_index(book)
            self.add_to_year_index(book)
            self.add_to_title_index(book)
            
            # Добавляем книгу в общий список
            self._all_books.append(book)
            
            print(f"    Книга '{book.title}' добавлена в индексы")
        except ValueError:
            print(f"[Индексы] Ошибка при добавлении")

    def remove_from_isbn_index(self, isbn: str) -> None:
        """Удаление книги из индекса по ISBN"""
        if isbn in self._isbn_index:
            del self._isbn_index[isbn]

    def remove_from_author_index(self, book: Book) -> None:
        """Удаление книги из индекса по автору"""
        if book.author in self._author_index:
            self._author_index[book.author].remove(book)
           
            # Если у автора больше нет книг, удаляем автора из индекса
            if not self._author_index[book.author]:
                del self._author_index[book.author]

    def remove_from_year_index(self, book: Book) -> None:
        """Удаление книги из индекса по году"""
        if book.year in self._year_index:
            self._year_index[book.year].remove(book)
            # Если в этом году больше нет книг, удаляем год из индекса
            if not self._year_index[book.year]:
                del self._year_index[book.year]

    def remove_book(self, isbn: str) -> bool:
        """Удаление книги из всех индексов по ISBN"""
        if isbn not in self._isbn_index:
            print(f"    Книга с ISBN {isbn} не найдена")
            return False
        
        # Получаем книгу по ISBN
        book = self._isbn_index[isbn]
        
        # Удаляем книгу из всех индексов
        self.remove_from_isbn_index(isbn)
        self.remove_from_author_index(book)
        self.remove_from_year_index(book)
        
        # Удаляем книгу из общего списка
        self._all_books.remove(book)
        
        print(f"    Книга '{book.title}' удалена из индексов")
        return True

    def search_by_isbn(self, isbn: str):
        """Поиск книги по ISBN"""
        return self._isbn_index.get(isbn)

    def search_by_title(self, title: str):
        """Поиск книг по названию"""
        return self._title_index.get(title)
    
    def search_by_author(self, author: str) -> list:
        """Поиск книг по автору"""
        return self._author_index.get(author, [])
    
    def search_by_year(self, year: int) -> list:
        """Поиск книг по году издания"""
        return self._year_index.get(year, [])