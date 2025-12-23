from typing import Optional
import random
from books import Book, GlossyCover, HardCover, SoftCover
from books_collection import BookCollection
from index_dict import IndexDict
from library import Library
from constans import *
    
def str_validation(s:str) -> bool:
    """
    Проверка строковых аргументов на корректность
    Параметры:
    s - строка для проверки
    Возвращает:
    bool - True если строка корректна, False если есть ошибки
    """
    if s == "":
        print("Ошибка: поле не может быть пустым")
        return False
    for symbol in range(len(s)):
        if s[symbol] in ['@', '#', '$', '%', '^', '&', '*', '=', '+', '<', '>', '/', '\\', '|', '~', '`']:
            return False
    if not s[0].isupper():
        print("Ошибка: должно начинаться с большой буквы")
        return False
    else:
        return True

# принты

def print_commands():
    """Вывод списка возможных команд"""
    print("\nСИСТЕМА УПРАВЛЕНИЯ БИБЛИОТЕКОЙ\n")
    print("1. Добавить книгу (по типу обложки)")
    print("2. Взять книгу")
    print("3. Вернуть книгу")
    print("4. Нанести урон книге")
    print("5. Найти книгу по ISBN")
    print("6. Найти книги по автору")
    print("7. Найти книги по жанру")
    print("8. Найти книги по году")
    print("9. Проверить состояние всех книг")
    print("10. Удалить книгу")
    print("0. Выход")


def print_type_cover():
    """Вывод доступных типов обложки"""
    print("\nВыберите тип обложки\n")
    print("1. твёрдая")
    print("2. мягкая")
    print("3. глянцевая(журнальная)")

# инпуты

def input_title() -> str:
    """Ввод названия книги"""
    print(f"\nВведите название книги:")
    while True:
        title = input(f"Название книги (с заглавной буквы): ").strip()
        if str_validation(title) == True:  # Если строка прошла проверку, возвращаем её
            return title


def input_author() -> str:
    """Ввод автора книги"""
    print(f"\nВведите автора книги:")
    while True:
        author = input("Автор книги (с заглавной буквы): ").strip()
        if str_validation(author) == True:
            return author


def input_year() -> int:
    """Ввод года издания"""
    print(f"\nВведите год издания книги:")
    while True:
        year = input("Год издания: ").strip()
        if year == "":
            print("Ошибка: год не может быть пустым")
            continue
        if year.isdigit() == False:
            print("Ошибка: год должен быть числом")
            continue
        try:
            return int(year)
        except ValueError:
            print("Ошибка: некорректное число")


def input_genre() -> str:
    """Ввод жанра книги"""
    print(f"\nВведите жанр книги:")
    print(f"Возможно вы искали: {', '.join(GENRES)}")
    while True:
        genre = input("Жанр книги (с заглавной буквы): ").strip()
        for symbol in range(len(genre)):
            if genre[symbol].isdigit() == True:
                print("Ошибка: жанр не может содержать цифры")
                return False
        if str_validation(genre) == True:
            return genre


def input_cover_type() -> str:
    """Ввод типа обложки """
    print(f"\nВведите тип обложки:")
    print(f"Варианты:\n 1. Твёрдая\n 2. Мягкая\n 3. Глянцевая\n")
    while True:
        cover_type = input("Ваш ввод (слово): ").strip()
        if cover_type != 'Мягкая' and cover_type != 'Твёрдая' and cover_type != 'Глянцевая':
            print("Ошибка: тип обложки должен быть выбран из предложенных'")
            continue
        return cover_type


def input_condition() -> int:
    """Ввод состояния книги (0-100)"""
    print(f"\nВведите состояние книги(в процентах без знака '%'): ")
    while True:
        condition = input("Cостояние книги: ").strip()
        if condition == "":
            print("Ошибка: состояние не может быть пустым")
            continue
        for symbol in condition:
            if symbol.isdigit() == False:
                print("Ошибка: состояние должно быть числом")
            continue
        return int(condition)


def input_has_images() -> bool:
    """Ввод информации о наличии изображений в книге"""
    images = input('\nЕсть ли в книге изображения? (y/n) или (да/нет): ')
    while True:
        if images == 'y' or 'yes' or 'да':
            has_images = True
            return has_images
        elif images == 'n' or 'no' or 'нет':
            has_images = False    
            return has_images
        else:
            print('Ошибка: ответ может быть только (y/n)')
            continue

