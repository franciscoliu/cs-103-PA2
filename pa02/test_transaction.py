import pytest
from transaction import Transaction


@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')


@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    cat1 = {'item_number': '1', 'amount': 10, "category": "milk", "date": 20201105, "description": "testing milk"}
    cat2 = {'item_number': '2', 'amount': 20, "category": "car", "date": 20201105, "description": "testing car"}
    cat3 = {'item_number': '3', 'amount': 35, "category": "car", "date": 20201110, "description": "testing car two"}
    cat4 = {'item_number': '4', 'amount': 41, "category": "milk", "date": 20111205, "description": "testing milk"}
    cat5 = {'item_number': '5', 'amount': 5253, "category": "car", "date": 20011105, "description": "testing car"}
    cat6 = {'item_number': '6', 'amount': 323424, "category": "car", "date": 19931110, "description": "testing car two"}
    cat7 = {'item_number': '7', 'amount': 102242, "category": "phone", "date": 18321105, "description": "testing phone"}
    cat8 = {'item_number': '8', 'amount': 24430, "category": "car", "date": 19921105, "description": "testing car"}
    cat9 = {'item_number': '9', 'amount': 3424245, "category": "car", "date": 20011110, "description": "testing car"}
    cat10 = {'item_number': '10', 'amount': 13442250, "category": "milk", "date": 20031105, "description": "testing milk"}
    cat11 = {'item_number': '11', 'amount': 2255530, "category": "phone", "date": 20001105, "description": "testing phone"}
    cat12 = {'item_number': '12', 'amount': 3522535, "category": "book", "date": 20061110, "description": "testing book"}
    cat13 = {'item_number': '13', 'amount': 10553324, "category": "milk", "date": 20081105, "description": "testing milk"}
    cat14 = {'item_number': '14', 'amount': 262430, "category": "car", "date": 20211105, "description": "testing car"}
    cat15 = {'item_number': '15', 'amount': 3525553, "category": "wood", "date": 20211110, "description": "testing wood"}
    id1 = empty_db.add(cat1)
    id2 = empty_db.add(cat2)
    id3 = empty_db.add(cat3)
    id4 = empty_db.add(cat4)
    id5 = empty_db.add(cat5)
    id6 = empty_db.add(cat6)
    id7 = empty_db.add(cat7)
    id8 = empty_db.add(cat8)
    id9 = empty_db.add(cat9)
    id10 = empty_db.add(cat10)
    id11 = empty_db.add(cat11)
    id12 = empty_db.add(cat12)
    id13 = empty_db.add(cat13)
    id14 = empty_db.add(cat14)
    id15 = empty_db.add(cat15)
    yield empty_db
    empty_db.delete(id1)
    empty_db.delete(id2)
    empty_db.delete(id3)
    empty_db.delete(id4)
    empty_db.delete(id5)
    empty_db.delete(id6)
    empty_db.delete(id7)
    empty_db.delete(id8)
    empty_db.delete(id9)
    empty_db.delete(id10)
    empty_db.delete(id11)
    empty_db.delete(id12)
    empty_db.delete(id13)
    empty_db.delete(id14)
    empty_db.delete(id15)


@pytest.mark.add
def test_add(small_db):
    cat0 = {'item_number': '4', 'amount': 20, "category": "milk", "date": 20201120, "description": "testing milk in add"}
    cats0 = small_db.select_all()
    rowid = small_db.add(cat0)
    cats1 = small_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = small_db.select_one(rowid)
    assert cat1["amount"] == 20
    assert cat1["category"] == "milk"
    assert cat1["date"] == 20201120
    assert cat1["description"] == "testing milk in add"

# @pytest.mark.summarizemonth
# def test_summarize_by_month(small_db):
#
