import pytest

from orders.mydb import *


# todo  create my conn
@pytest.fixture(scope ='module')
def cur():
    db = MyDB()
    conn = db.conn()
    cur = conn.cur()
    yield cur
    cur.close()
    conn.close()

def test_query1(cur):
    print('test query1...')
    id = cur.execute('query1')
    assert id == 1

def test_query2(cur):
    print('test query2...')
    id = cur.execute('query2')
    assert id == 2