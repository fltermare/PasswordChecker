from src.passwdcheck import request_api_data
from tests.test_data import TestData
from unittest.mock import patch


def test_request_api_data_success():

    testdata = TestData()
    with patch("requests.get") as patcher:
        patcher.return_value = testdata
        resp = request_api_data("12345")

        assert resp.status_code == 200


def test_request_api_data_fail():
    testdata = TestData()
    testdata.status_code = 404
    with patch("requests.get") as patcher:
        patcher.return_value = testdata

        try:
            resp = request_api_data("12345")
            assert False
        except RuntimeError:
            assert True
