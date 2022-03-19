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
    id1 = empty_db.add(cat1)
    id2 = empty_db.add(cat2)
    id3 = empty_db.add(cat3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

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
