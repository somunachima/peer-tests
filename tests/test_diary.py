from lib.diary import Diary
from unittest.mock import Mock

# def test_mock_read_diary_contents():
#     fake_diary = Mock("hello")
#     fake_diary.contents = "hello"
#     fake_diary.read.return_value == "hello"
#     assert fake_diary.read() == "hello"

def test_unit_read_diary_contents():
    diary = Diary("hello")
    assert diary.read() == "hello"