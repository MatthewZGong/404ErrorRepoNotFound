import pytest

import db.db_connect as dbc

TEST_DB = dbc.DB_NAME
TEST_COLLECT = "test_collect"
# can be used for field and value:
TEST_NAME = "test"


@pytest.fixture(scope="function")
def temp_rec():
    dbc.connect_db()
    dbc.client[TEST_DB][TEST_COLLECT].insert_one({TEST_NAME: TEST_NAME})
    # yield to our test function
    # delete_one operation will not be executed until the test function, which
    # is using the temp_rec fixture, has completed or it explicitly calls next()
    yield
    dbc.client[TEST_DB][TEST_COLLECT].delete_one({TEST_NAME: TEST_NAME})


def test_fetch_one(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: TEST_NAME})
    assert ret is not None


def test_fetch_one_not_there(temp_rec):
    ret = dbc.fetch_one(TEST_COLLECT, {TEST_NAME: "not a field value in db!"})
    assert ret is None
