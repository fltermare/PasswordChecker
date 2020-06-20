from src.passwdcheck import get_password_leaks_count
from tests.test_data import TestData
from unittest.mock import patch


def test_get_password_leaks_count_found():
    testdata = TestData()
    res = get_password_leaks_count(testdata, testdata.hash_to_check)
    assert res == testdata.ans_count


def test_get_password_leaks_count_not_found():
    testdata = TestData()
    testdata.hash_to_check = 'NOTFOUNDHASHSTRINGABCDEFGHIJKLMNOPQ'
    res = get_password_leaks_count(testdata, testdata.hash_to_check)
    assert res == 0
