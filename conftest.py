import pytest
from main import BooksCollector


@pytest.fixture(scope="function")
def object_with_book():
    collector = BooksCollector()
    collector.add_new_book('Маленький принц')
    return collector


@pytest.fixture(scope="function")
def object_with_several_books():
    collector = BooksCollector()
    list_of_names = ['Маленький принц', 'Алиса в стране чудес', 'Гарри Поттер', 'Оно', 'Шерлок Холмс',
                     'Большая маленькая ложь', 'Не хочу взрослеть']
    list_of_genres = ['Мультфильмы', 'Мультфильмы', 'Фантастика', 'Ужасы', 'Детективы', 'Детективы', 'Комедии']
    for i in range(len(list_of_names)):
        collector.add_new_book(list_of_names[i])
        collector.set_book_genre(list_of_names[i], list_of_genres[i])
    return collector
