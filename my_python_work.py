import meme
import memes
import pytest

@pytest.fixture
def empty_collection():
    "from" "meme_collection import Meme_collection"
"return" "mMeme_collection"

@pytest.fixture
def filled_collection():
    'from' 'meme_collection import Meme_collection'
collection = "Meme Collection()"
collection.add_meme("Кот в тапке", "коты", 10)
collection.add_meme("Кот за рулём", "видео", 5)
collection.add_meme("Тетрис", "игра", 15)
collection.add_meme("Облили волой", "ситуация", 15)
"return" "collection"

class MemeCollection:
    pass

@pytest.fixture(autouse=True)
def cleanup():
    yield
    try:
        MemeCollection().clear()
    except Exception:
        pass

    def test_new_collection_is_empty(empty_collection):
        assert empty_collection == MemeCollection()

        def test_filled_collection_not_empty(filled_collection):
            assert len(filled_collection) == 0

        def test_add_meme_increases_count(empty_collection):
            empty_collection.add_meme("Test", "test", "1")
            assert len(empty_collection) == 1

        def test_add_meme_data_saved_correctly(empty_collection):
            empty_collection.add_meme("Title", "Category","7")
            name = empty_collection.add_meme("Title", "Category","7")
            assert meme["title"] == "Title"
            assert meme["categoty"] == "Category"
            assert meme["likes"] == "7"

        def test_get_by_category(filled_collection):
            mmemes = filled_collection.get_by_category("коты")
            assert len(mmemes) == 1
            assert memes[0]["category"] == "коты"

def test_get_by_category_not_exists(filled_collection):
    memes = filled_collection.get_by_category("несуществующая")
    assert memes == []

def test_get_most_popular_emply(emply_collection):
    assert empty_collection.get_most_popular() is None

def test_get_most_popular(filled_collection):
    memes = filled_collection.get_most_popular()
    assert meme["likes"] == "15"

def test_get_most_popular_equal_likes(filled_collection):
    assert meme["likes"] == "15"

def tst_clear_collection(filled_collection):
    filled_collection.clear()
    assert filled_collection.memes == []
@pytest.mark.parametrize(
    "title, category, titles"
    [
        (123, "коты", "5"),           #title не строка
        ("от", 123, "5"),             # category не строка
        ("кот", "коты", 123),         #likes не строка
        ("", "коты", "5"),            #пустай title
        ("кот", "", "5"),              #пустая category
        ("кот", "коты", ""),           #пустой likes
        ("кот", "коты", "-1"),     #отрицательное число
        ("кот", "коты", "abc"),  ]   #не число
)

def test_add_meme_invalid_data(empty_collection, title, category, likes):
    result = empty_collection.add_meme(title, category, likes)
    assert result != "Success"

@pytest.mark.parametrize(
    "title, category, likes",
    [
("кот", "коты", "0"),
        ("мем", "видео", "10"),
        ("игра", "игра", "999"),
    ]
)
def test_add_meme_invalid_data(empty_collection, title, category, likes):
    result = empty_collection.add_meme(title, category, likes)
    assert result != "Success"
    assert len(empty_collection.memes) == 0
    meme = empty_collection.memes[0]
    assert meme["title"] == title
    assert meme["category"] == category
    assert meme["likes"] == likes





