# команды

def add_book(library: Library) -> None:
    """Добавление новой книги в библиотеку"""
    title = input_title()
    author = input_author()
    year = input_year()
    genre = input_genre()
    cover_type = input_cover_type()
    isbn = input("Введите ISBN (формат: ISBN-001): ").strip()
    condition = input_condition()
    has_images = input_has_images()

    if isbn in library.index:
        print(f"\nОшибка: книга с ISBN '{isbn}' уже существует в библиотеке\n")
        return

    if cover_type == 'Твёрдая':
        cover_type = CoverType.HARD
        book = HardCover(title, author, year, genre, isbn, condition, has_images)

    if cover_type == 'Мягкая':
        cover_type = CoverType.SOFT
        book = SoftCover(title, author, year, genre, isbn, condition, has_images)

    if cover_type == 'Глянцевая':
        cover_type = CoverType.GLOSSY
        book = GlossyCover(title, author, year, genre, isbn, condition, has_images)

    else:
        print("\nНеверный выбор!")
        return
    library.add_book(book)
    print(f"\nКнига добавлена: {book}")


def borrow_book(library: Library) -> None:
    """Взятие книги"""
    if len(library.book_collection) == 0:
        print("\nБиблиотека пуста!")
        return 
    print("\nПоиск книги для выдачи:")
    print("1. По названию")
    print("2. По ISBN")
    choice = input("Выберите способ поиска (1 или 2): ").strip()

    if choice == '1':
        title = input("Введите название книги: ").strip()
        success = library.borrow_book_by_title(title)
        
        if success:
            book = library.search_by_title(title)
            if book:
                if isinstance(book, HardCover):
                    damage = random.randint(0, 5)
                    book.damage(damage)
                    print(f"Нанесен урон: {damage}%")
                elif isinstance(book, SoftCover):
                    damage = random.randint(3, 7)
                    book.damage(damage)
                    print(f"Нанесен урон: {damage}%")
                elif isinstance(book, GlossyCover):
                    scratches = random.randint(0, 5)
                    damage = random.randint(3, 10)
                    book.add_scratches(scratches)
                    book.damage(damage)
                    print(f"Добавлено царапин: {scratches}, нанесен урон: {damage}%")
    
    elif choice == '2':
        isbn = input("Введите ISBN книги: ").strip()
        success = library.borrow_book_by_isbn(isbn)
        if success:
            book = library.search_by_isbn(isbn)
            if book:
                if isinstance(book, HardCover):
                    damage = random.randint(0, 5)
                    book.damage(damage)
                    print(f"Нанесен урон: {damage}%")
                elif isinstance(book, SoftCover):
                    damage = random.randint(3, 7)
                    book.damage(damage)
                    print(f"Нанесен урон: {damage}%")
                elif isinstance(book, GlossyCover):
                    scratches = random.randint(0, 5)
                    damage = random.randint(3, 10)
                    book.add_scratches(scratches)
                    book.damage(damage)
                    print(f"Добавлено царапин: {scratches}, нанесен урон: {damage}%")
    else:
        print("\nНеверный выбор!")
       

def return_book(library: Library) -> None:
    """Возврат взятой книги"""
    title = input_title("Введите название или позже ISBN: ").strip()
    isbn = input("Введите ISBN: ").strip()

    if len(library.book_collection) != 0:
        borrowed_books = []
        for b in library:
            if b.is_borrowed:
                borrowed_books.append(b)
        if borrowed_books:
            if title is None:
                book = library.search_by_isbn(isbn)
            else:
                book = library.search_by_title(title)
                book.return_book()
                print(f"Книга возвращена: {book.title}")
        else:
            print('\nНет взятых книг для возврата')
    else:
        print('\nНет книг в библиотеке')


