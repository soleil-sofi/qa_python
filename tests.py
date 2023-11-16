import pytest
from main import BooksCollector


class TestBooksCollector:
    @pytest.mark.parametrize("name", ["Маленький принц", "A", "Старик, который читал любовные романы..."],
                             ids=['name_of_15_characters', 'name_of_1_character', 'name_of_40_characters'])
    def test_add_new_book_unique_valid_name_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name in collector.get_books_genre() and collector.get_book_genre(name) == ''

    @pytest.mark.parametrize("name", ["", "Старик, который читал любовные романы...."],
                             ids=['empty_name', 'name_of_41_characters'])
    def test_add_new_book_unique_invalid_name_book_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    @pytest.mark.parametrize("genre", BooksCollector().genre)
    def test_set_book_genre_for_existing_book_and_genre_successfully(self, genre, object_with_book):
        name = list(object_with_book.books_genre.keys())[0]
        object_with_book.set_book_genre(name, genre)
        assert object_with_book.get_book_genre(name) == genre

    def test_get_book_genre_for_existing_book_successfully(self, object_with_book):
        name = list(object_with_book.books_genre.keys())[0]
        object_with_book.set_book_genre(name, "Мультфильмы")
        assert object_with_book.get_book_genre(name) == "Мультфильмы"

    def test_books_with_specific_genre_detectives_successfully(self, object_with_several_books):
        genres_list = object_with_several_books.get_books_with_specific_genre('Детективы')
        assert 'Большая маленькая ложь' in genres_list and 'Шерлок Холмс' in genres_list

    def test_get_books_genre(self, object_with_several_books):
        assert object_with_several_books.get_books_genre() == object_with_several_books.books_genre

    def test_get_books_for_children(self, object_with_several_books):
        book_list = object_with_several_books.get_books_for_children()
        for name in book_list:
            assert object_with_several_books.get_book_genre(name) not in object_with_several_books.genre_age_rating

    def test_add_book_in_favorites_it_added(self, object_with_several_books):
        object_with_several_books.add_book_in_favorites("Оно")
        assert "Оно" in object_with_several_books.get_list_of_favorites_books()

    def test_delete_book_from_favorites_it_deleted(self, object_with_several_books):
        object_with_several_books.add_book_in_favorites("Оно")
        object_with_several_books.add_book_in_favorites("Гарри Поттер")
        object_with_several_books.delete_book_from_favorites("Оно")
        assert ("Оно" not in object_with_several_books.get_list_of_favorites_books() and "Гарри Поттер" in
                object_with_several_books.get_list_of_favorites_books())

    def test_get_list_of_favorites_books(self, object_with_several_books):
        object_with_several_books.add_book_in_favorites("Оно")
        object_with_several_books.add_book_in_favorites("Гарри Поттер")
        assert object_with_several_books.get_list_of_favorites_books() == object_with_several_books.favorites
