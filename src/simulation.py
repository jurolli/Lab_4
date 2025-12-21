from typing import Optional
import random
from books import Book, GlossyCover, HardCover, SoftCover
from books_collection import BookCollection
from index_dict import IndexDict
from library import Library
from constans import *


def run_simulation(steps: int = 40, seed: Optional[int] = None) -> None:

    print(f"\n{'='*60}")
    print(f"СИМУЛЯЦИЯ БИБЛИОТЕКИ")
    print(f"{'='*60}")
    
    if seed is not None:
        random.seed(seed)
        print(f"[Симуляция] Seed установлен: {seed}")
    
    library = Library('Библиотека')
    added_books_history = []
   
    
    for step in range(1, steps + 1):
        print(f"\n-- Шаг {step}/{steps} --")
        event = random.choice(SIMULATION_EVENTS)
        print(f"Событие: {event}")
        

        if event == 'add_hardcover':
            title = random.choice(TITLES)
            author = random.choice(AUTHORS)
            year = random.randint(1900, 2026)
            genre = random.choice(GENRES)
            isbn = f"HC-{step:04d}-{random.randint(1000,9999)}"
            condition = random.randint(30, 100)
            has_images = random.choice([True, False])

            book = HardCover(title, author, year, genre,  isbn, condition, has_images)
            library.add_book(book)
            added_books_history.append(book)


        elif event == 'add_softcover':
            title = random.choice(TITLES)
            author = random.choice(AUTHORS)
            year = random.randint(1990, 2026)
            genre = random.choice(GENRES)
            isbn = f"SC-{step:04d}-{random.randint(1000,9999)}"
            condition = random.randint(30, 100)
            has_images = random.choice([True, False])
            
            book = SoftCover(title, author, year, genre, isbn, condition, has_images)
            library.add_book(book)
            added_books_history.append(book)
            

        elif event == 'add_glossycover':
            title = random.choice(TITLES)
            author = 'Редакция журнала'
            year = random.randint(2000, 2026)
            genre = random.choice(['Журнал', 'Альбом', 'Каталог'])
            isbn = f"GC-{step:04d}-{random.randint(1000,9999)}"
            condition = random.randint(30, 100)
            has_images = random.choice([True, False])
           
            book = GlossyCover(title, author, year, genre, isbn, condition, has_images)
            library.add_book(book)

            added_books_history.append(book)
            

        elif event == 'borrow_book':
            if added_books_history:
                book = random.choice(added_books_history)
                print(f"[Симуляция] Пытаемся взять книгу: {book.title}\n")
                if book.borrow():
                    print(f"Книга взята. Всего взятий: {book.borrow_count()}\n")

                    if isinstance(book, HardCover):
                        book.damage(random.randint(0, 5))
                    elif isinstance(book, SoftCover):
                        book.damage(random.randint(3, 7))
                    elif isinstance(book, GlossyCover):
                        book.add_scratches(random.randint(0, 5))
                        book.damage(random.randint(3, 10))
                else:
                    print('Книга уже взята')
            else:
                print('[Симуляция] Нет книг для взятия')


        elif event == 'return_book':
            if added_books_history:
                borrowed_books = []
                for b in added_books_history:
                    if b.is_borrowed:
                        borrowed_books.append(b)
                if borrowed_books:
                    book = random.choice(borrowed_books)
                    book.return_book()
                    print(f"[Симуляция] Книга возвращена: {book.title}")
                else:
                    print('[Симуляция] Нет взятых книг для возврата')
            else:
                print('[Симуляция] Нет книг в библиотеке')



        elif event == 'damage_book':
            if added_books_history:
                book = random.choice(added_books_history)
                print(f"[Симуляция] Наносим повреждение: {book.title}\n")
                
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
                print('[Симуляция] Нет книг для повреждения')


              
        elif event == 'search_by_cover_type':
            cover_types = [CoverType.HARD, CoverType.SOFT, CoverType.GLOSSY]
            search_type = random.choice(cover_types)
            
            print(f"[Симуляция] Поиск книг с обложкой: {search_type}")
            if added_books_history:
                found_books = []
                for book in library.book_collection:
                    if book.cover_type == search_type:
                        found_books.append(book)
                
                print(f"  Найдено: {len(found_books)} книг")
                for book in found_books: 
                    print(f"    - {book}")
            else:
                print('[Симуляция] Библиотека пуста, поиск невозможен')


        elif event == 'search_by_author':
            if added_books_history:
                found_books = []
                search_author = random.choice(AUTHORS)
                print(f"[Симуляция] Поиск книг автора: {search_author}")
                for book in library.book_collection:
                    if book.author == search_author:
                        found_books.append(book)
                print(f"  Найдено: {len(found_books)} книг")
                for book in found_books: 
                    print(f"    - {book}")
            else:
                print('[Симуляция] Библиотека пуста, поиск невозможен')


        elif event == 'search_by_year':
            if added_books_history:
                found_books = []
                search_year = random.randint(1900, 2025)
                print(f"[Симуляция] Поиск книг {search_year} года")
                for book in library.book_collection:
                    if book.year == search_year:
                        found_books.append(book)
                print(f"  Найдено: {len(found_books)} книг")
                for book in found_books: 
                    print(f"    - {book}")
            else:
                print('[Симуляция] Библиотека пуста, поиск невозможен')

        
        elif event == 'search_by_genre':
            if added_books_history:
                found_books = []
                search_genre = random.choice(GENRES)
                print(f"[Симуляция] Поиск книг с жанром: {search_genre}")
                for book in library.book_collection:
                    if book.genre == search_genre:
                        found_books.append(book)
                print(f"  Найдено: {len(found_books)} книг")
                for book in found_books: 
                    print(f"    - {book}")
            else:
                print('[Симуляция] Библиотека пуста, поиск невозможен')
  
                
        elif event == 'check_condition':
            if added_books_history:
                sample_size = min(3, len(added_books_history))
                sample_books = random.sample(added_books_history, sample_size)
                
                print(f"[Симуляция] Проверка состояния книг:")
                for book in sample_books:
                    condition = book.get_condition()
                    print(f"  {book.title}: {condition}")        
            else:
                print('[Симуляция] Нет книг для проверки состояния')
                

        elif event == 'remove_book':
            if added_books_history:
                book = random.choice(added_books_history)
                print(f"[Симуляция] Удаляем книгу: {book.title}")
                success = library.remove_book_by_title(book.title)
                if success:
                    added_books_history.remove(book)
            else:
                print('[Симуляция] Нет книг для удаления')

            
        elif event == 'get_nonexistent':
            if added_books_history:
                fake_isbn = "ISBN-NOT-EXISTS"
                result = library.search_by_isbn(fake_isbn)
                if result is None:
                    print(f"Книга с ISBN '{fake_isbn}' не найдена")
                else:
                    print(f"Неожиданно найдена: {result}")

        
    print(f"Симуляция завершена. Книг в библиотеке: {len(added_books_history)}")


if __name__ == "__main__":
    run_simulation(steps = 40, seed = 42)