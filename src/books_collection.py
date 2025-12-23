from books import Book  

class BookCollection:
    """Класс для управления коллекцией книг"""
    
    def __init__(self, name: str):
        """
        Конструктор класса BookCollection
        Параметры:
        name - название коллекции
        """
        self.name = name
        self._books = []  # Приватный список для хранения книг

    def __len__(self) -> int:
        """Количество книг в коллекции"""
        return len(self._books)

    def __iter__(self):
        """Итерация по коллекции книг"""
        return iter(self._books)

    def __getitem__(self, index: int):
        """Доступ к книге по индексу"""
        return self._books[index]
    
    def add_book(self, book: Book) -> None:
        """
        Добавление книги в коллекцию
        Параметры:
        book - объект класса Book для добавления
        """
        self._books.append(book)

    def remove_by_title(self, title: str) -> bool:
        """
        Удаление книги из коллекции по названию
        Параметры:
        title - название книги для удаления
        Возвращает:
        bool - True если книга была удалена, False если не найдена
        """
        for i, book in enumerate(self._books):
            if book.title.lower() == title.lower():
                removed_book = self._books.pop(i)  # Удаляем книгу по индексу
                return True
        return False  # Книга не найдена

    def show_collection(self) -> None:
        """Отображение всей коллекции книг в консоли"""
        print(f"\n=== Коллекция '{self.name}' ({len(self)} книг) ===")
        for i, book in enumerate(self._books):
            print(f"{i}: {book}")  # Используется строковое представление книги