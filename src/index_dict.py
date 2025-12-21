
from src.books import Book

class IndexDict:

    def __init__(self):
        self._isbn_index = {}  
        self._title_index = {}  
        self._author_index = {}    
        self._year_index = {} 
        self._genre_index = {}
        self._all_books = []


    def __len__(self) -> int:
        return len(self._all_books)


    def __iter__(self):
        return iter(self._all_books)


    def __getitem__(self, key):
        if isinstance(key, str):
            # Проверяем, ISBN это или имя автора
            if key in self._isbn_index:
                return self._isbn_index[key]  
            elif key in self._author_index:
                return self._author_index[key] 
            else:
                raise KeyError(f"Не найден ISBN или автор: {key}")
        elif isinstance(key, int):
            if key in self._year_index:
                return self._year_index[key]
            else:
                return []
        else:
            raise KeyError(f"Неподдерживаемый тип ключа: {type(key)}")

    
    def add_to_isbn_index(self, book: Book) -> None:
        if book.isbn in self._isbn_index:
            raise ValueError(f"Книга с ISBN {book.isbn} уже существует в индексе")
        self._isbn_index[book.isbn] = book


    def add_to_author_index(self, book: Book) -> None:
        if book.author not in self._author_index:
            self._author_index[book.author] = []
        self._author_index[book.author].append(book)

    def add_to_title_index(self, book: Book) -> None:
        if book.title not in self._title_index:
            self._title_index[book.title] = []
        self._title_index[book.title].append(book)
    

    def add_to_year_index(self, book: Book) -> None:
        if book.year not in self._year_index:
            self._year_index[book.year] = []
        self._year_index[book.year].append(book)

    def add_book(self, book: Book) -> None:
        if book in self._all_books:
            raise ValueError("Книга уже есть в коллекции")
        
        try:
            self.add_to_isbn_index(book)
            self.add_to_author_index(book)
            self.add_to_year_index(book)
            self.add_to_title_index(book)
            self._all_books.append(book)
            print(f"Книга '{book.title}' добавлена в индексы")
        except ValueError:
            print(f"[Индексы] Ошибка при добавлении")

            
    
    def remove_from_isbn_index(self, isbn: str) -> None:
        if isbn in self._isbn_index:
            del self._isbn_index[isbn]
    

    def remove_from_author_index(self, book: Book) -> None:
        if book.author in self._author_index:
            self._author_index[book.author].remove(book)
           
            if not self._author_index[book.author]:
                del self._author_index[book.author]
    

    def remove_from_year_index(self, book: Book) -> None:
        if book.year in self._year_index:
            self._year_index[book.year].remove(book)
            if not self._year_index[book.year]:
                del self._year_index[book.year]
    

    def remove_book(self, isbn: str) -> bool:
        if isbn not in self._isbn_index:
            print(f"Книга с ISBN {isbn} не найдена")
            return False
        
        book = self._isbn_index[isbn]
        self.remove_from_isbn_index(isbn)
        self.remove_from_author_index(book)
        self.remove_from_year_index(book)
        self._all_books.remove(book)
        
        print(f"Книга '{book.title}' удалена из индексов")
        return True

    

    def search_by_isbn(self, isbn: str):
        return self._isbn_index.get(isbn)

    def search_by_title(self, title: str):
        return self._title_index.get(title)
    
    def search_by_author(self, author: str) -> list:
        return self._author_index.get(author, [])
    
    def search_by_year(self, year: int) -> list:
        return self._year_index.get(year, [])
    