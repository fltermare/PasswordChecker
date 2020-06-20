from src.passwdcheck import pwned_api_check
from tests.test_data import TestData
from unittest.mock import patch


def test_pwned_api_check():
    testdata = TestData()
    with patch("requests.get") as patcher:
        patcher.return_value = testdata

        res = pwned_api_check(testdata.password)
        assert res == testdata.ans_count