def damage_book(library: Library)  -> None:
    """Нанесение урона книге"""
    if len(library) != 0:
        book = input_title("введите название: ").strip()
        print(f"Наносим повреждение: {book.title}\n")
                
        if isinstance(book, HardCover):
            damage = random.randint(5, 15)
            book.damage(damage)
            print(f"  Прочность снижена на {damage}%. Текущая: {book.get_condition()}%\n")
                    
        elif isinstance(book, SoftCover):
            damage = random.randint(10, 25)
            book.damage(damage)
            print(f"   Прочность снижена на {damage}%. Текущий: {book.get_condition()}%\n")  
    
        elif isinstance(book, GlossyCover):
            scratches = random.randint(1, 5)
            book.add_scratches(scratches)
            damage = random.randint(8, 18)
            book.damage(damage)
            print(f"  Добавлено царапин: {scratches}.\nОбщая прочность {book.get_condition()}\n")              
        else:
            print('Нет книг для повреждения')

    else:
        print('\nНет книг в библиотеке')


def search_by_isbn(library: Library) -> None:
    """Поиск книги по ISBN"""
    isbn = input("Введите ISBN: ").strip()
    book = library.search_by_isbn(isbn)

    if book is None:
        print(f"Книга с ISBN '{isbn}' не найдена!")
    else:
        print(f"Найдена книга: {book.title}")
        print(f"Автор: {book.author}")
        print(f"Год: {book.year}")
        print(f"Жанр: {book.genre}")
        print(f"Тип обложки: {book.cover_type}")
        print(f"Состояние: {book.condition}")


def search_by_author(library: Library) -> None:
    """Поиск книг по автору"""
    if len(library.book_collection) != 0:
        found_books = []
        search_author = input("Введите имя Автора: ").strip()
        book = library.search_by_author(search_author)
        for book in library.book_collection:
            if book.author == search_author:
                found_books.append(book)
        print(f"  Найдено: {len(found_books)} книг")
        for book in found_books: 
            print(f"    - {book}")
    else:
        print('\nБиблиотека пуста, поиск невозможен')


def search_by_year(library: Library) -> None:
    """Поиск книг по году издания"""
    if len(library.book_collection) != 0:
        found_books = []
        search_year = input("Введите год издания: ").strip()
        print(f" Поиск книг {search_year} года")
        for book in library.book_collection:
            if book.year == search_year:
                found_books.append(book)
            print(f"  Найдено: {len(found_books)} книг")
            for book in found_books: 
                print(f"    - {book}")
        else:
            print('Библиотека пуста, поиск невозможен')


def search_by_genre(library: Library) -> None:
    """Поиск книг по жанру"""
    if len(library.book_collection) != 0:
        found_books = []
        search_genre =input("Введите жанр: ").strip()
        print(f"Поиск книг с жанром: {search_genre}")
        for book in library.book_collection:
            if book.genre == search_genre:
                found_books.append(book)
        print(f"  Найдено: {len(found_books)} книг")
        for book in found_books: 
            print(f"    - {book}")
    else:
        print('Библиотека пуста, поиск невозможен')


def check_condition(library: Library) -> None:
    """Проверка состояния всех книг в библиотеке"""
    if len(library.book_collection) != 0:
        print(f"Проверка состояния книг:")
        for book in library.book_collection:
            condition = book.get_condition()
            print(f"  {book.title}: {condition}")        
    else:
         print('Нет книг для проверки состояния')
                

def remove_book(library: Library) -> None:
    """Удаление книги из библиотеки"""
    if len(library.book_collection) != 0:
        title = input_title("введите название: ").strip()
        book = library.search_by_title(title)
        print(f"[Удаляем книгу: {book.title}")
        success = library.remove_book_by_title(book.title)
        if success:
            print(f"Книга '{title}' успешно удалена!")
        else:
            print(f"Не удалось удалить книгу '{title}'!")
    else:
        print('[Нет книг для удаления')


def main() -> None:
    """Главная функция - основной цикл программы"""
    library = Library('Мvv')
    while True:
        print_commands()
        choice = input("Выберите действие (0-10): ").strip()

        if choice == '1':
            add_book(library)
        elif choice == '2':
            borrow_book(library)
        elif choice == '3':
            return_book(library)
        elif choice == '4':
            damage_book(library)
        elif choice == '5':
            search_by_isbn(library)
        elif choice == '6':
            search_by_author(library)
        elif choice == '7':
            search_by_genre(library)
        elif choice == '8':
            search_by_year(library)
        elif choice == '9':
            check_condition(library)
        elif choice == '10':
            remove_book(library)
        elif choice == "0":
            print("\nДо свидания!")
            break
        else:
            print("Неверный выбор! Попробуйте снова.")


if __name__ == "__main__":
    main()
