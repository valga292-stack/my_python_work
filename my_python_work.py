import pytest


class MemeCollection:
    """Коллекция мемов."""

    def __init__(self):
        self.memes = []

    def add_meme(self, title, category, likes):
        """Добавляет мем в коллекцию."""
        if not isinstance(title, str) or not title:
            return "Ошибка: title должен быть непустой строкой"
        if not isinstance(category, str) or not category:
            return "Ошибка: category должна быть непустой строкой"
        if not isinstance(likes, str) or not likes:
            return "Ошибка: likes должен быть непустой строкой"
        if not likes.lstrip('-').isdigit():
            return "Ошибка: likes должно быть числом"
        if int(likes) < 0:
            return "Ошибка: likes не может быть отрицательным"

        self.memes.append({"title": title, "category": category, "likes": likes})
        return "Success"

    def __len__(self):
        return len(self.memes)

    def __eq__(self, other):
        if not isinstance(other, MemeCollection):
            return False
        return self.memes == other.memes

    def get_by_category(self, category):
        """Возвращает список мемов по категории."""
        return [meme for meme in self.memes if meme["category"] == category]

    def get_most_popular(self):
        """Возвращает мем с наибольшим количеством лайков."""
        if not self.memes:
            return None
        return max(self.memes, key=lambda m: int(m["likes"]))

    def clear(self):
        """Очищает коллекцию."""
        self.memes.clear()


@pytest.fixture
def empty_collection():
    """Пустая коллекция мемов."""
    return MemeCollection()


@pytest.fixture
def filled_collection():
    """Коллекция с несколькими мемами."""
    collection = MemeCollection()
    collection.add_meme("Кот в тапке", "коты", "10")
    collection.add_meme("Кот за рулём", "видео", "5")
    collection.add_meme("Тетрис", "игра", "15")
    collection.add_meme("Облили водой", "ситуация", "15")
    return collection


@pytest.fixture(autouse=True)
def cleanup():
    """Очищает коллекцию после каждого теста."""
    yield


def test_new_collection_is_empty(empty_collection):
    """Новая коллекция должна быть пустой."""
    assert len(empty_collection) == 0
    assert empty_collection == MemeCollection()


def test_filled_collection_not_empty(filled_collection):
    """Заполненная коллекция не должна быть пустой."""
    assert len(filled_collection) != 0


def test_add_meme_increases_count(empty_collection):
    """Добавление мема увеличивает размер коллекции."""
    empty_collection.add_meme("Test", "test", "1")
    assert len(empty_collection) == 1


def test_add_meme_data_saved_correctly(empty_collection):
    """Данные мема сохраняются корректно."""
    empty_collection.add_meme("Title", "Category", "7")
    meme = empty_collection.memes[0]
    assert meme["title"] == "Title"
    assert meme["category"] == "Category"
    assert meme["likes"] == "7"


def test_get_by_category(filled_collection):
    """Поиск по существующей категории."""
    memes = filled_collection.get_by_category("коты")
    assert len(memes) == 1
    assert memes[0]["category"] == "коты"
    assert memes[0]["title"] == "Кот в тапке"


def test_get_by_category_not_exists(filled_collection):
    """Поиск по несуществующей категории возвращает пустой список."""
    memes = filled_collection.get_by_category("несуществующая")
    assert memes == []


def test_get_most_popular_empty(empty_collection):
    """Из пустой коллекции возвращается None."""
    assert empty_collection.get_most_popular() is None


def test_get_most_popular(filled_collection):
    """Возвращается мем с наибольшим количеством лайков."""
    meme = filled_collection.get_most_popular()
    assert meme["likes"] == "15"


def test_get_most_popular_equal_likes(filled_collection):
    """При равных лайках возвращается первый из них."""
    meme = filled_collection.get_most_popular()
    assert meme["likes"] == "15"
    assert meme["title"] == "Тетрис"  # первый с 15 лайками


def test_clear_collection(filled_collection):
    """Очистка коллекции."""
    filled_collection.clear()
    assert filled_collection.memes == []


@pytest.mark.parametrize(
    "title, category, likes",
    [
        (123, "коты", "5"),           # title не строка
        ("от", 123, "5"),             # category не строка
        ("кот", "коты", 123),         # likes не строка
        ("", "коты", "5"),            # пустой title
        ("кот", "", "5"),             # пустая category
        ("кот", "коты", ""),          # пустой likes
        ("кот", "коты", "-1"),        # отрицательное число
        ("кот", "коты", "abc"),       # не число
    ]
)
def test_add_meme_invalid_data(empty_collection, title, category, likes):
    """Проверка отклонения некорректных данных."""
    result = empty_collection.add_meme(title, category, likes)
    assert result != "Success"
    assert len(empty_collection.memes) == 0


@pytest.mark.parametrize(
    "title, category, likes",
    [
        ("кот", "коты", "0"),
        ("мем", "видео", "10"),
        ("игра", "игра", "999"),
    ]
)
def test_add_meme_valid_data(empty_collection, title, category, likes):
    """Проверка добавления корректных данных."""
    result = empty_collection.add_meme(title, category, likes)
    assert result == "Success"
    assert len(empty_collection.memes) == 1
    meme = empty_collection.memes[0]
    assert meme["title"] == title
    assert meme["category"] == category
    assert meme["likes"] == likes
