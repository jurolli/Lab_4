
from books import Book
from books_collection import BookCollection
from index_dict import IndexDict


class Library:

    def __init__(self, name: str):
        self.name = name
        self.book_collection = BookCollection(f"Коллекция библиотеки '{name}'")
        self.index = IndexDict()

    def __len__(self):
        return len(self.book_collection)


    def add_book(self, book: Book) -> None:
        if book.isbn in self.index:
            raise ValueError(f"Книга с ISBN {book.isbn} уже существует")
        self.book_collection.add_book(book)
        self.index.add_book(book)

    def borrow_book_by_title(self, title: str) -> bool:
        for book in self.book_collection:
            if book.title == title:
                if book.borrow():
                    return True
                else:
                    return False
            else:
                return False
            

    def borrow_book_by_isbn(self, isbn: str) -> bool:
        book = self.index.search_by_isbn(isbn)
        if book:
            return self.borrow_book_by_title(book.title)
        return False


    def remove_book_by_title(self, title: str) -> bool:
        for book in self.book_collection:
            if book.title == title:
                self.index.remove_book(book.isbn)
                self.book_collection.remove_by_title(title)
                return True
            return False
        return False


    def search_by_isbn(self, isbn: str):
        result = self.index.search_by_isbn(isbn)
        if result:
            print(f"[Библиотека] Найдена книга по ISBN {isbn}: {result.title}")
        else:
            print(f"[Библиотека] Книга с ISBN {isbn} не найдена")
        return result

    def search_by_title(self, title: str):
        result = self.index.search_by_title(title)
        if result:
            print(f"[Библиотека] Найдена книга {title}")
        else:
            print(f"[Библиотека] Книга {title} не найдена")
        return result


    def search_by_author(self, author: str) -> list:
        result = self.index.search_by_author(author)
        print(f"[Библиотека] Найдено {len(result)} книг автора '{author}'")
        return result
    

    def search_by_year(self, year: int) -> list:
        result = self.index.search_by_year(year)
        print(f"[Библиотека] Найдено {len(result)} книг {year} года")
        return result

    def show_all_books(self) -> None:
        print(f"\n{'='*50}")
        print(f"БИБЛИОТЕКА: {self.name}")
        print(f"{'='*50}")
        self.book_collection.show_collection()