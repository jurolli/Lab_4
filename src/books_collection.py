
from src.books import Book


class BookCollection:

    def __init__(self, name: str):
        self.name = name
        self._books = []

    def __len__(self) -> int:
        return len(self._books)

    def __iter__(self):
        return iter(self._books)

    def __getitem__(self, index: int):
        return self._books[index]
    
    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_by_title(self, title: str) -> bool:
        for i, book in enumerate(self._books):
            if book.title.lower() == title.lower():
                removed_book = self._books.pop(i)
            return True
        return False

    def show_collection(self) -> None:
        print(f"\n=== Коллекция '{self.name}' ({len(self)} книг) ===")
        for i, book in enumerate(self._books):
            print(f"{i}: {book}")

        
       
